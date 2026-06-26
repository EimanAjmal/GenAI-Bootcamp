import random

secret = random.randint(1, 10)

guess = int(input("Guess a number (1-10): "))

if guess == secret:
    print("🎉 Correct!")

else:
    print("❌ Wrong")
    print("Number was:", secret)