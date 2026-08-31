from faker import Faker
import random
import pandas as pd

fake = Faker("en_IN")

students = []

for i in range(20):
    students.append({
        "Name": fake.name(),
        "Email": fake.email(),
        "Age": random.randint(18, 25),
        "Phone": fake.phone_number(),
        "City": fake.city()
    })

df = pd.DataFrame(students)


df.loc[2, "Name"] = None
df.loc[5, "Email"] = "wrong-email"
df.loc[7, "Age"] = -5
df.loc[9, "Phone"] = "123"
df.loc[11, "City"] = None

print(df)