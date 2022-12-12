#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $ "))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
no_of_persons = float(input("How many people to split the bill? "))
tip = (float(tip_percentage) * float(total_bill)) / 100
total_bill += float(tip)
each_person = float(total_bill)/float(no_of_persons)
bill= round(each_person,2);
print(f"Each person will pay $ {bill} ")