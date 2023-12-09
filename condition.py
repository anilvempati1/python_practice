gender = input("enter the gender::").lower()
age = int(input("enter the age::"))
if gender == "male":
    if age >= 21:
        print("man")
    else:
        print("boy")
if gender == "female":
    if age >= 18:
        print("women")
    else:
        print("girl")


