# #variables, values, need

# #should not use keywords as variables
# # import keyword
# # print(keyword.kwlist)

# age = 10
# Age = 120

# _age = 102
# _user1 = 'anil'

# print(_user1, _age)

# _class = 'divya'

# # print(age)
# # del age
# # print(age)



# anil_kumar_reddy_vempati = 'divya'

# AnilKumarReddyVempati = 'divya'



# #dataTypes(string, )

# #strings
# name = 'anil'
# gender = 'm'

# #integers
# age = 21

# #decimals
# salary = 25000.45

# #boolean
# male = False

# print(name)
# print(type(name))


# #type conversions
# #int->float
# age = 21
# age = float(age)
# print(type(age), age)

# #float->int
# age = 21.6
# age = int(age)
# print(age)

# #integers->strings
# salary = 55000
# salary = str(salary)
# print(salary)

# #strings->integers
# name = '100.9'
# print(int(float(name)))

# # print(7%4)
# # print(4%7)
# # print(9%78)
# # print(100%20)
# # print(81%456)

# # n = 4
# # print(n ** 10)

# # print(n ** 3)

# # print(n ** (0.5))

# # print(7.0 // 2)
# # print(7.0 // 2.0)



# # name = input()
# # age = int(input())
# # mail = input()
# # phn = int(input())

# # # erripuk {name} who is {age} and has a {mail} and u can book him by contacting {phn}
# # print('erripuk', name, 'who is', age, 'and has a', mail, 'and u can book him by contacting ', phn)

# # 20, 30
# # n1 = 21
# # n2 = 30

# # print(n1 <= n2)

# # #and or not
# # print(n1 > 10 or n1 % 2 == 0)

# # #not
# # print(not n1 < 20)


# # #in not in
# # print('i' in 'anil')

# # print('p' not in 'anil')


# #is -> identity(id)
# #== -> each and every

# # n1 = 10.0
# # n2 = 10.0

# # print(n1 is n2)
# # # print(n1 == n2)
# # print(id(n1), id(n2))


# # name = 'anil'
# # print('org : ',id(name))

# # name += 'kumar'
# # print('new : ', id(name))

# # lis = [1, 2, 3]
# # print(id(lis))
# # lis.append(4)
# # print(id(lis))

# # #strings
# # name = 'anil'
# # print(id(name))
# # name += 'divya'
# # print(name)
# # print(id(name))

# # name = "anil"
# # name1 = """ 
# #     once upon a time
# #       there lived a king
# #     """
# # print(name1)

# # line = 'anil is erripuk'\
# # ' mod gud'
# # print(line)

# # line2 = 'divya is anil\'s girlfrnd'
# # print(line2)


# # fruit = 'apple'

# # # 1001 | 1002 | <- | 1003 | 1004 |

# # print(id(fruit[1]), id(fruit[2]))

# # #unicode
# # print('한국어 신문')


# #slicing
# bond = 'AnilKumarDivya'
# #syntax : variable[start : end : step]
# print(bond[ -3 : -4 : -1])


# #string functions
# name = 'divya'
# print(name.capitalize())

# name = 'divya'
# print(name.upper())

# name = 'Divya'
# print(name.lower())

# name = '123d#ivya1234'
# print(name.upper())
# print(len(name))


# line = '  Hello World  '
# print(len(line))
# line2 = line.strip()
# print(line2, len(line2))

# line = '  Hello World  '
# print(len(line))
# line2 = line.lstrip()
# print(line2, len(line2))

# line = '  Hello World  '
# print(len(line))
# line2 = line.rstrip()
# print(line2, len(line2))

# line = '$$$Hello World$$$'
# print(len(line))
# line2 = line.rstrip('$dH')
# print(line2, len(line2))


# line = 'I am learn ing python'
# line1 = line.split() #['I', 'am', 'learn', 'ing', 'python']
# res = ','.join(line1) #Iamlearningpython
# print(res)

# date = '12/04/2023'
# date = date.split('/')
# print(date)

# date = '12/04/2023/'
# date = date.split('/', 2)
# print(date)


# line = 'i love python and i dont love java'
# print(line.find('i'))

# line = 'i love python and i dont love java'
# print(line.rfind('i'))

# line = 'i love python and i dont love java'
# print(line.find('loves')) #returns -1 if substr not found

# line = 'i love python and i dont love java'
# print(line.index('loves')) #throws error os substr not found




# #validations
# line = 'anillovesdivya123#$%^'
# print(line.startswith('anil')) #True
# print(line.startswith('divya')) #False
# print(line.isalpha()) #False
# print(line.isalnum()) #True (either alphabets or nums)
# print(line.isdigit()) #False
# print(line.count('i'))




#CONTROL STRUCTURES : 
#   - conditional
#   - looping
#   - unconditional


# #conditional
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))

# if (num1 > num2):
#     print(num1,'is greater than',num2 )
# else:
#     print(num2,'is greater than',num1)
    
# #o/p :- 20 is greater than 10

# str1 = "Oh! yes, this is awesome."

# if '.' in str1:
#     print("given string has .")
# if '!' in str1:
#     print("given string has !")
# if ',' in str1:
#     print("given string has ,")
# if ';' in str1:
#     print("given string has ;")

# num = 15

# if num%2 == 0:
#     print (num**2,'1st')
# else:
#     if num % 5 == 0:
#         print (num**3,'2nd')
#     else:
#         print (num*10,'3rd')

# print("The End")

# x = 257
# y = 257
# print(id(x), id(y))

# #FOR LOOP in 
# #string
# print('for loop iterates in string')
# mail = 'anilreddy'
# for i in range(0, len(mail)):
#     print(mail[i])

# #list
# print('\nfor loop iterates in list')
# mail = [1, 2, 3, 4]
# for i in range(0, len(mail)):
#     print(mail[i])

# #tuple
# print('\nfor loop iterates in tuple')
# mail = (1, 2, 3, 4)
# for i in range(0, len(mail)):
#     print(mail[i])

# #dict
# print('\nfor loop iterates in dict')
# mail = {'a' : 1, 'b' : 2, 'c' : 3}
# for i in mail:
#     print(i)

# #set
# print('\nfor loop iterates in set')
# mail = {1, 2, 3, 4}
# for i in mail:
#     print(i)

# email = 'anil9160@gmail.com'
# username = email.split('@')[0] #anil9160

# name = '' 
# for i in username:
#     if i.isdigit() == False:
#         name += i
# print(name)

# a = 10
# even_sum = 0
# for i in range(1, a+1):
#     if i % 2 != 0:
#         even_sum += i
# print(even_sum)

"""
Syntax: 
while condition:
    statements
"""
# n = 10
# i = 1
# while i <= n:
#     print(i)
#     i += 1

# n = 1
# i = 10
# while i >= n:
#     print(i)
#     i -= 1



# a = 'anil'
# temp = 10
# while temp >= 1:
#     print(temp, a)
#     temp -= 1



# n = 5
# while n <= 10:
#     print(n)
#     n += 1


# n = 10
# while n >= 5:
#     print(n)
#     n -= 1



# start = 20
# end = 30

# while start <= end:
#     print(start)
#     start += 1


# start = 49
# end = 39
# while start >= end:
#     print(start)
#     start -= 1


# name = 'anil'
# temp = 44
# while temp < 49:
#     print(name)
#     temp += 1


# name = 'anil'
# temp = 49
# while temp >= 44:
#     print(name)
#     temp -= 1

# start = 49
# end = 44
# name = 'anil'
# while start > end:
#     print(name)
#     start -= 1

# for i in range(start, end, -1):
#     print(i, name)


# i = 1
# while i <= 2:
#     name, age = input().split()[:2]
#     print('name is ',name, 'age is', age)
#     print()
#     i+=1


# name = 'anil'
# for i in range(0, len(name)):
#     print(name[i], name, i)

# start = 0
# while start < len(name):
#     print(name[start])
#     start +=1


#unconditional statements
# #break
# for i in range(1, 100):
#     if i % 5 == 0:
#         break
#     else:
#         print(i)

# #continue
# name = 'apple'
# for i in name:
#     if i == 'p':
#         continue
#     print(i)

# #adding non multiples of 5
# temp = 0
# for i in range(1, 51):
#     if i % 5 == 0:
#         continue
#     temp += i
# print(temp)


# #LIST
# nums = []
# for i in range(1, 21):
#     nums.append(i)
# #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# print(nums)

# for i in nums:
#     if i % 2 == 0:
#         nums.remove(i)
# #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# print(nums, nums[:5])

# #tuple
# nums = (1, 2, 3, 4, 5, 2, 2)
# print(nums.count(2), nums.index(2), len(nums))
# print(nums[:3])

# data = ('anil', 23)
# name = data[0]
# age = data[1]
# print(data, name, age)

# name, age = ('anil', 23, 1234)
# print([name, age])

# #SET
# nums1 = {1,2,3,4}
# nums2 = {5,6}
# nums1.add(20)
# nums1.discard(21)
# nums1.update(nums2)
# print(nums1)

# #dict
# data = {}
# data['name'] = 'anil'
# data['age'] = 23
# data['name'] = 'divya'
# data['pook'] = 'anil'
# # print(data)
# # print(list(data.keys()))
# # print(data['name']) #if name key exists
# # print(data.get('mail'))
# for i in data:
#     print('key',i)
#     print('value',data[i])
#     print()




days = {
     'Sunday' : 34,
     'Monday' : 32.5,
     'Tuesday' : 33,
     'Wednesday' : 35,
     'Thursday' : 32,
     'Friday' : 35.1,
     'Saturday' : 33.6
    }

#Xday : 40.1
days['Xday'] = 40.1 #added item
days.pop('Xday') #removed item
# print(days.get('Xday')) #do this
# print(days['Wednesday']) #dont do this
# print(list(days.items()))
# print(list(days.keys()))
# print(list(days.values()))

# data = list(days.items())
# print(data[2][1])

# for key in days:
#     print(key, days[key])

# for key, val in days.items():
#     print(val)

# data = [('anil', 23), ('divya', 21), ('nikhil',21)] #list of tuples
# # data = [['anil', 23], ['divya', 21], ['nikhil',21]] #list of lists
# data = dict(data)
# print(data)
# print(data['divya'])

# data = {'Name': 'nick', 'Phn': 90000000, 'Age': 22}
# print(data['Name'])


#FUNCTIONS
# a = 10
# b = 20
# c = a + b

# print(c)

# def add(num1, num2, num3):
#     print('addition of', num1, 'and', num2, 'is', num1 + num2)
#     print('still in function')
#     return 'end' #control goes back to it's function call with 'anil'


# print(add(10, 20, 30))


# data = [['anil', 9000000000, 23],['divya', 800000000, 21],['nikh',80000000034,5]]
# for i in data:
#     print(i[1])

# # -----------------------------------------------------------------------------
# #app using LIST as database
# hdfc_dataBase = []
# print('before running app',hdfc_dataBase)

# def welcome(name):
#     print(f'Hello {name} welcome to the hdfc bank')

# def create_acc(name, phn, age):
#     data = [name, phn, age]
#     hdfc_dataBase.append(data)
#     print(f'hey {name}, your account created successfully')

# def login(name):
#     for data in hdfc_dataBase:
#         if name == data[0]:
#             print('logged in successfully', data[0])
#             break
#     else:
#         print('invalid credentials')

# welcome('anil')
# create_acc('anil', 9000000000, 23)
# create_acc('divya', 800000000, 21)
# login('divya')

# print('after running app',hdfc_dataBase)
# #--------------------------------------------------------------------------

# #app using DICT as database

# hdfc_database = {}

# def welcome(name):
#     print(f'Hello {name} welcome to the hdfc bank')


# def create_acc(_id, raw):
#     data = {}
#     data['Name'] = raw[0]
#     data['Phn'] = raw[1]
#     data['Age'] = raw[2]

#     hdfc_database[_id] = data
#     print(f'hey {raw[0]}, your account created successfully')


# def login(name):
#     for data in hdfc_database:
#         user_dict = hdfc_database[data]
#         if name == user_dict['Name']:
#             print('logged in succesfully')
#             break
#     else:
#         print('invalid')


# welcome('anil')
# create_acc(1001, ['nick', 90000000, 22])
# create_acc(1002, ['anil', 8000000, 23])
# login('anil')
# print(hdfc_database)
# #--------------------------------------------------------------------------






# def add(num1, num2):
#     print(num1 + num2)
#     return 'end'

# print(add(2, 3))



# def show(n):
#     for i in range(1, n+1):
#         print(i)
# show(20)
# show(30)


# def extract(email):
#     user_name = email.split('@')[0]
#     return user_name
# user1 = extract('nick123@gmail.com')
# user2 = extract('anil123@gmail.com')
# print(f"user1 name is {user1} and user2 name is {user2}")

# #GLOBAL
# n = 10
# def fun1():
#     global n
#     n = 20
# def test():
#     print('before:', n)
#     fun1()
#     print('after:', n)
# test()

# #--------------------------------------------------------
# def jeep(n):
#     print('jeep start')
#     print('n value:',n)
#     print('jeep end')

# def bus(n):
#     print('bus start')
#     n = n+5
#     jeep(n)
#     print('bus end')

# def car(n):
#     print('car start')
#     n = n+5
#     bus(n)
#     print('car end')

# def main():
#     m = 20
#     n = 15
#     print('main func start')
#     car(n)
#     print('main end')
# main()
# #------------------------------------------------------------

# def swap(a, b):
#     global x
#     global y
#     x, y = b, a

# x = 10
# y = 20
# swap(x, y)
# print(x)
# print(y)


def modify(p):
    p = [1, 2, 3]

def main():
    lis = [10, 100, 30]
    modify(lis)
    print(lis)
main()