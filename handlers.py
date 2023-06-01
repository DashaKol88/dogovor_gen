import logging
from typing import Any, Coroutine

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, KeyboardButton, InputFile, Bot
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters, CallbackContext,
)

from pdf_service.pdf_generator import generate_pdf_with_jinja
from pdf_service.templates.generate_with_format import generate_pdf_with_format
from userdata import *

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

LAST_NAME, FIRST_NAME, MIDDLE_NAME, PHONE_NUM, P_SER, P_NUM, P_ISS_B, P_ISS_D, REG_ADDR, TAX_ID, CHECK, THANK, CORRECTION, CORRECT_HANDLER = range(
    14)


async def send_pdf_document(bot: Bot, chat_id: int, document_path: str, caption: str = "") -> None:
    """
    Sends a PDF document to the specified chat using the Telegram bot.

    Parameters:
    - bot: A Bot instance representing the Telegram bot.
    - chat_id: An integer representing the ID of the chat to send the document to.
    - document_path: A string specifying the path to the PDF document file.
    - caption: (optional) A string representing the caption for the document.

    Returns:
    - None
    """
    with open(document_path, 'rb') as file:
        await bot.send_document(chat_id=chat_id, document=InputFile(file), caption=caption)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Starts the conversation and asks the user for their name.

    Parameters:
    - update: An Update object containing information about the incoming message or event.
    - context: A Context object providing access to the shared state and bot's functions.

    Returns:
    - int: The state code for transitioning to the next dialog step.
    """
    user = update.message.from_user

    customer = Customer()
    context.user_data['customer'] = customer
    context.user_data['customer'].set_username(user.first_name)

    await update.message.reply_text(
        "Привіт, я БОТ для генераціі PDF договору!\n"
        "Відправте /cancel для того щоб зупинити мене.\n\n")

    await update.message.reply_text("Введіть, будь ласка, Ваше прізвище:")

    return LAST_NAME


async def lastname(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Handles the user's last name input and sets it in the Customer object.

    Parameters:
    - update: An Update object containing information about the incoming message or event.
    - context: A Context object providing access to the shared state and bot's functions.

    Returns:
    - int: The state code for transitioning to the next dialog step.
    """

    user = update.message.from_user
    logger.info("Last name of %s: %s", user.first_name, update.message.text)

    try:
        context.user_data['customer'].set_lastname(update.message.text)
    except ValueError as err:
        await context.bot.send_message(chat_id=update.message.chat_id, text=str(err))
        return LAST_NAME

    await update.message.reply_text("Дякую.\nТепер введіть, будь ласка, Ваше ім'я:")
    return FIRST_NAME


async def firstname(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Handles the user's first name input and sets it in the Customer object.

    Parameters:
    - update: An Update object containing information about the incoming message or event.
    - context: A Context object providing access to the shared state and bot's functions.

    Returns:
    - int: The state code for transitioning to the next dialog step.
    """

    user = update.message.from_user
    logger.info("First name of %s: %s", user.first_name, update.message.text)

    try:
        context.user_data['customer'].set_firstname(update.message.text)
    except ValueError as err:
        await context.bot.send_message(chat_id=update.message.chat_id, text=str(err))
        return FIRST_NAME

    await update.message.reply_text("Дякую.\nТепер введіть, будь ласка, Ваше по батькові:")

    return MIDDLE_NAME


async def middle_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Handles the user's middle name input and sets it in the Customer object.

    Parameters:
    - update: An Update object containing information about the incoming message or event.
    - context: A Context object providing access to the shared state and bot's functions.

    Returns:
    - int: The state code for transitioning to the next dialog step.
    """

    user = update.message.from_user
    logger.info("Middle name of %s: %s", user.first_name, update.message.text)

    try:
        context.user_data['customer'].set_middle_name(update.message.text)
    except ValueError as err:
        await context.bot.send_message(chat_id=update.message.chat_id, text=str(err))
        return MIDDLE_NAME

    await update.message.reply_text("Дякую.\nТепер введіть, будь ласка, свій номер телефону (10 цифр):")

    return PHONE_NUM


async def phonenum(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Handles the user's phone number input and sets it in the Customer object.

    Parameters:
    - update: An Update object containing information about the incoming message or event.
    - context: A Context object providing access to the shared state and bot's functions.

    Returns:
    - int: The state code for transitioning to the next dialog step.
    """
    user = update.message.from_user
    logger.info("Phone number of %s: %s", user.first_name, update.message.text)

    try:
        context.user_data['customer'].set_phone_number(update.message.text)
    except ValueError as err:
        await context.bot.send_message(chat_id=update.message.chat_id, text=str(err))
        return PHONE_NUM

    await update.message.reply_text("Дякую.\nТепер введіть, будь ласка, серію паспорту:")
    return P_SER


async def pas_ser(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Handles the user's passport series input and sets it in the Customer object.

    Parameters:
    - update: An Update object containing information about the incoming message or event.
    - context: A Context object providing access to the shared state and bot's functions.

    Returns:
    - int: The state code for transitioning to the next dialog step.
    """
    user = update.message.from_user
    logger.info("Passport series of %s: %s", user.first_name, update.message.text)

    try:
        context.user_data['customer'].set_passport_series(update.message.text)
    except ValueError as err:
        await context.bot.send_message(chat_id=update.message.chat_id, text=str(err))
        return P_SER

    await update.message.reply_text("Дякую.\nТепер введіть, будь ласка, номер паспорту:")
    return P_NUM


async def pas_num(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Handles the user's passport number input and sets it in the Customer object.

    Parameters:
    - update: An Update object containing information about the incoming message or event.
    - context: A Context object providing access to the shared state and bot's functions.

    Returns:
    - int: The state code for transitioning to the next dialog step.
    """
    user = update.message.from_user
    logger.info("Passport number of %s: %s", user.first_name, update.message.text)

    try:
        context.user_data['customer'].set_passport_number(update.message.text)
    except ValueError as err:
        await context.bot.send_message(chat_id=update.message.chat_id, text=str(err))
        return P_NUM

    await update.message.reply_text("Дякую.\nТепер введіть, будь ласка, ким виданий паспорт:")
    return P_ISS_B


async def pas_iss_by(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Handles the user's passport issuing authority input and sets it in the Customer object.

    Parameters:
    - update: An Update object containing information about the incoming message or event.
    - context: A Context object providing access to the shared state and bot's functions.

    Returns:
    - int: The state code for transitioning to the next dialog step.
    """
    user = update.message.from_user
    logger.info("Passport issued by of %s: %s", user.first_name, update.message.text)

    try:
        context.user_data['customer'].set_passport_issued_by(update.message.text)
    except ValueError as err:
        await context.bot.send_message(chat_id=update.message.chat_id, text=str(err))
        return P_ISS_B

    await update.message.reply_text(
        f"Дякую.\nТепер введіть, будь ласка, дату видачі паспорту у форматі день.місяць.рік (наприклад, {date.today().strftime('%d.%m.%Y')}):")
    return P_ISS_D


async def pas_iss_date(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Handles the user's passport issuance date input and sets it in the Customer object.

    Parameters:
    - update: An Update object containing information about the incoming message or event.
    - context: A Context object providing access to the shared state and bot's functions.

    Returns:
    - int: The state code for transitioning to the next dialog step.
    """
    user = update.message.from_user
    logger.info("Passport issued date of %s: %s", user.first_name, update.message.text)

    try:
        context.user_data['customer'].set_passport_issued_date(update.message.text)
    except ValueError as err:
        await context.bot.send_message(chat_id=update.message.chat_id, text=str(err))
        return P_ISS_D

    await update.message.reply_text("Дякую.\nТепер введіть, будь ласка, адресу реестрації:")
    return REG_ADDR


async def reg_address(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Handles the user's registration address input and sets it in the Customer object.

    Parameters:
    - update: An Update object containing information about the incoming message or event.
    - context: A Context object providing access to the shared state and bot's functions.

    Returns:
    - int: The state code for transitioning to the next dialog step.
    """
    user = update.message.from_user
    logger.info("Registration address of %s: %s", user.first_name, update.message.text)

    try:
        context.user_data['customer'].set_registration_address(update.message.text)
    except ValueError as err:
        await context.bot.send_message(chat_id=update.message.chat_id, text=str(err))
        return REG_ADDR

    await update.message.reply_text("Дякую.\nТепер введіть, будь ласка, ідентифікаційний код:")
    return TAX_ID


async def tax_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Handles the user's tax ID input and sets it in the Customer object.

    Parameters:
    - update: An Update object containing information about the incoming message or event.
    - context: A Context object providing access to the shared state and bot's functions.

    Returns:
    - int: The state code for transitioning to the next dialog step.
    """
    user = update.message.from_user
    logger.info("ID code of %s: %s", user.first_name, update.message.text)

    try:
        context.user_data['customer'].set_id_code(update.message.text)
    except ValueError as err:
        await context.bot.send_message(chat_id=update.message.chat_id, text=str(err))
        return TAX_ID

    await update.message.reply_text("Дякую.\nНаразі мені відомі такі данні про вас:")
    await update.message.reply_text(context.user_data['customer'].print_info(), parse_mode='html')
    reply_keyboard = [["Вірно", "Невірно"]]
    await update.message.reply_text("Тепер перевірте, будь ласка, чи всі дані введено вірно",
                                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True,
                                                                     input_field_placeholder="Вірно чи невірно?"), )

    return CHECK


async def check(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Handles the user's verification of entered data.

    Parameters:
    - update: An Update object containing information about the incoming message or event.
    - context: A Context object providing access to the shared state and bot's functions.

    Returns:
    - int: The state code for transitioning to the next dialog step or ending the conversation.
    """
    user_choice = update.message.text.lower()

    if user_choice == "вірно":
        user = update.message.from_user
        customer = context.user_data['customer']
        output_path = generate_pdf_with_jinja(customer, user.id)
        await send_pdf_document(context.bot, update.message.chat_id, output_path, caption="Ваш договір")
        # output_path = generate_pdf_with_format(customer, user.id)
        await update.message.reply_text("Дякую.")

        return ConversationHandler.END
    elif user_choice == "невірно":
        reply_keyboard = [
            ["Ім'я", "Прізвище"], ["По батькові", "Номер телефону"], ["Серія паспорта", "Номер паспорта"],
            ["Ким виданий паспорт",
             "Дата видачі паспорта"], ["Адреса реєстрації", "Ідентифікаційний код"]]

        await update.message.reply_text(
            "Вкажіть, будь ласка, які дані невірні",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
        )

        return CORRECTION
    else:
        await update.message.reply_text("Будь ласка, оберіть один з доступних варіантів.")
        return CHECK


async def correct_handler(update: Update, context: CallbackContext) -> int:
    try:
        method_to_call = getattr(context.user_data['customer'], context.user_data['correction_method'])
        method_to_call(update.message.text)
    except ValueError as err:
        await context.bot.send_message(chat_id=update.message.chat_id, text=str(err))
        return CORRECT_HANDLER

    await update.message.reply_text("Дякую.\nНаразі мені відомі такі данні про вас:")
    await update.message.reply_text(context.user_data['customer'].print_info(), parse_mode='html')
    reply_keyboard = [["Вірно", "Невірно"]]
    await update.message.reply_text("Тепер перевірте, будь ласка, чи всі дані введено вірно",
                                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True,
                                                                     input_field_placeholder="Вірно чи невірно?"), )
    return CHECK


async def correction_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    correction_messages = {
        "Ім'я": ["set_firstname", "Тепер введіть, будь ласка, Ваше ім'я:"],
        "Прізвище": ["set_lastname", "Тепер введіть, будь ласка, Ваше прізвище:"],
        "По батькові": ["set_middle_name", "Тепер введіть, будь ласка, Ваше по батькові:"],
        "Номер телефону": ["set_phone_number", "Тепер введіть, будь ласка, Ваш номер телефону:"],
        "Серія паспорта": ["set_passport_series", "Тепер введіть, будь ласка, серію паспорта:"],
        "Номер паспорта": ["set_passport_number", "Тепер введіть, будь ласка, номер паспорта:"],
        "Ким виданий паспорт": ["set_passport_issued_by", "Тепер введіть, будь ласка, ким виданий паспорт:"],
        "Дата видачі паспорта": ["set_passport_issued_date", "Тепер введіть, будь ласка, дату видачі паспорта:"],
        "Адреса реєстрації": ["set_registration_address", "Тепер введіть, будь ласка, адресу реєстрації:"],
        "Ідентифікаційний код": ["set_id_code", "Тепер введіть, будь ласка, ідентифікаційний код:"]
    }

    incorrect_data = update.message.text

    set_method, message = correction_messages.get(incorrect_data)
    context.user_data['correction_method'] = set_method
    await update.message.reply_text(message)

    return CORRECT_HANDLER


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Handles the cancellation of the conversation.

    Parameters:
    - update: An Update object containing information about the incoming message or event.
    - context: A ContextTypes.DEFAULT_TYPE object providing access to the shared state and bot's functions.

    Returns:
    - int: The state code for ending the conversation.
    """
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        "До побачення! Сподіваюся, колись ми знову поговоримо.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END
