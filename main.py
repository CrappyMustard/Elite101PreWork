#Some code came from a previous project of mine from Code2College SDE1.
#https://codehs.com/sandbox/korrigan/the-everything-store/run

import time
import random

random_response = ["Cool name!", "What a great name!", "Sounds like your parents did you good!", "That name sounds amazing!"]

def ageChecker():
  age = input("Sorry if I'm being a bit intrusive, but could I get your age, too? ")
  try:
    newAge = int(age)
  except ValueError:
    print(f"Sorry, {user_name}, didn't catch that. Try again?")
    time.sleep(2)
    ageChecker()
    return
  if newAge < 13:
    print(f"{newAge}, huh? Quite young, don't you think?")
  elif newAge >= 13 and newAge < 18:
    print(f"{newAge}, huh? Ah, I miss my teen years...")
    time.sleep(1)
    print("Wait...did I even have teen years?")
  elif newAge >= 18 and newAge < 65:
    print(f"Wow, you're {newAge}? All grown up, aren't we?")
  elif newAge >= 65:
    print(f"{newAge}, aren't we? Maybe I should talk in 1's and 0's...")
    time.sleep(2)
    print("I'm joking, hahaha!")

def display_options():
  print(f"How can I be of service, {user_name}?")
  time.sleep(1)
  print("1 - Tell me more about this company")
  print("2 - Tell me more about you")
  print("3 - Tell me about company hours")
  print("4 - Tell me about being hired for this company")
  print("5 - Exit")

def user_selection():
  user_select = input("Enter a number between 1 and 5 here... ")
  if user_select == "1":
    print("This company helps people learn how to make chatbots like me!")
    time.sleep(2)
    user_selection()
  elif user_select == "2":
    print("More about me?")
    time.sleep(2)
    print(f"Well, {user_name}, I personally enjoy hiking, cooking, taking photos of nature, hanging out with friends--")
    time.sleep(1)
    print("Oops! I guess I started rambling a bit...")
    time.sleep(2)
    user_selection()
  elif user_select == "3":
    print("From Monday to Friday, 9:00 AM to 5:00 PM.")
    time.sleep(2)
    user_selection()
  elif user_select == "4":
    print("We are not currently hiring at this time. Sorry!")
    time.sleep(2)
    user_selection()
  elif user_select == "5":
    print(f"Thanks for using me, {user_name}! See you again soon!")
  else:
    print("Sorry, I didn't catch that. Try again?")
    time.sleep(2)
    user_selection()

print("Hey there!")
time.sleep(1)
print("The name's ChatterBot!")
time.sleep(1)
print("But you can just call me Chatter!")
time.sleep(2)
print("I'm here to help answer all your questions you have about this company!")
time.sleep(2)
user_name = input("Before we begin, could you mind giving me your name? ")
print(f"{user_name}...")
time.sleep(2)
print(random.choice(random_response))
time.sleep(2)
ageChecker()
time.sleep(2)
print(f"Thanks for the information, {user_name}! Now let's get started!")
time.sleep(2)
display_options()
user_selection()