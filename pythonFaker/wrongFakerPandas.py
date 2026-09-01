from faker import Faker
import random
import pandas as pd

fake = Faker("en_IN")

data = []

for i in range(20):
    age = random.randint(18, 60)
    email = fake.email()
    name = fake.name()


    if random.random() < 0.2:
        age = -random.randint(1, 20)

    if random.random() < 0.2:
        email = "invalid_email"

    if random.random() < 0.2:
        name = ""

    data.append({
        "Name": name,
        "Email": email,
        "Age": age
    })

df = pd.DataFrame(data)

print(df)