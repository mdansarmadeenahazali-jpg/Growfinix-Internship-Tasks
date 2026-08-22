import re

with open("enquiries.txt", "r", encoding="utf-8") as f:
    data = f.read()

emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', data)
names = re.findall(r'[A-Z][a-z]+ [A-Z][a-z]+', data)

places = ["Goa","Manali","Kashmir","Ooty","Jaipur",
          "Darjeeling","Kerala","Shimla","Andaman"]

print("===== CLEAN TOUR ENQUIRIES =====")

for i in range(len(emails)):
    place = "Unknown"
    for p in places:
        if p in data.split("\n\n")[i]:
            place = p
            break

    print("\nRecord", i+1)
    print("Name :", names[i])
    print("Email:", emails[i])
    print("Place:", place)