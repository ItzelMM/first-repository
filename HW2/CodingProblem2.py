# Itzel Munoz Monroy PSID: 1888446
import datetime

dates_f = open("inputDates.txt", "r")
right_dates = open("parsedDates.txt", "w")
dates = []
months_num = {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6, "july": 7,
              "august": 8, "september": 9, "october": 10, "november": 11, "december": 12}
months = months_num.keys()

for response in dates_f:
    if (len(response.split()) != 3 or response.find(",") == -1) and response.find("-1") == -1:
        continue
    elif response != "-1":
        dates.append(response)

for date in dates:
    date_l = date.lower()
    date_e = date_l.replace(",", "")
    mdy = date_e.split()
    if mdy[0] in months and mdy[1].isnumeric() and mdy[2].isnumeric():
        mdy[0] = months_num[mdy[0]]
        if datetime.date(int(mdy[2]), int(mdy[0]), int(mdy[1])) <= datetime.date.today():
            print(str(mdy[0]) + "/" + mdy[1] + "/" + mdy[2])
            right_dates.write(str(mdy[0]) + "/" + mdy[1] + "/" + mdy[2] + '\n')

dates_f.close()
right_dates.close()
