#even or odd number program
# number = int(input("entre the number::"))
# if number % 2 == 0:
#     print("even number")
# else:
#     print("odd number")

#find text in a string
# string = input("enter the string::")
# text = input("enter the text::")
# if text in string:
#     print("true")
# else:
#     print("false")

# check for vowels
# word = input("enter the word::")
# vowels = "aeiou"
# for i in word:
#     if i in vowels:
#         print("vowels found ")
#     else:
#         print("no vowels found in the word")

#vowel or consenent
# word = input("enter the alphabet::")
# vowels = "aeiou"
# for i in word:
#     if i in vowels:
#         print("it is a vowels")
#     else:
#         print("consonent")


#find yougest in the 3 people

# boy_1,boy_2,boy_3 = int(input("age_1::")),int(input("age_2::")),int(input("age_3::"))
# if boy_1 < boy_2 and boy_1 < boy_3:
#     print("boy 1 is youger")
# elif boy_2 < boy_1 and boy_2 < boy_3:
#     print("boy 2 is youger")
# else:
#     print("boy 3 is youger")


# number = int(input("enter the number less than 999999::"))
# temp = 0
# camp = 1
# number = str(number)
# if len(number) <= 6:
#     for i in number:
#         if int(i) % 2 == 0:
#             temp = int(i)+temp
#         if int(i) % 2 != 0:
#             camp = int(i)*camp
# print(temp)
# print(camp)

#leap year program

# year = int(input("enter the year::"))
# if year % 400 == 0 and year % 100 == 0:
#     print (year,"is a leap year")
# elif year % 4 == 0 and year % 100 == 0:
#     print(year,"is a leap year")
# else:
#     print(year,"is not a leap year")

#write a program is divisible by 7 and multiple of 5

# start = 1500
# end = 2700
# for i in range(start,end):
#     if (i % 7 == 0) and (i % 5 == 0):
#         print(i)

#store discount program
# no_of_items = int(input("enter the no of items required::"))
# cost = 12
# if no_of_items < 10:
#     cost = no_of_items * cost
#     print("your total payable amount is = ",cost)
# elif no_of_items > 10 and no_of_items < 100:
#     cost = no_of_items * (cost - 2)
#     print("your total payable amount is = ",cost)
# elif no_of_items >= 100:
#     cost = no_of_items * (cost -5)
#     print("your total payable amount is = ",cost)

# employee salary hike  by 5 % hike 
# salary = int(input("enter the your present salary:: "))
# year_of_joining = int(input("enter the year of joining::"))
# if (2023 - year_of_joining) >= 5:
#     bonus = (5/100) * salary
#     print("your bonus for five year in our experience is ",bonus)
# else:
#     print("your are not eligible for bonus")

# 10% discount program
# quantity = int(input("enter the required quantity::"))
# cost = 100
# price = cost * quantity
# if quantity > 10:
#     price = price -((10 / 100) * price)

#     print("total payable after the 10% discount is ",price)
# else:
#     print("total payable amount is ",price)

#student attendance program

# attended = int(input("enter the number days attended to class::"))
# medical = input("if you have midical cause put Y else put N::")
# total = 300
# actual_peercent = (attended/total)*100
# if actual_peercent >= 75 and medical == "N":
#     print("you are allowed to sit in the exam")
# elif actual_peercent < 75 and medical == "Y":
#      print("you are allowed to sit in the exam")
# elif actual_peercent >= 75 and medical == "Y":
#       print("you are allowed to sit in the exam")
# else:
#       print("you are not allowed to sit in the exam")

#asking user to print how many times his name should be print
# name = input("enter the name ::")
# times = int(input("enter how many it should be prtinted::"))
# for i in range(0,times+1):
#     print(name)

#funny pattern
# name = input("enter the name::")
# for i in name:
#     print(i)
    
#capitalize the second letter and beside
# word = input() 

#     word = word.capitalize
#     print(word)

#intergers and their squares 
# n = 20
# for i in range(1,n):
#     print(i,"-----",i**2)

#count of spaces
# text = input()
# temp = 0
# for i in text:
#     if text.find(" "):
#         temp += 1
# print(temp)

#printing numbers from 8 to 89 with 3 difference
# temp = 8
# for i in range(8,92,3):
#     print(i)

    

    