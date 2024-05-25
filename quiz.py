print("Welcome to my Beatles Quiz!")
playing = input("Do you want to play? ")

if playing.lower() != "yes": 
    quit()
  
print("Okay! Let's rock!")
score = 0

answer = input("Who was the first drummer for the Beatles? ")

if answer.lower() == "pete best":
    print("Correct!")
    score += 1 
else: 
    print("Too bad, incorrect!")

answer = input("To which German city did the Beatles move in the 60s? ")
if answer.lower() == "hamburg":
    print("That is right!")
    score += 1
else: 
    print("Too bad, incorrect!")

answer = input("In which city was John Lennon murdered? ")
if answer.lower() == "new york":
    print("That is right!")
    score += 1 
else: 
    print("Too bad, incorrect!")

answer = input("What was the Beatles first album? ")
if answer.lower() == "please please me":
    print("That is right!")
    score += 1 
else: 
    print("Too bad, incorrect!")

answer = input("In which city can you find the real ‘Abbey Road’? ")
if answer.lower() == "london":
    print("That is right!")
    score += 1 
else: 
    print("Too bad, incorrect!")

answer = input("Who played lead guitar on ‘While My Guitar Gently Weeps’? ")
if answer.lower() == "eric clapton":
    print("That is right!")
    score += 1 
else: 
    print("Too bad, incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")
