import csv

user_filepath = "./user.csv"

with open(user_filepath, encoding="UTF-8", mode="r") as user_file:
    users = csv.DictReader(user_file)
    for user in users:
        print(user)
        print(user["username"])
