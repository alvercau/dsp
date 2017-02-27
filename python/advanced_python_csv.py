import pandas as pd

with open("faculty.csv") as f:
    data = pd.read_csv(f)
    data = data.rename(columns=lambda x: x.strip())
    emails = data['email'].str.strip()
    emails.to_csv('emails.csv')
