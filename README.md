# PDF Agreement Telegram Bot

Telegram bot to generate an agreement in PDF format

## Installation

1. Clone a project to work directory
    ```bash
    git clone https://github.com/DashaKol88/dogovor_gen.git
    ```
2. Create virtual env
   ```bash
    python -m venv ./venv
   ```
3. Activate the virtual env
   ```bash
   source ./venv/bin/activate
   ```
4. Install required dependencies
   ```bash
   pip install -r requirements.txt
   ```
5. Install wkhtmltopdf (Debian/Ubuntu)
   ```bash
   sudo apt-get install wkhtmltopdf
   ```
6. Create and fill a .env file
7. Run the bot
   ```bash
   python ./bot.py
   ```

## Docker

To be implemented