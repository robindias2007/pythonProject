import phonenumbers

number = input("Please Enter the phone number to check the location and Provider Details along with country code? \n")

from phonenumbers import geocoder
ch_number = phonenumbers.parse(number, "CH")
print("This phone number is based in " + geocoder.description_for_number(ch_number, "en"))

from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print("The service provider of this phone number is " + carrier.name_for_number(service_number, "en"))

