# digit=input("Enter three digit number"+"  ")
# print("Your three digit number is "+" "+digit)
# First_number= (digit[0])
# Second_number= (digit[1])
# Third_number= (digit[2])
# Result= int(First_number) + int(Second_number) + int(Third_number)
# print(f"Sum of your three digit number is  {Result}")


# weight=input("enter your weight in kg: ")
# height=input("enter your height in m:  ")
# weight_as_int=int(weight)
# height_as_float=float(height)
# body_mass_index= weight_as_int/(height_as_float*height_as_float)
# BMI_as_int=int(body_mass_index)
# print(BMI_as_int)


# print(round(10/3, 3)


# Age = input("What is your age: ")
# age_as_int = int(Age)
# left_year = 90 - age_as_int
# months = (left_year * 12)
# weeks = (left_year * 52)
# days = (left_year * 365)
# Result = f"you have{months}months,{weeks}weeks and {days}days left."
# print(Result)


# sum= 5/6
# sum /=6
# print(sum)

# name=input("enter your name: ")
# length=len(name)
#   # result=str(length)
# print(length)


# print("Welcome to tip calculator")
# bill=float(input(" What is your total bill ? $ "))
# tip=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
# total_people=int(input("how many people to split the bill? "))
# tip_as_percentage=float(tip/100)
# tip_for_billamnt=bill*tip_as_percentage
# amnt_incl_tip= bill+tip_for_billamnt
# bill_per_person= amnt_incl_tip/total_people
# result=bill_per_person
# print( f"your bill for each person is ${result}")


############### Nested if else statement ####################3

# num=int(input("enter a number"))
# if num % 2 == 0 :
#     print(" given number is even number")
# else :
#     print("given number is odd number")


# height_as_cm=int(input("enter your height in cm "))
# weight_as_kg=int(input("enter your weight in kg "))
# if height_as_cm >=185:
#         if weight_as_kg >=70:
#             print("You can play roller coaster ,you have to pay $100")
#         elif weight_as_kg <= 70 >=50:
#             print("you can play roller coaster, you have to pay $50")
#         else: 
#             print("your weight should be reduce before playing roller coaster")
# else:
#     print("your are not eligible play roller coaster")




               
# float(input("enter your weight: "))
# float(input("enter your height: "))
            

# year = int(input("enter a year : "))
# if year %4 ==0:
#     print ("given year is a leap year")
#     if year %100 !=0 :
#         print ("given year is a leap year")
#         if year %400 ==0 :
#             print (" given year is  a leap year")
# else :
#     print ("given year is not a leap year ")

# height_as_cm=int(input("enter your height in cm : "))
# weight_as_kg=int(input("enter your weight in kg : "))
# # bill=0
# if height_as_cm >=185:
#     if weight_as_kg >=70:
#         print("You can play roller coaster ,you have to pay $100")
#         bill = 100
#     elif weight_as_kg <= 70 >=50:
#         print("you can play roller coaster, you have to pay $50")
#         bill = 50
#     elif weight_as_kg <=50:
#         print("you can play roller coaster, you have to pay $30")
#         bill = 30
#     else:  
#         print("your weight should be reduce before playing roller coaster")

#     age_as_num=int(input("enter your age : "))
#     if age_as_num >=50 :
#         bill -= 5
#         print(f" your bill is {bill }") 
#     elif age_as_num <=18 :
#         bill -= 8
#         print(f" your bill is {bill }")
        
#     photo = input("Do you want your photo of playing roller coaster, yes or no : ")
#     if photo == "yes":
#         bill += 10
#         print (f"your total bill is {bill}")
# else:
#     print("your are not eligible play roller coaster")

# print("Welcome to dominos pizza")
# size=input("choose your size  S, M, L : ")
# peporoni=input("do you want peporoni in your pizza Y or N : ")
# double_cheese=input("do you want extra cheese in your pizza Y or N : ")
# bill=0
# if size =="S" :
#     bill = 5
# elif size =="M" :
#     bill = 10
# elif size =="L" :
#     bill = 15
# if peporoni =="Y" :
#     bill += 2
# if double_cheese == "Y" :
#     bill += 5
#     print(f"your bill is {bill}")
# else:
#     print ( f"your total amount is {bill}")

# your_name= (input("enter your name "))
# partner_name= (input("enter your partner name "))
# together = (your_name + partner_name)
# lower_case=together.lower()


# t=lower_case.count("t")
# r=lower_case.count("r")
# u=lower_case.count("u")
# e=lower_case.count("e")

# true = t + r + u + e

# l=lower_case.count("l")
# o=lower_case.count("o")
# v=lower_case.count("v")
# e=lower_case.count("e")

# love = l + o + v + e

# true_love = int(str(true) + str(love))

# if true_love >= 80 or (true_love <=30) :
#     print(" you are made for each other ")
# elif true_love <80 and (true_love >=50) :
#     print(" you are meant to be together ")
# else :
#     print("you are somehow happy i guess")

# print("Welcome to Treasure island.\n you mission  is to find the treasure\n which direction you decided to go ")
# direction = input('"Right""  ""left": ').lower()
# if direction == "left":
#     action = input('"swim""  ""wait": ').lower()
#     if action == "wait":
#         color = input('"blue""  ""red""  ""yellow": ').lower()
#         if color == "blue":
#             print("Eaten by beast\n GAME OVER")
#         elif color == "red":
#             print("Bruned by fire\n GAME OVER")
#         elif color == "yellow":
#             print("yeahhhhhhhhhhhh YOU WINNNNNN!!")
#         else :
#             print("GAME OVER")       
#     else :
#         print("Attacked by by trout\n GAME OVER")
# else :
#     print("Fall into a hole")


################ randomization

# import random

# random_integer = random.randint(1,10)
# print(random_integer)

# random_float = random.random() * 5
# print(random_float)


# import random
# random_integer = random.randint(0,1)
# if  random_integer == 1 :
#     print("Head")
# else :
#     print("tail")



# import random
# name_string=input(" Give me names of you and your friends:  ")
# names = name_string.split(", ")
# num_of_items=(len (names))
# random_choice = random.randint(0,num_of_items - 1)
# person_who_will_pay = names[random_choice]
# print(person_who_will_pay +"is the person who is going to pay ")

# row1 = ["😄","🤔","👍"]
# row2 = ["😴","😄","🤔"]
# row3 = ["👍","😴","😄"]
# map = [ row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}\n")
# position = input("where do you want to put your treasure  ")
# # ex: 26
# horizontal = int( position[0])
# vertical = int(position[1])
# map [vertical-1] [horizontal-1]="x"
# print(f"{row1}\n{row2}\n{row3}\n")


# import random
# rock=("""
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """)

# paper=("""
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """)

# scissors=("""
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """)
# get_images= [rock , paper ,scissors]
# user= int(input("what would like to choose 0 , 1 or 2:\n "))
# if user >=3 or user<0:
#     print (" you enterd a invalid ")
# else:
#     print(get_images[user])
#     computer = random.randint(0 , 2)
#     print("computer choose")
#     print(computer,get_images[computer])
#     if user == computer :
#         print("its draw")
#     elif user >= computer:
#         print("you winn")
#     elif user <= computer:
#         print("you fail")

#!!!!!!!!!!!!!!!Day 5 (loops , range and code blocks)


# students_height = input("enter students height : ").split()
# for n in range (0,  len(students_height)) :
#     students_height[n]= float(students_height[n]) 
# print(students_height)

# total_height = 0
# for height in (students_height):
#     total_height += height
# print (total_height)

# number_of_students = 0
# for student in students_height:
#     number_of_students += 1
# print(number_of_students)

# average_height = round(total_height/number_of_students)
# print(average_height)

# students_score = input("enter students marks : ").split()
# for marks in range (0,  len(students_score)) :
#      students_score[marks]= int(students_score[marks]) 
# print(students_score)

# highest_score =0
# for score in students_score:
#      if score >= highest_score:
#         higest_score = score
# print(f"the higest score is :{higest_score}")      

# total=0
# for sum in range( 2,101,2):
#     # sum_of = int (sum)
#     total += sum
# print(total)


# for sum in range( 1,101):
#     if sum %3 ==0 and sum %5 ==0:
#        print("FIZZBUZZ")
#     elif sum %3 == 0 :
#        print("FIZZ")
#     elif sum %5 == 0:
#        print("BIZZ")
#     else:
#        print(sum)






# import random
# print("Welcome to Pypassword Generator!")
# number = ['0','1','2','3','4','5','6','7','8','9']
# symbol = ['!','@','#','$','%','&','*','+','?']
# letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# symbols=int(input("how many symbols would you like\n"))
# numbers=int(input("how many numbers would you like\n"))
# letters=int(input("how many letters would you like\n"))

# #easy level
# # password=""
# # for char in range (1,letters + 1):
# #     password +=  random.choice(letter)

# # for char in range (1,symbols + 1):
# #     password +=  random.choice(symbol)

# # for char in range (1,numbers + 1):
# #     password +=  random.choice(number)

# # print(password)

# #hard level
# password_list=[]
# for char in range (1,letters + 1):
#     password_list +=  random.choice(letter)

# for char in range (1,symbols + 1):
#     password_list +=  random.choice(symbol)

# for char in range (1,numbers + 1):
#     password_list +=  random.choice(number)

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password =""
# for char in password_list:
#     password += char

# print(f"your password {password}")


###!!!!!!!!!!!!!!!!!!!!!! code blocks ,function and code blocks 

