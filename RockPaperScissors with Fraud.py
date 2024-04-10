print("please choose your weapon: ")
print("1. Rock", "2. Paper", "3. Scissor")
while True:
    p_c = int(input("choose 1, 2 or 3 and for exit choose 0: "))
    # If the input was 0, it will exit the program. break-->is for loop (for & while)
    if p_c == 0:
        break
    weapons = {1: 'Rock', 2: 'Paper', 3: 'Scissor'}
    if p_c == 1:
        print("I choose Paper")
        print("I won :p ")
    elif p_c == 2:
        print("I choose Scissor")
        print("I won :p ")
    elif p_c == 3:
        print("I choose Rock")
        print("I won :p ")

# Name of the programmer: Maryam Jamali
# Email address: m.jamali16@yahoo.com
# GitHub address: https://github.com/MaryaJamali
