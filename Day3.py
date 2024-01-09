#ticket payment and photo price

height=int(input("Enter a Height in cm\n"))
ticket=0

if(height<120):
    print("Your height is too short for the ticket. It should be at least 120cm\n")
elif(height>=120):
    age=int(input("Enter a Age\n"))
    if age<12:
        ticket=5
    elif(age>=12 and age<18):
        ticket=7
    else:
        ticket=12
if(ticket!=0):
    pht=input("Do you want Photos [Y/N]\n")
    if ( pht=='Y'or pht=='y'):
        ticket=ticket+3
    print(f"Your ticket price is {ticket} ")
