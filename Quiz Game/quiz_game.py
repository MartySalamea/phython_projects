print("Welcome to my Quiz Game!")

playing = input("Are you ready to Play? ")

if playing.lower() != "yes":
    quit()

print("Okay get Ready!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Favorite city? ")
if answer.lower() == "cuenca":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Favorite pet? ")
if answer.lower() == "dog":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")     

print("You got " + str(score) + " questions correct!")        
print("You got " + str((score / 4) * 100) + "%")        


