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

LAST_NAME, FIRST_NAME, MIDDLE_NAME, PHONE_NUM, P_SER, P_NUM, P_ISS_B, P_ISS_D, REG_ADDR, TAX_ID, CHECK, THANK, CORRECTION, CORRECT_FIRST_NAME, CORRECT_LAST_NAME, CORRECT_MIDDLE_NAME, CORRECT_PHONE_NUM, CORRECT_P_SER, CORRECT_P_NUM, CORRECT_P_ISS_B, CORRECT_P_ISS_D, CORRECT_REG_ADDR, CORRECT_TAX_ID = range(
    23)


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

    await update.message.reply_text("Дякую.")
    await update.message.reply_text("Тепер введіть, будь ласка, Ваше ім'я:")
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

    await update.message.reply_text("Дякую.")
    await update.message.reply_text("Тепер введіть, будь ласка, Ваше по батькові:")

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

    await update.message.reply_text("Дякую.")
    await update.message.reply_text("Тепер введіть, будь ласка, свій номер телефону (10 цифр):")

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

    await update.message.reply_text("Дякую.")
    await update.message.reply_text("Тепер введіть, будь ласка, серію паспорту:")
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

    await update.message.reply_text("Дякую.")
    await update.message.reply_text("Тепер введіть, будь ласка, номер паспорту:")
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

    await update.message.reply_text("Дякую.")
    await update.message.reply_text("Тепер введіть, будь ласка, ким виданий паспорт:")
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

    # context.user_data['customer'].set_passport_issued_by(update.message.text)
    await update.message.reply_text("Дякую.")
    await update.message.reply_text(
        f"Тепер введіть, будь ласка, дату видачі паспорту у форматі день.місяць.рік (наприклад, {date.today().strftime('%d.%m.%Y')}):")
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

    await update.message.reply_text("Дякую.")
    await update.message.reply_text("Тепер введіть, будь ласка, адресу реестрації:")
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

    # context.user_data['customer'].set_registration_address(update.message.text)
    await update.message.reply_text("Дякую.")
    await update.message.reply_text("Тепер введіть, будь ласка, ідентифікаційний код:")
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

    await update.message.reply_text("Дякую.")
    await update.message.reply_text("Наразі мені відомі такі данні про вас:")
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
        output_path = generate_pdf_with_format(customer, user.id)
        await update.message.reply_text("Дякую.")

        return ConversationHandler.END
    elif user_choice == "невірно":
        reply_keyboard = [
            ["Ім'я", "Прізвище", "По батькові", "Номер телефону", "Серія паспорта", "Номер паспорта",
             "Ким виданий паспорт",
             "Дата видачі паспорта", "Адреса реєстрації", "Ідентифікаційний код"]]

        await update.message.reply_text(
            "Вкажіть, будь ласка, які дані невірні",
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
        )

        return CORRECTION
    else:
        await update.message.reply_text("Будь ласка, оберіть один з доступних варіантів.")
        return CHECK


async def correct_first_name(update: Update, context: CallbackContext) -> int:
    """
    Handles the correction of the user's first name.

    Parameters:
    - update: An Update object containing information about the incoming message or event.
    - context: A CallbackContext object providing access to the shared state and bot's functions.

    Returns:
    - int: The state code for transitioning to the next dialog step.
    """
    new_first_name = update.message.text
    try:
        context.user_data['customer'].set_firstname(new_first_name)
    except ValueError as err:
        await context.bot.send_message(chat_id=update.message.chat_id, text=str(err))
        return CORRECT_FIRST_NAME
    await update.message.reply_text("Дякую.")
    await update.message.reply_text("Наразі мені відомі такі данні про вас:")
    await update.message.reply_text(context.user_data['customer'].print_info(), parse_mode='html')
    reply_keyboard = [["Вірно", "Невірно"]]
    await update.message.reply_text("Тепер перевірте, будь ласка, чи всі дані введено вірно",
                                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True,
                                                                     input_field_placeholder="Вірно чи невірно?"), )
    return CHECK


async def correct_last_name(update: Update, context: CallbackContext) -> int:
    """
    Handles the correction of the user's last name.

    Parameters:
    - update: An Update object containing information about the incoming message or event.
    - context: A CallbackContext object providing access to the shared state and bot's functions.

    Returns:
    - int: The state code for transitioning to the next dialog step.
    """
    new_last_name = update.message.text
    try:
        context.user_data['customer'].set_last_name(new_last_name)
    except ValueError as err:
        await context.bot.send_message(chat_id=update.message.chat_id, text=str(err))
        return CORRECT_LAST_NAME
    await update.message.reply_text("Дякую.")
    await update.message.reply_text("Наразі мені відомі такі данні про вас:")
    await update.message.reply_text(context.user_data['customer'].print_info(), parse_mode='html')
    reply_keyboard = [["Вірно", "Невірно"]]
    await update.message.reply_text("Тепер перевірте, будь ласка, чи всі дані введено вірно",
                                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True,
                                                                     input_field_placeholder="Вірно чи невірно?"), )
    return CHECK


async def correct_middle_name(update: Update, context: CallbackContext) -> int:
    """
    Handles the correction of the user's middle name.

    Parameters:
    - update: An Update object containing information about the incoming message or event.
    - context: A CallbackContext object providing access to the shared state and bot's functions.

    Returns:
    - int: The state code for transitioning to the next dialog step.
    """
    new_middle_name = update.message.text
    try:
        context.user_data['customer'].set_middle_name(new_middle_name)
    except ValueError as err:
        await context.bot.send_message(chat_id=update.message.chat_id, text=str(err))
        return CORRECT_MIDDLE_NAME
    await update.message.reply_text("Дякую.")
    await update.message.reply_text("Наразі мені відомі такі данні про вас:")
    await update.message.reply_text(context.user_data['customer'].print_info(), parse_mode='html')
    reply_keyboard = [["Вірно", "Невірно"]]
    await update.message.reply_text("Тепер перевірте, будь ласка, чи всі дані введено вірно",
                                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True,
                                                                     input_field_placeholder="Вірно чи невірно?"), )
    return CHECK


async def correct_phone_num(update: Update, context: CallbackContext) -> int:
    """
    Handles the correction of the user's phone number.

    Parameters:
    - update: An Update object containing information about the incoming message or event.
    - context: A CallbackContext object providing access to the shared state and bot's functions.

    Returns:
    - int: The state code for transitioning to the next dialog step.
    """
    new_phone_number = update.message.text
    try:
        context.user_data['customer'].set_phone_number(new_phone_number)
    except ValueError as err:
        await context.bot.send_message(chat_id=update.message.chat_id, text=str(err))
        return CORRECT_PHONE_NUM
    await update.message.reply_text("Дякую.")
    await update.message.reply_text("Наразі мені відомі такі данні про вас:")
    await update.message.reply_text(context.user_data['customer'].print_info(), parse_mode='html')
    reply_keyboard = [["Вірно", "Невірно"]]
    await update.message.reply_text("Тепер перевірте, будь ласка, чи всі дані введено вірно",
                                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True,
                                                                     input_field_placeholder="Вірно чи невірно?"), )
    return CHECK


async def correct_pas_ser(update: Update, context: CallbackContext) -> int:
    """
    Handles the correction of the user's passport series.

    Parameters:
    - update: An Update object containing information about the incoming message or event.
    - context: A CallbackContext object providing access to the shared state and bot's functions.

    Returns:
    - int: The state code for transitioning to the next dialog step.
    """
    new_passport_series = update.message.text
    try:
        context.user_data['customer'].set_passport_series(new_passport_series)
    except ValueError as err:
        await context.bot.send_message(chat_id=update.message.chat_id, text=str(err))
        return CORRECT_P_SER
    await update.message.reply_text("Дякую.")
    await update.message.reply_text("Наразі мені відомі такі данні про вас:")
    await update.message.reply_text(context.user_data['customer'].print_info(), parse_mode='html')
    reply_keyboard = [["Вірно", "Невірно"]]
    await update.message.reply_text("Тепер перевірте, будь ласка, чи всі дані введено вірно",
                                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True,
                                                                     input_field_placeholder="Вірно чи невірно?"), )
    return CHECK


async def correct_pas_num(update: Update, context: CallbackContext) -> int:
    """
    Handles the correction of the user's passport number.

    Parameters:
    - update: An Update object containing information about the incoming message or event.
    - context: A CallbackContext object providing access to the shared state and bot's functions.

    Returns:
    - int: The state code for transitioning to the next dialog step.
    """
    new_passport_number = update.message.text
    try:
        context.user_data['customer'].set_passport_number(new_passport_number)
    except ValueError as err:
        await context.bot.send_message(chat_id=update.message.chat_id, text=str(err))
        return CORRECT_P_NUM
    await update.message.reply_text("Дякую.")
    await update.message.reply_text("Наразі мені відомі такі данні про вас:")
    await update.message.reply_text(context.user_data['customer'].print_info(), parse_mode='html')
    reply_keyboard = [["Вірно", "Невірно"]]
    await update.message.reply_text("Тепер перевірте, будь ласка, чи всі дані введено вірно",
                                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True,
                                                                     input_field_placeholder="Вірно чи невірно?"), )
    return CHECK


async def correct_pas_iss_by(update: Update, context: CallbackContext) -> int:
    """
    Handles the correction of the user's passport issued by.

    Parameters:
    - update: An Update object containing information about the incoming message or event.
    - context: A CallbackContext object providing access to the shared state and bot's functions.

    Returns:
    - int: The state code for transitioning to the next dialog step.
    """
    new_pas_iss_by = update.message.text
    try:
        context.user_data['customer'].set_passport_issued_by(new_pas_iss_by)
    except ValueError as err:
        await context.bot.send_message(chat_id=update.message.chat_id, text=str(err))
        return CORRECT_P_ISS_B
    await update.message.reply_text("Дякую.")
    await update.message.reply_text("Наразі мені відомі такі данні про вас:")
    await update.message.reply_text(context.user_data['customer'].print_info(), parse_mode='html')
    reply_keyboard = [["Вірно", "Невірно"]]
    await update.message.reply_text("Тепер перевірте, будь ласка, чи всі дані введено вірно",
                                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True,
                                                                     input_field_placeholder="Вірно чи невірно?"), )
    return CHECK


async def correct_pas_iss_date(update: Update, context: CallbackContext) -> int:
    """
    Handles the correction of the user's passport issued date.

    Parameters:
    - update: An Update object containing information about the incoming message or event.
    - context: A CallbackContext object providing access to the shared state and bot's functions.

    Returns:
    - int: The state code for transitioning to the next dialog step.
    """
    new_pas_iss_date = update.message.text
    try:
        context.user_data['customer'].set_passport_issued_date(new_pas_iss_date)
    except ValueError as err:
        await context.bot.send_message(chat_id=update.message.chat_id, text=str(err))
        return CORRECT_P_ISS_D
    await update.message.reply_text("Дякую.")
    await update.message.reply_text("Наразі мені відомі такі данні про вас:")
    await update.message.reply_text(context.user_data['customer'].print_info(), parse_mode='html')
    reply_keyboard = [["Вірно", "Невірно"]]
    await update.message.reply_text("Тепер перевірте, будь ласка, чи всі дані введено вірно",
                                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True,
                                                                     input_field_placeholder="Вірно чи невірно?"), )
    return CHECK


async def correct_reg_address(update: Update, context: CallbackContext) -> int:
    """
    Handles the correction of the user's registration address.

    Parameters:
    - update: An Update object containing information about the incoming message or event.
    - context: A CallbackContext object providing access to the shared state and bot's functions.

    Returns:
    - int: The state code for transitioning to the next dialog step.
    """
    new_reg_address = update.message.text
    try:
        context.user_data['customer'].set_registration_address(new_reg_address)
    except ValueError as err:
        await context.bot.send_message(chat_id=update.message.chat_id, text=str(err))
        return CORRECT_REG_ADDR
    await update.message.reply_text("Дякую.")
    await update.message.reply_text("Наразі мені відомі такі данні про вас:")
    await update.message.reply_text(context.user_data['customer'].print_info(), parse_mode='html')
    reply_keyboard = [["Вірно", "Невірно"]]
    await update.message.reply_text("Тепер перевірте, будь ласка, чи всі дані введено вірно",
                                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True,
                                                                     input_field_placeholder="Вірно чи невірно?"), )
    return CHECK


async def correct_tax_id(update: Update, context: CallbackContext) -> int:
    """
    Handles the correction of the user's tax ID.

    Parameters:
    - update: An Update object containing information about the incoming message or event.
    - context: A CallbackContext object providing access to the shared state and bot's functions.

    Returns:
    - int: The state code for transitioning to the next dialog step.
    """
    new_tax_id = update.message.text
    try:
        context.user_data['customer'].set_id_code(new_tax_id)
    except ValueError as err:
        await context.bot.send_message(chat_id=update.message.chat_id, text=str(err))
        return CORRECT_TAX_ID
    await update.message.reply_text("Дякую.")
    await update.message.reply_text("Наразі мені відомі такі данні про вас:")
    await update.message.reply_text(context.user_data['customer'].print_info(), parse_mode='html')
    reply_keyboard = [["Вірно", "Невірно"]]
    await update.message.reply_text("Тепер перевірте, будь ласка, чи всі дані введено вірно",
                                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True,
                                                                     input_field_placeholder="Вірно чи невірно?"), )
    return CHECK


async def handle_correction(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Handles the correction of user data based on the incorrect data provided.

    Parameters:
    - update: An Update object containing information about the incoming message or event.
    - context: A ContextTypes.DEFAULT_TYPE object providing access to the shared state and bot's functions.

    Returns:
    - int: The state code for transitioning to the next dialog step.
    """
    incorrect_data = update.message.text

    if incorrect_data == "Ім'я":
        await update.message.reply_text("Тепер введіть, будь ласка, Ваше ім'я:")
        return CORRECT_FIRST_NAME
    elif incorrect_data == "Прізвище":
        await update.message.reply_text("Тепер введіть, будь ласка, Ваше прізвище:")
        return CORRECT_LAST_NAME
    elif incorrect_data == "По батькові":
        await update.message.reply_text("Тепер введіть, будь ласка, Ваше по батькові:")
        return CORRECT_MIDDLE_NAME
    elif incorrect_data == "Номер телефону":
        await update.message.reply_text("Тепер введіть, будь ласка, Ваш номер телефону:")
        return CORRECT_PHONE_NUM
    elif incorrect_data == "Серія паспорта":
        await update.message.reply_text("Тепер введіть, будь ласка, серію паспорта:")
        return CORRECT_P_SER
    elif incorrect_data == "Номер паспорта":
        await update.message.reply_text("Тепер введіть, будь ласка, номер паспорта:")
        return CORRECT_P_NUM
    elif incorrect_data == "Ким виданий паспорт":
        await update.message.reply_text("Тепер введіть, будь ласка, ким виданий паспорт:")
        return CORRECT_P_ISS_B
    elif incorrect_data == "Дата видачі паспорта":
        await update.message.reply_text("Тепер введіть, будь ласка, дату видачі паспорта:")
        return CORRECT_P_ISS_D
    elif incorrect_data == "Адреса реєстрації":
        await update.message.reply_text("Тепер введіть, будь ласка, адресу реєстрації:")
        return CORRECT_REG_ADDR
    elif incorrect_data == "Ідентифікаційний код":
        await update.message.reply_text("Тепер введіть, будь ласка, ідентифікаційний код:")
        return CORRECT_TAX_ID


# async def thanks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     """
#     Handles the completion of the conversation flow and sends the generated PDF document to the user.
#
#     Parameters:
#     - update: An Update object containing information about the incoming message or event.
#     - context: A Context object providing access to the shared state and bot's functions.
#
#     Returns:
#     - int: The state code for ending the conversation handler.
#     """
#     user = update.message.from_user
#     customer = context.user_data['customer']
#     output_path = generate_pdf_with_jinja(customer, user.id)
#     await send_pdf_document(context.bot, update.message.chat_id, output_path, caption="Ваш договір")
#     output_path = generate_pdf_with_format(customer, user.id)
#     await update.message.reply_text("Дякую.")
#
#     return ConversationHandler.END


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
