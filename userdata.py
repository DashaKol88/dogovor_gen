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

    def get_username(self) -> str:
        """
        Returns the username.

        :return: The username.
        :rtype: str
        """
        return self.__user_name

    def set_lastname(self, lastname: str) -> None:
        """
        Sets the last name.

        :param lastname: The last name.
        :type lastname: str
        """
        if lastname == "_":
            self.__lastname = ""
        else:
            self.__lastname = lastname.capitalize()

    def get_lastname(self) -> str:
        """
        Returns the last name.

        :return: The last name.
        :rtype: str
        """
        return self.__lastname

    def set_firstname(self, firstname: str) -> None:
        """
        Sets the first name.

        :param firstname: The first name.
        :type firstname: str
        """
        if firstname == "_":
            self.__firstname = ""
        else:
            self.__firstname = firstname.capitalize()

    def get_firstname(self) -> str:
        """
        Returns the first name.

        :return: The first name.
        :rtype: str
        """
        return self.__firstname

    def set_middle_name(self, middle_name: str) -> None:
        """
        Sets the middle name.

        :param middle_name: The middle name.
        :type middle_name: str
        """
        if middle_name == "_":
            self.__middle_name = ""
        else:
            self.__middle_name = middle_name.capitalize()

    def get_middle_name(self) -> str:
        """
        Returns the middle name.

        :return: The middle name.
        :rtype: str
        """
        return self.__middle_name

    def set_phone_number(self, phone_number: str) -> None:
        """
        Sets the phone number.

        :param phone_number: The phone number.
        :type phone_number: str
        """
        if phone_number == "_":
            self.__phone_number = ""
        else:
            self.__phone_number = phone_number

    def get_phone_number(self) -> str:
        """
        Returns the phone number.

        :return: The phone number.
        :rtype: str
        """
        return self.__phone_number

    def set_passport_series(self, passport_series: str) -> None:
        """
        Sets the passport series.

        :param passport_series: The passport series.
        :type passport_series: str
        """
        if passport_series == "_":
            self.__passport_series = ""
        else:
            self.__passport_series = passport_series.upper()

    def get_passport_series(self) -> str:
        """
        Returns the passport series.

        :return: The passport series.
        :rtype: str
        """
        return self.__passport_series

    def set_passport_number(self, passport_number: str) -> None:
        """
        Sets the passport number.

        :param passport_number: The passport number.
        :type passport_number: str
        """
        if passport_number == "_":
            self.__passport_number = ""
        else:
            self.__passport_number = passport_number

    def get_passport_number(self) -> str:
        """
        Returns the passport number.

        :return: The passport number.
        :rtype: str
        """
        return self.__passport_number

    def set_passport_issued_by(self, passport_issued_by: str) -> None:
        """
        Sets the entity that issued the passport.

        :param passport_issued_by: The entity that issued the passport.
        :type passport_issued_by: str
        """
        if passport_issued_by == "_":
            self.__passport_issued_by = ""
        else:
            self.__passport_issued_by = passport_issued_by

    def get_passport_issued_by(self) -> str:
        """
        Returns the entity that issued the passport.

        :return: The entity that issued the passport.
        :rtype: str
        """
        return self.__passport_issued_by

    def set_passport_issued_date(self, passport_issued_date: str) -> None:
        """
        Sets the date when the passport was issued.

        :param passport_issued_date: The passport issued date in the format "dd.mm.yyyy".
        :type passport_issued_date: str
        """
        if passport_issued_date == "_":
            self.__passport_issued_date = ""
        else:
            try:
                passport_issued_date = datetime.strptime(passport_issued_date, '%d.%m.%Y').date()
            except ValueError:
                raise ValueError('Недійсний формат дати.')
            self.__passport_issued_date = passport_issued_date

    def get_passport_issued_date(self) -> date:
        """
        Returns the date when the passport was issued.

        :return: The passport issued date.
        :rtype: date
        """
        return self.__passport_issued_date

    def set_registration_address(self, registration_address: str) -> None:
        """
        Sets the registration address.

        :param registration_address: The registration address.
        :type registration_address: str
        """
        if registration_address == "_":
            self.__registration_address = ""
        else:
            self.__registration_address = registration_address

    def get_registration_address(self) -> str:
        """
        Returns the registration address.

        :return: The registration address.
        :rtype: str
        """
        return self.__registration_address

    def set_id_code(self, id_code: str) -> None:
        """
        Sets the identification code.

        :param id_code: The identification code.
        :type id_code: str
        """
        if id_code == "_":
            self.__id_code = ""
        else:
            self.__id_code = id_code

    def get_id_code(self) -> str:
        """
        Returns the identification code.

        :return: The identification code.
        :rtype: str
        """
        return self.__id_code

    def print_info(self) -> str:
        """
        Returns the customer's information.

        :return: The customer's information.
        :rtype: str
        """
        info = f"<b>nickname:</b> {self.__user_name}\n" \
               f"<b>Прізвище:</b> {self.__lastname}\n" \
               f"<b>Ім'я:</b> {self.__firstname}\n" \
               f"<b>По батькові:</b> {self.__middle_name}\n" \
               f"<b>Номер телефону:</b> {self.__phone_number}\n" \
               f"<b>Серія паспорту:</b> {self.__passport_series}\n" \
               f"<b>Номер паспорту:</b> {self.__passport_number}\n" \
               f"<b>Паспорт виданий:</b> {self.__passport_issued_by}\n" \
               f"<b>Дата видачі паспорту:</b> {self.__passport_issued_date}\n" \
               f"<b>Адреса реестрації:</b> {self.__registration_address}\n" \
               f"<b>Ідентифікаційний код:</b> {self.__id_code}\n"
        return info
