import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from userdata import *

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

LAST_NAME, FIRST_NAME, MIDDLE_NAME, PHONE_NUM, P_SER, P_NUM, P_ISS_B, P_ISS_D, REG_ADDR, TAX_ID, CHECK, THANK, PDF_GEN = range(
    13)


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
    # await update.message.reply_text("Наразі мені відомі такі данні про Вас:")
    # await update.message.reply_text(customer.print_info(), parse_mode='html')
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
    # await update.message.reply_text("Наразі мені відомі такі данні про Вас:")
    # await update.message.reply_text(context.user_data['customer'].print_info(), parse_mode='html')
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
    # await update.message.reply_text("Наразі мені відомі такі данні про Вас:")
    # await update.message.reply_text(context.user_data['customer'].print_info(), parse_mode='html')
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
    # await update.message.reply_text("Наразі мені відомі такі данні про вас:")
    # await update.message.reply_text(context.user_data['customer'].print_info(), parse_mode='html')
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
    # await update.message.reply_text("Наразі мені відомі такі данні про вас:")
    # await update.message.reply_text(context.user_data['customer'].print_info(), parse_mode='html')
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
    # await update.message.reply_text("Наразі мені відомі такі данні про вас:")
    # await update.message.reply_text(context.user_data['customer'].print_info(), parse_mode='html')
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

    context.user_data['customer'].set_passport_issued_by(update.message.text)
    await update.message.reply_text("Дякую.")
    # await update.message.reply_text("Наразі мені відомі такі данні про вас:")
    # await update.message.reply_text(context.user_data['customer'].print_info(), parse_mode='html')
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
    # await update.message.reply_text("Наразі мені відомі такі данні про вас:")
    # await update.message.reply_text(context.user_data['customer'].print_info(), parse_mode='html')
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

    context.user_data['customer'].set_registration_address(update.message.text)
    await update.message.reply_text("Дякую.")
    # await update.message.reply_text("Наразі мені відомі такі данні про вас:")
    # await update.message.reply_text(context.user_data['customer'].print_info(), parse_mode='html')
    await update.message.reply_text("Тепер введіть, будь ласка, ідентифікаційний код:")
    return TAX_ID


async def tax_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """
    Handles the user's tax identification code input and sets it in the Customer object.

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
    # await update.message.reply_text("Тепер перевірьте, будь ласка, чи всі дані введено вірно:")

    return CHECK


async def check(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation and asks the user about their gender."""
    reply_keyboard = [["Вірно", "Невірно"]]

    await update.message.reply_text(
        "Тепер перевірьте, будь ласка, чи всі дані введено вірно",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Вірно чи невірно?"
        ),
    )

    return THANK

async def thanks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the selected gender and asks for a photo."""
    user = update.message.from_user
    logger.info("Gender of %s: %s", user.first_name, update.message.text)
    await update.message.reply_text(
        "I see! Please send me a photo of yourself, "
        "so I know what you look like, or send /skip if you don't want to.",
        reply_markup=ReplyKeyboardRemove(),
    )
    await update.message.reply_text("Дякую.")

    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        "Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END
