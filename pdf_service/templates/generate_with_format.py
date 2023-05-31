import os
from typing import List

from dotenv import load_dotenv
import pdfkit
from datetime import date

from userdata import Customer

load_dotenv()

wkhtmltopdf_path = os.getenv("WKHTMLTOPDF_PATH")
html_template_path = os.getenv("HTML_TEMPLATE_PATH_2")
output_path = os.getenv("OUTPUT_PATH_2")

config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)


def parsing_data(value: date) -> List[str]:
    """
    Parses the date value into a list of strings representing day, month, and year.

    Parameters:
    - value: The date value to be parsed.

    Returns:
    - List[str]: The list of strings representing day, month, and year.
    """
    months = {
        "1": "січня",
        "2": "лютого",
        "3": "березня",
        "4": "квітня",
        "5": "травня",
        "6": "червня",
        "7": "липня",
        "8": "серпня",
        "9": "вересня",
        "10": "жовтня",
        "11": "листопада",
        "12": "грудня"
    }
    value = [str(value.day), months[str(value.month)], str(value.year)]
    return value


def generate_pdf_with_format(customer: Customer, contract_number: int = 100,
                             html_template_path: str = html_template_path,
                             output_path: str = output_path) -> str:
    """
    Generates a PDF document using the provided customer data and template.

    Parameters:
    - customer: An instance of the Customer class containing customer data.
    - contract_number: The contract number (default: 100).
    - html_template_path: The path to the HTML template file (default: value from environment variable).
    - output_path: The path to save the generated PDF file (default: value from environment variable).

    Returns:
    - str: The path of the generated PDF file.
    """
    with open(html_template_path, 'r', encoding='utf-8') as template_file:
        html_template = template_file.read()

    filled_template = html_template.format(
        cont_numb=str(contract_number),
        day_today=parsing_data(date.today()),
        lastname=customer.get_lastname(),
        firstname=customer.get_firstname(),
        middlename=customer.get_middle_name(),
        phone_number=customer.get_phone_number(),
        passport_series=customer.get_passport_series(),
        passport_number=customer.get_passport_number(),
        passport_issued_by=customer.get_passport_issued_by(),
        passport_issued_date=parsing_data(customer.get_passport_issued_date()),
        registration_address=customer.get_registration_address(),
        id_code=customer.get_id_code()
    )

    pdfkit.from_string(filled_template, output_path, configuration=config)
    return output_path
