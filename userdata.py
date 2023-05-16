class Customer:
    __user_name = None
    __firstname = None
    __lastname = None

    def __init__(self):
        pass

    def set_username(self, username):
        self.__user_name = username

    def set_firstname(self, firstname):
        self.__firstname = firstname

    def set_lastname(self, lasttname):
        self.__lastname = self.validate_lastname(lasttname)

    def print_info(self):
        info = f"<b>nickname:</b> {self.__user_name}\n" \
               f"<b>Ім'я:</b> {self.__firstname}\n" \
               f"<b>Прізвище:</b> {self.__lastname}\n"

        return info