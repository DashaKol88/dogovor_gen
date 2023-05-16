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
        self.__firstname = firstname

    def set_lastname(self, lastname):
        self.__lastname = lastname

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_passport_series(self, passport_series):
        self.__passport_series = passport_series

    def set_passport_number(self, passport_number):
        self.__passport_number = passport_number

    def set_passport_issued_by(self, passport_issued_by):
        self.__passport_issued_by = passport_issued_by

    def set_passport_issued_date(self, passport_issued_date):
        self.__passport_issued_date = passport_issued_date

    def set_registration_address(self, registration_address):
        self.__registration_address = registration_address

    def set_id_code(self, id_code):
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
