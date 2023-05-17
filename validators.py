import re
from datetime import date
from datetime import datetime
from typing import Optional


def validate_name_and_surname_length(value: str) -> Optional[str]:
    """
    Validates the length of a name or surname.

    Parameters:
    - value (str): A string representing the name or surname.

    Returns:
    - str or None: If the length of the value is less than 2 or greater than 30 characters, it returns an error message.
        Otherwise, it returns None.

    """
    if len(value) < 2 or len(value) > 30:
        return "Ім\'я або прізвище має містити від 2 до 30 символів"


def validate_name_and_surname_characters(value: str) -> Optional[str]:
    """
    Validates that a name or surname contains only Ukrainian alphabet characters and apostrophes.

    Parameters:
    - value (str): A string representing the name or surname.

    Returns:
    - str or None: If the value contains characters other than Ukrainian alphabet characters and apostrophes,
      it returns an error message. Otherwise, it returns None.

    """
    ukrainian_pattern = re.compile(r"^[а-щА-ЩЬьЮюЯяЇїІіЄєҐґ']+?$")
    if not ukrainian_pattern.match(value):
        return 'Ім\'я або прізвище має містити лише символи українського алфавіту та апостроф.'


def validate_phone_number(value: str) -> Optional[str]:
    """
    Validates that a phone number contains exactly 10 digits.

    Parameters:
    - value (str): A string representing the phone number.

    Returns:
    - str or None: If the value does not contain exactly 10 digits or contains non-digit characters,
      it returns an error message. Otherwise, it returns None.

    """
    if len(value) != 10 or not value.isdigit():
        return 'Номер телефону повинен містити рівно 10 цифр.'


def validate_passport_series(value: str) -> Optional[str]:
    """
    Validates that a passport series contains exactly 2 alphabetic characters.

    Parameters:
    - value (str): A string representing the passport series.

    Returns:
    - str or None: If the value does not contain exactly 2 alphabetic characters, it returns an error message.
      Otherwise, it returns None.

    """
    if len(value) != 2 or not value.isalpha():
        return 'Серія паспорту повинна містити рівно 2 літери.'


def validate_passport_number(value: str) -> Optional[str]:
    """
    Validates that a passport number contains exactly 6 digits.

    Parameters:
    - value (str): A string representing the passport number.

    Returns:
    - str or None: If the value does not contain exactly 6 digits or contains non-digit characters,
      it returns an error message. Otherwise, it returns None.

    """
    if len(value) != 6 or not value.isdigit():
        return 'Номер паспорту повинен містити рівно 6 цифр.'


def validate_passport_issued_date(value: str) -> Optional[str]:
    """
    Validates that a passport issued date is in the correct format and is a valid date.

    Parameters:
    - value (str): A string representing the passport issued date in the format 'dd.mm.yy'.

    Returns:
    - str or None: If the value is not in the correct format or is not a valid date, it returns an error message.
      Otherwise, it returns None.

    """
    try:
        value = datetime.strptime(value, '%d.%m.%Y').date()
    except ValueError:
        return "Недійсний формат дати."

    if not isinstance(value, date):
        return "Дата вказано невірно."

    return None


def validate_passport_issued_date_in_future(value: str) -> Optional[str]:
    """
    Validates that a passport issued date is not in the future.

    Parameters:
    - value (str): A string representing the passport issued date in the format 'dd.mm.yy'.

    Returns:
    - str or None: If the value represents a date in the future, it returns an error message.
      Otherwise, it returns None.

    """
    try:
        value = datetime.strptime(value, '%d.%m.%Y').date()
    except ValueError:
        return "Недійсний формат дати."

    if value > date.today():
        return "Невірно вказана дата видачі"

    return None


def validate_id_code(value: str) -> Optional[str]:
    """
    Validates that an ID code consists of exactly 10 digits.

    Parameters:
    - value (str): The ID code to validate.

    Returns:
    - str or None: If the ID code is not exactly 10 digits or contains non-digit characters,
      it returns an error message. Otherwise, it returns None.

    """
    if len(value) != 10 or not value.isdigit():
        return 'Ідентифікаційний код повинен містити рівно 10 цифр.'
