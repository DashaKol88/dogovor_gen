import os

from dotenv import load_dotenv
from handlers import *
from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 5):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    load_dotenv()
    application = Application.builder().token(os.environ['BOT_TOKEN']).build()

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            FIRST_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, firstname)],
            LAST_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, lastname)],
            PHONE_NUM: [MessageHandler(filters.TEXT & ~filters.COMMAND, phonenum)],
            P_SER: [MessageHandler(filters.TEXT & ~filters.COMMAND, pas_ser)],
            P_NUM: [MessageHandler(filters.TEXT & ~filters.COMMAND, pas_num)],
            P_ISS_B: [MessageHandler(filters.TEXT & ~filters.COMMAND, pas_iss_by)],
            P_ISS_D: [MessageHandler(filters.TEXT & ~filters.COMMAND, pas_iss_date)],
            REG_ADDR: [MessageHandler(filters.TEXT & ~filters.COMMAND, reg_address)],
            TAX_ID: [MessageHandler(filters.TEXT & ~filters.COMMAND, tax_id)],
            CHECK: [MessageHandler(filters.Regex("^(Вірно|Невірно)$"), check)],
            # PHOTO: [MessageHandler(filters.PHOTO, photo), CommandHandler("skip", skip_photo)],
            # LOCATION: [
            #     MessageHandler(filters.LOCATION, location),
            #     CommandHandler("skip", skip_location),
            # ],
            # BIO: [MessageHandler(filters.TEXT & ~filters.COMMAND, bio)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
