from userdata import *
from datetime import date
from jinja2 import Environment, FileSystemLoader

# user data example
CON_NUMBER = 100
customer = Customer()
try:
    customer.set_username("sad_user")
    customer.set_lastname("Іванов")
    customer.set_firstname("Павло")
    customer.set_middle_name("Іванович")
    customer.set_phone_number("1234567890")
    customer.set_passport_series("АВ")
    customer.set_passport_number("123456")
    customer.set_passport_issued_by("Бориспільським МВ ГУ МВС України в Київській області")
    customer.set_passport_issued_date("01.01.2022")
    customer.set_registration_address("м. Київ, вул. Січових стрільців, буд. 40, кв. 152")
    customer.set_id_code("1234567890")

    print(customer.print_info())

except ValueError as e:
    print(f"Виникла помилка: {str(e)}")


def parsing_data(value):
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


html_template_path = "dogovor_for_jinja.html"
output_path = "completed_contract.html"


def generate_html_doc(customer: Customer, html_template_path: str, output_path: str,
                      con_number: int = CON_NUMBER) -> None:
    global CON_NUMBER

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(html_template_path)

    filled_template = template.render(
        cont_numb=str(con_number),
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

    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(filled_template)

    CON_NUMBER += 1


generate_html_doc(customer, html_template_path, output_path)
print(CON_NUMBER)
