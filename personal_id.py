# program says what is your birthday by knowing first part of your id number
# program works only if u live in 2022 and u r less than 199 years old 

# inputs and variables
id = int(input("Input first part of your personal ID number= "))
hundredCheck = input("Are u 100 years old or older than 100 years? Type y or n - ")
date = int(id*0.0001) #date
month = int((id-(date*10000))*0.01)
year = id-(date*10000)-month*100

# checking if u damn old and problem with centuries
if hundredCheck == "y":
    if year >22:
        year += 1800
    else:
        year += 1900 
else:
    if year >22:
        year += 1900
    else:
        year += 2000 


# month names 
if month == 1:
    month = "January"
if month == 2:
    month = "February"
if month == 3:
    month = "March"
if month == 4:
    month = "April"
if month == 5:
    month = "May"
if month == 6:
    month = "June"
if month == 7:
    month = "July"
if month == 8:
    month = "August"
if month == 9:
    month = "September"
if month == 10:
    month = "October"
if month == 11:
    month = "November"
if month == 12:
    month = "December"

print("Your Birthday is", date, month, year)
