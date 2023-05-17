import re
from datetime import date
from datetime import datetime



class Customer:
    __user_name: str = None
    __firstname: str = None
    __lastname: str = None
    __phone_number: str = None
    __passport_series: str = None
    __passport_number: str = None
    __passport_issued_by: str = None
    __passport_issued_date: date = None
    __registration_address: str = None
    __id_code: str = None

    def __init__(self):
        pass

    def set_username(self, username: str) -> None:
        """
        Sets the username.

        :param username: The username.
        :type username: str
        """
        self.__user_name = username

    def set_firstname(self, firstname: str) -> None:
        """
        Sets the first name.

        :param firstname: The first name.
        :type firstname: str
        :raises ValueError: If the first name has an invalid length or contains invalid characters.
        """
        if len(firstname) < 2 or len(firstname) > 30:
            raise ValueError('Ім\'я має містити від 2 до 30 символів')

        ukrainian_pattern = re.compile(r"^[а-щА-ЩЬьЮюЯяЇїІіЄєҐґ']+?$")
        if not ukrainian_pattern.match(firstname):
            raise ValueError('Ім\'я має містити лише символи українського алфавіту та апостроф.')

        self.__firstname = firstname.capitalize()

    def set_lastname(self, lastname: str) -> None:
        """
        Sets the last name.

        :param lastname: The last name.
        :type lastname: str
        :raises ValueError: If the last name has an invalid length or contains invalid characters.
        """
        if len(lastname) < 2 or len(lastname) > 40:
            raise ValueError('Прізвище має містити від 2 до 40 символів')

        ukrainian_pattern = re.compile(r"^[а-щА-ЩЬьЮюЯяЇїІіЄєҐґ'-]+?$")
        if not ukrainian_pattern.match(lastname):
            raise ValueError('Прізвище має містити лише символи українського алфавіту та апостроф.')

        self.__lastname = lastname.capitalize()

    def set_phone_number(self, phone_number: str) -> None:
        """
        Sets the phone number.

        :param phone_number: The phone number.
        :type phone_number: str
        :raises ValueError: If the phone number has an invalid length or contains non-digit characters.
        """
        if len(phone_number) != 10 or not phone_number.isdigit():
            raise ValueError('Номер телефону повинен містити рівно 10 цифр.')

        self.__phone_number = phone_number

    def set_passport_series(self, passport_series: str) -> None:
        """
        Sets the passport series.

        :param passport_series: The passport series.
        :type passport_series: str
        :raises ValueError: If the passport series has an invalid length or contains non-alphabetic characters.
        """
        if len(passport_series) != 2 or not passport_series.isalpha():
            raise ValueError('Серія паспорту повинна містити рівно 2 літери.')

        self.__passport_series = passport_series.upper()

    def set_passport_number(self, passport_number: str) -> None:
        """
        Sets the passport number.

        :param passport_number: The passport number.
        :type passport_number: str
        :raises ValueError: If the passport number has an invalid length or contains non-digit characters.
        """
        if len(passport_number) != 6 or not passport_number.isdigit():
            raise ValueError('Номер паспорту повинен містити рівно 6 цифр.')

        self.__passport_number = passport_number

    def set_passport_issued_by(self, passport_issued_by: str) -> None:
        """
        Sets the entity that issued the passport.

        :param passport_issued_by: The entity that issued the passport.
        :type passport_issued_by: str
        :raises ValueError: If the passport issued by contains non-Ukrainian alphabet characters, apostrophe, space, or punctuation marks.
        """

        ukrainian_pattern = re.compile(r"^[а-щА-ЩЬьЮюЯяЇїІіЄєҐґ\s'-.,]+?$")
        if not ukrainian_pattern.match(passport_issued_by):
            raise ValueError('Має містити лише символи українського алфавіту, апостроф, пробіл або розділові знаки.')

        self.__passport_issued_by = passport_issued_by

    def set_passport_issued_date(self, passport_issued_date: str) -> None:
        """
        Sets the date when the passport was issued.

        :param passport_issued_date: The passport issued date in the format "dd.mm.yyyy".
        :type passport_issued_date: str
        :raises ValueError: If the passport issued date has an invalid format or is a future date.
        """
        try:
            passport_issued_date = datetime.strptime(passport_issued_date, '%d.%m.%Y').date()
        except ValueError:
            raise ValueError('Недійсний формат дати.')

        if not isinstance(passport_issued_date, date) or passport_issued_date > date.today():
            raise ValueError('Дата вказано невірно.')

        self.__passport_issued_date = passport_issued_date
        return None

    def set_registration_address(self, registration_address: str) -> None:
        """
        Sets the registration address.

        :param registration_address: The registration address.
        :type registration_address: str
        :raises ValueError: If the registration address contains non-Ukrainian alphabet characters, apostrophe, space, digits, or punctuation marks.
        """

        ukrainian_pattern = re.compile(r"^[а-щА-ЩЬьЮюЯяЇїІіЄєҐґ\s\d'.,-]+?$")
        if not ukrainian_pattern.match(registration_address):
            raise ValueError(
                'Має містити лише символи українського алфавіту, апостроф, пробіл,розділові знаки або цифри.')

        self.__registration_address = registration_address

    def set_id_code(self, id_code: str) -> None:
        """
        Sets the identification code.

        :param id_code: The identification code.
        :type id_code: str
        :raises ValueError: If the identification code has an invalid length or contains non-digit characters.
        """
        if len(id_code) != 10 or not id_code.isdigit():
            raise ValueError('Ідентифікаційний код повинен містити рівно 10 цифр.')

        self.__id_code = id_code

    def print_info(self) -> str:
        """
        Returns the customer's information.

        :return: The customer's information.
        :rtype: str
        """
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
