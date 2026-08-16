
score = 0

print("Welcome to Python Quiz Game!")
print()

answer = input("1. What is the capital of India? ")

if answer.lower() == "delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print()

answer = input("2. Which language is used for AI mostly? ")

if answer.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print()

answer = input("3. How many days are there in a week? ")

if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print()
answer = input("What is the correct spelling of pyton?")
if answer.lower() == "python"
    print("Correct!")
    score +=1
esle:
    print("Wrong")
answer = input("How many months in a year?")
if answer.lower() == "12"
    print("Correct!")
    score +=1
esle:
    print("Wrong")

print("Quiz Finished!")
print("Your score is:", score, "/ 5")
