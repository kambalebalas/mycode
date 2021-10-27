#!/usr/bin/python3
#"" What is your Zodiac Sign "

def main():
    name= input("What is your name:   ").capitalize()
    # you can slice strings, too-- [0] will return the first letter
    first_letter= name[0]
    print(first_letter)

    if first_letter in ["A","B","C"]:
       print("Your zodiac sign is Auries")
    elif first_letter in ["D","E","F"]:
        print("Your Zodisc sign is Taurus ")
    elif  first_letter in ("G","T","K"):
        print("Your Zodisc sign is Gemini")
    elif  first_letter in ("S","N","L"):
        print("Your Zodisc sign is Leo")
    elif  first_letter in ("I","H","P"):
        print("Your Zodisc sign is Scorpio")
    else:                 # if name was wrong
        print ("Sorry, your name dont have any Zodiac sign ")
main()
