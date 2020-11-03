import random


def run_game():
    """
    TODO: implement Mastermind code here
    """
    random_number = []
    while len(random_number) != 4:
        x = random.randint(1,8)
        if x in random_number:
            continue
        random_number += [x]
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    # print(random_number)
    
    guesses = 12
    while guesses > 0:
        correct = 0
        wrong = 0
        user_input = ''
        user_input = input("Input 4 digit code: ")
        if len(user_input) != 4:
            print("Please enter exactly 4 digits.")
            continue
        if not user_input.isdigit():
            print("Please enter exactly 4 digits.")
            continue
        if '9' in user_input:
            print("Please enter exactly 4 digits.")
            continue
        if '0' in user_input:
            print("Please enter exactly 4 digits.")
            continue
        
        for a, b in enumerate(random_number):
            if int(user_input[a]) == b:
                correct += 1
            elif str(b) in user_input:
                wrong += 1
        print("Number of correct digits in correct place:    ",correct)
        print("Number of correct digits not in correct place:", wrong)

        code = ""
        for each in random_number:
            code = code + str(each)
        if user_input == code:
            print("Congratulations! You are a codebreaker!")
            print("The code was: "+ code)
            break
        
        guesses -= 1
        print("Turns left:", guesses)


if __name__ == "__main__":
    run_game()