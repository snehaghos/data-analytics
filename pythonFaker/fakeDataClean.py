from faker import Faker
import pandas as pd

fake = Faker()

data = []

for i in range(20):
    data.append({
        "Name": fake.name(),
        "Email": fake.email(),
        "Phone": fake.phone_number(),
        "City": fake.city(),
        "Address": fake.address()
    })


df = pd.DataFrame(data)

print("Original Fake Data:")
print(df)

df.drop_duplicates(inplace=True)

for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].str.strip()

df["Email"] = df["Email"].str.lower()


df.fillna("Unknown", inplace=True)



print("\nCleaned Fake Data:")
print(df)


df.to_csv("cleaned_fake_data.csv", index=False)

print("\nCleaned data saved successfully!")