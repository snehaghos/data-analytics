from faker import Faker
import pandas as pd

#indian faker datas
fake = Faker("en_IN")

students = []

for i in range(10):
    students.append({
        "ID": i + 1,
        "Name": fake.name(),
        "Email": fake.email(),
        "City": fake.city(),
        "Phone": fake.phone_number()
    })

df = pd.DataFrame(students)

print(df)