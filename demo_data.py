import psycopg2
from faker import Faker

try:
    conn = psycopg2.connect("dbname='angel-dev' user='postgres' password='postgres'")
except:
    print "I am unable to connect to the database"

fake = Faker()

def create_profile
    return {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'lat': fake.latitude(),
            'lon': fake.longitude()
            }

def create_card
    return {
            'card_exp': fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y"),
            'card_prov': fake.credit_card_provider(card_type=None),
            'card num': fake.credit_card_number(card_type=None),
            'security code': fake.credit_card_security_code(card_type=None)
            }


