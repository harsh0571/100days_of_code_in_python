#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill=int(input("What is the total bill?\n"))
pep=int(input("How many people are there?\n"))
tip_per=int(input("What is the tip percentage?\n"))
tip=(bill/pep)*(tip_per/100+1)

rtip=round(tip,2)
#round off the final price 2 after commoa represent the upto how much decimal places round off

print("Each person shold pay",rtip)