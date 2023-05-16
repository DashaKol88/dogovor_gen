import re
from datetime import date


def validate_name_and_surname_length(value):
    if len(value) < 2 or len(value) > 30:
        return "Ім\'я або прізвище має містити від 2 до 30 символів"


def validate_name_and_surname_characters(value):
    ukrainian_pattern = re.compile(r"^[а-щА-ЩЬьЮюЯяЇїІіЄєҐґ']+?$")
    if not ukrainian_pattern.match(value):
        return 'Ім\'я або прізвище має містити лише символи українського алфавіту та апостроф.'


def validate_phone_number(value):
    if len(value) != 10 or not value.isdigit():
        return 'Номер телефону повинен містити рівно 10 цифр.'


def validate_passport_series(value):
    if len(value) != 2:
        return 'Серія паспорту повинна містити рівно 2 літери.'


def validate_passport_number(value):
    if len(value) != 6 or not value.isdigit():
        return 'Номер паспорту повинен містити рівно 6 цифр.'


def validate_passport_issued_date(value: date):
    if value > date.today():
        return 'Невірно вказана дата видачі'


def validate_id_code(value):
    if len(value) != 10 or not value.isdigit():
        return 'Ідентифікаційний код повинен містити рівно 10 цифр.'
