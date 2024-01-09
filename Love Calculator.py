print("The Love Calculator is calculating your score...")
name1 = input("Boys's  Name?\n") 
name2 = input("Girl's Name?\n") 
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
n1=name1.lower()
n2=name2.lower()
t=['t','r','u','e']
l=['l','o','v','e']
c1=0
c2=0
for i in range(len(t)):
    if t[i] in n1:
        c1+=n1.count(t[i])
    i+=1
for i in range(len(t)):
    if t[i] in n2:
        c1+=n2.count(t[i])
    i+=1
for i in range(len(l)):
    if l[i] in n1:
        c2+=n1.count(l[i])
    i+=1
for i in range(len(l)):
    if l[i] in n2:
        c2+=n2.count(l[i])
    i+=1
s=str(c1)+str(c2)
score=int(s)
if (score<10 or score>90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score>40 and score<50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
