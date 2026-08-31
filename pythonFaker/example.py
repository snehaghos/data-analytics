from faker import Faker

fake = Faker()

print(fake.name())
print(fake.email())
print(fake.address())
print(fake.phone_number())



#fake 10 students

for i in range(10):
    print(f"Student {i+1}:")
    print(f"Name: {fake.name()}")
    print(f"Email: {fake.email()}")
    print(f"Address: {fake.address()}")
    print(f"Phone Number: {fake.phone_number()}")
    print("-----------------------------")\
        
        
        



#some Fker methods
# fake.name()
# fake.first_name()
# fake.last_name()
# fake.email()
# fake.phone_number()
# fake.address()
# fake.city()
# fake.state()
# fake.country()
# fake.pincode()
# fake.date_of_birth()
# fake.company()
# fake.job()
# fake.text()
# fake.random_int()