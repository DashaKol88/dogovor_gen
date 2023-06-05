import unittest
from userdata import Customer
import datetime
from datetime import date


class CustomerTestCase(unittest.TestCase):
    def setUp(self):
        """
        Set up the test case.
        """
        self.customer = Customer()

    def test_set_username(self):
        """
        Test the set_username method of Customer.
        """
        self.customer.set_username("іван_іванов")
        self.assertEqual(self.customer.get_username(), "іван_іванов")

    def test_set_lastname(self):
        """
        Test the set_lastname method of Customer.
        """
        self.customer.set_lastname("Іванов")
        self.assertEqual(self.customer.get_lastname(), "Іванов")

    def test_set_firstname(self):
        """
        Test the set_firstname method of Customer.
        """
        self.customer.set_firstname("Іван")
        self.assertEqual(self.customer.get_firstname(), "Іван")

    def test_middle_name(self):
        """
        Test the set_middle_name method of Customer.
        """
        self.customer.set_middle_name("Іванович")
        self.assertEqual(self.customer.get_middle_name(), "Іванович")

    def test_phone_number(self):
        """
        Test the set_phone_number method of Customer.
        """
        self.customer.set_phone_number("0123456789")
        self.assertEqual(self.customer.get_phone_number(), "0123456789")

    def test_passport_series(self):
        """
        Test the set_passport_series method of Customer.
        """
        self.customer.set_passport_series("АМ")
        self.assertEqual(self.customer.get_passport_series(), "АМ")

    def test_passport_number(self):
        """
        Test the set_passport_number method of Customer.
        """
        self.customer.set_passport_number("123456")
        self.assertEqual(self.customer.get_passport_number(), "123456")

    def test_passport_issued_by(self):
        """
        Test the set_passport_issued_by method of Customer.
        """
        self.customer.set_passport_issued_by("Радянським УДМС України в Черкаській області")
        self.assertEqual(self.customer.get_passport_issued_by(), "Радянським УДМС України в Черкаській області")

    def test_passport_issued_date(self):
        """
        Test the set_passport_issued_date method of Customer.
        """
        self.customer.set_passport_issued_date("20.05.2000")
        self.assertEqual(self.customer.get_passport_issued_date(), datetime.date(2000, 5, 20))

    def test_registration_address(self):
        """
        Test the set_registration_address method of Customer.
        """
        self.customer.set_registration_address("м. Київ, вул. Дегтярівська буд. 38 кв. 101")
        self.assertEqual(self.customer.get_registration_address(), "м. Київ, вул. Дегтярівська буд. 38 кв. 101")

    def test_id_code(self):
        """
        Test the set_id_code method of Customer.
        """
        self.customer.set_id_code("9876543210")
        self.assertEqual(self.customer.get_id_code(), "9876543210")

    def test_set_lastname_invalid_length(self):
        """
        Test the set_lastname method of Customer with invalid length.
        """
        with self.assertRaises(ValueError):
            self.customer.set_lastname("A")
        with self.assertRaises(ValueError):
            self.customer.set_lastname("А" * 41)

    def test_set_lastname_invalid_characters(self):
        """
        Test the set_lastname method of Customer with invalid characters.
        """
        with self.assertRaises(ValueError):
            self.customer.set_lastname("Іванов123")
        with self.assertRaises(ValueError):
            self.customer.set_lastname("Іванов!")

    def test_set_firstname_invalid_length(self):
        """
        Test the set_firstname method of Customer with invalid length.
        """
        with self.assertRaises(ValueError):
            self.customer.set_firstname("Б")
        with self.assertRaises(ValueError):
            self.customer.set_firstname("Б" * 31)

    def test_set_firstname_invalid_characters(self):
        """
        Test the set_firstname method of Customer with invalid characters.
        """
        with self.assertRaises(ValueError):
            self.customer.set_firstname("Іван123")
        with self.assertRaises(ValueError):
            self.customer.set_firstname("Іван!")

    def test_set_middle_name_invalid_length(self):
        """
        Test the set_middle_name method of Customer with invalid length.
        """
        with self.assertRaises(ValueError):
            self.customer.set_middle_name("В")
        with self.assertRaises(ValueError):
            self.customer.set_middle_name("В" * 31)

    def test_set_middle_name_invalid_characters(self):
        """
        Test the set_middle_name method of Customer with invalid characters.
        """
        with self.assertRaises(ValueError):
            self.customer.set_middle_name("Іванович123")
        with self.assertRaises(ValueError):
            self.customer.set_middle_name("Іванович!")

    def test_set_phone_number_invalid_length(self):
        """
        Test the set_phone_number method of Customer with invalid length.
        """
        with self.assertRaises(ValueError):
            self.customer.set_phone_number("12345")

    def test_set_phone_number_non_digit_chars(self):
        """
        Test the set_phone_number method of Customer with non-digit characters.
        """
        with self.assertRaises(ValueError):
            self.customer.set_phone_number("1234abc678")

    def test_set_passport_series_invalid_length(self):
        """
        Test the set_passport_series method of Customer with invalid length.
        """
        with self.assertRaises(ValueError):
            self.customer.set_passport_series("А")

        with self.assertRaises(ValueError):
            self.customer.set_passport_series("АБВ")

    def test_set_passport_series_invalid_characters(self):
        """
        Test the set_passport_series method of Customer with invalid characters.
        """
        with self.assertRaises(ValueError):
            self.customer.set_passport_series("А1")

        with self.assertRaises(ValueError):
            self.customer.set_passport_series("АБ!")

    def test_set_passport_number_invalid_length(self):
        """
        Test the set_passport_number method of Customer with invalid length.
        """
        with self.assertRaises(ValueError):
            self.customer.set_passport_number("12345")

        with self.assertRaises(ValueError):
            self.customer.set_passport_number("1234567")

    def test_set_passport_number_invalid_characters(self):
        """
        Test the set_passport_number method of Customer with invalid characters.
        """
        with self.assertRaises(ValueError):
            self.customer.set_passport_number("1234А6")

        with self.assertRaises(ValueError):
            self.customer.set_passport_number("123!56")

    def test_set_passport_issued_by_invalid_characters(self):
        """
        Test the set_passport_issued_by method of Customer with invalid characters.
        """
        with self.assertRaises(ValueError):
            self.customer.set_passport_issued_by("123")

        with self.assertRaises(ValueError):
            self.customer.set_passport_issued_by("Passport Issued By")

    def test_set_passport_issued_date_invalid_format(self):
        """
        Test the set_passport_issued_date method of Customer with invalid format.
        """
        with self.assertRaises(ValueError):
            self.customer.set_passport_issued_date("05/20/2000")

        with self.assertRaises(ValueError):
            self.customer.set_passport_issued_date("2000-05-20")

    def test_set_passport_issued_date_future_date(self):
        """
        Test the set_passport_issued_date method of Customer with a future date.
        """
        today = date.today()
        future_date = today.replace(year=today.year + 1)
        future_date_str = future_date.strftime("%d.%m.%Y")
        with self.assertRaises(ValueError):
            self.customer.set_passport_issued_date(future_date_str)

    def test_set_passport_issued_date_invalid_date(self):
        """
        Test the set_passport_issued_date method of Customer with an invalid date.
        """
        with self.assertRaises(ValueError):
            self.customer.set_passport_issued_date("32.05.2000")

        with self.assertRaises(ValueError):
            self.customer.set_passport_issued_date("20.13.2000")

    def test_set_registration_address_invalid_characters(self):
        """
        Test the set_registration_address method of Customer with invalid characters.
        """
        with self.assertRaises(ValueError):
            self.customer.set_registration_address("Address123")

    def test_set_id_code_invalid_length(self):
        """
        Test the set_id_code method of Customer with invalid length.
        """
        with self.assertRaises(ValueError):
            self.customer.set_id_code("12345678")

        with self.assertRaises(ValueError):
            self.customer.set_id_code("12345678901")

    def test_set_id_code_invalid_characters(self):
        """
        Test the set_id_code method of Customer with invalid characters.
        """
        with self.assertRaises(ValueError):
            self.customer.set_id_code("1234А67890")

        with self.assertRaises(ValueError):
            self.customer.set_id_code("12#4567890")


if __name__ == '__main__':
    unittest.main()
