import phonenumbers
from test import number

from phonenumbers import geocoder,carrier

ch_number= phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_number,"en"))

service_provider= phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_provider,"en"))
