print("Welcome to my Computer Quiz")

playing = input("Do you want to play> ")
# "Name: "Apoorv -->> prompt

#   .lower() method in python for YES,Yes,YeS, yes and etc.
#   .upper() methid is alternate method for upper
if playing.lower() != "yes":
    quit()

print("Let's Play :) ")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct.!')
    score += 1
else:
    print('Incorrect..!')


answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct.!')
    score += 1
else:
    print('Incorrect..!')

# if we remove only '()' from function then still program works but
# without displaying any error but it,
# donot convert the input into lower
answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print('Correct.!')
    score += 1
else:
    print('Incorrect..!')


answer = input("What does PSU stand for? ").lower()
if answer == "power supply":
    print('Correct.!')
    score += 1
else:
    print('Incorrect..!')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4)*100) + "%.")