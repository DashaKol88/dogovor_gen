import re
from datetime import date
from datetime import datetime


class Customer:
    __user_name = None
    __firstname = None
    __lastname = None
    __phone_number = None
    __passport_series = None
    __passport_number = None
    __passport_issued_by = None
    __passport_issued_date = None
    __registration_address = None
    __id_code = None

    def __init__(self):
        pass

    def set_username(self, username):
        self.__user_name = username

    def set_firstname(self, firstname):
        if len(firstname) < 2 or len(firstname) > 30:
            raise ValueError('Ім\'я має містити від 2 до 30 символів')

        ukrainian_pattern = re.compile(r"^[а-щА-ЩЬьЮюЯяЇїІіЄєҐґ']+?$")
        if not ukrainian_pattern.match(firstname):
            raise ValueError('Ім\'я має містити лише символи українського алфавіту та апостроф.')

        self.__firstname = firstname.capitalize()

    def set_lastname(self, lastname):
        if len(lastname) < 2 or len(lastname) > 40:
            raise ValueError('Прізвище має містити від 2 до 40 символів')

        ukrainian_pattern = re.compile(r"^[а-щА-ЩЬьЮюЯяЇїІіЄєҐґ'-]+?$")
        if not ukrainian_pattern.match(lastname):
            raise ValueError('Прізвище має містити лише символи українського алфавіту та апостроф.')

        self.__lastname = lastname.capitalize()

    def set_phone_number(self, phone_number):
        if len(phone_number) != 10 or not phone_number.isdigit():
            return ValueError('Номер телефону повинен містити рівно 10 цифр.')

        self.__phone_number = phone_number

    def set_passport_series(self, passport_series):
        if len(passport_series) != 2 or not passport_series.isalpha():
            return ValueError('Серія паспорту повинна містити рівно 2 літери.')

        self.__passport_series = passport_series.upper()

    def set_passport_number(self, passport_number):
        if len(passport_number) != 6 or not passport_number.isdigit():
            return ValueError('Номер паспорту повинен містити рівно 6 цифр.')

        self.__passport_number = passport_number

    def set_passport_issued_by(self, passport_issued_by):
        self.__passport_issued_by = passport_issued_by

    def set_passport_issued_date(self, passport_issued_date):
        try:
            value = datetime.strptime(passport_issued_date, '%d.%m.%Y').date()
        except ValueError:
            raise ValueError('Недійсний формат дати.')

        if not isinstance(value, date) or value > date.today():
            raise ValueError('Дата вказано невірно.')

        self.__passport_issued_date = passport_issued_date
        return None


    def set_registration_address(self, registration_address):
        self.__registration_address = registration_address

    def set_id_code(self, id_code):
        if len(id_code) != 10 or not id_code.isdigit():
            return ValueError('Ідентифікаційний код повинен містити рівно 10 цифр.')

        self.__id_code = id_code

    def print_info(self):
        info = f"<b>nickname:</b> {self.__user_name}\n" \
               f"<b>Ім'я:</b> {self.__firstname}\n" \
               f"<b>Прізвище:</b> {self.__lastname}\n" \
               f"<b>Номер телефону:</b> {self.__phone_number}\n" \
               f"<b>Серія паспорту:</b> {self.__passport_series}\n" \
               f"<b>Номер паспорту:</b> {self.__passport_number}\n" \
               f"<b>Паспорт виданий:</b> {self.__passport_issued_by}\n" \
               f"<b>Дата видачі паспорту:</b> {self.__passport_issued_date}\n" \
               f"<b>Адреса реестрації:</b> {self.__registration_address}\n" \
               f"<b>Ідентифікаційний код:</b> {self.__id_code}\n"
        return info
