from faker import Faker
import phonenumbers
from phonenumbers import geocoder, PhoneNumberFormat
import random
import string

# Create a Faker instance
faker = Faker()

# Function to generate a British phone number and fake address
def generate_user_data():
    while True:
        # Generate a random phone number (without formatting)
        phone_number = faker.phone_number()

        # Parse the phone number to check if it's British
        parsed_number = phonenumbers.parse(phone_number, "GB")

        if geocoder.country_name_for_number(parsed_number, "en") == "United Kingdom":
            address = faker.address().replace("\n", ", ")
            return phone_number, address

# Function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Function to generate a fake web footprint
def generate_web_footprint():
    browsers = ["Chrome", "Firefox", "Safari", "Edge", "Opera"]
    browser_version = faker.random_int(min=70, max=90)
    operating_system = faker.random_element(["Windows 10", "Windows 8", "Mac OS X", "Linux"])
    return f"{random.choice(browsers)} {browser_version}.{faker.random_int(min=0, max=99)} {operating_system}"

# Ask the user for the number of users to generate
num_users = int(input("Enter the number of users to generate: "))

# Generate user data, passwords, and web footprints
user_data = []
for _ in range(num_users):
    phone_number, address = generate_user_data()
    password = generate_password()
    web_footprint = generate_web_footprint()
    user_data.append((phone_number, address, password, web_footprint))

# Print the generated user data
for i, data in enumerate(user_data, start=1):
    phone_number, address, password, web_footprint = data
    print(f"User {i}:")
    print("Phone Number:", phone_number)
    print("Address:", address)
    print("Password:", password)
    print("Web Footprint:", web_footprint)
    print()
