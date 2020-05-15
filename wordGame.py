print("Ready to play the fun Mad Libs Word Game? ")
print("Lets go!!")


def game():
    category = input("Choose a category (1 to 5): ")
    print('''1- Noun
    2- Plural Noun
    3- Adjective 
    4- Verb
    5- Article of clothing''')
    if category == "1":
        input_user = input("Enter a noun: ")
        print(f"Love is what makes the {input_user.lower()} go round.❤")
        play_again()
    if category == "2":
        input_user = input("Enter a plural noun: ")
        print(f"Be careful not to vacuum the {input_user.lower()} when you clean under your bed.")
        play_again()
    if category == "3":
        input_user = input("Enter an adjective: ")
        print(f"Once that {input_user.lower()} music comes on, it's time to shut down your acceptance speech.")
        play_again()
    if category == "4":
        input_user = input("Enter a verb (ending in -ing): ")
        print(f"My daily exercise is {input_user.lower()} after my school bus in the morning")
        play_again()
    if category == "5":
        input_user = input("Enter an article of clothing (plural): ")
        print(f"My gym locker stinks because I'm always leaving my dirty {input_user.lower()} in there!!")
        play_again()


def play_again():
    again = input("Wanna play again? (yes or no): ")
    if again.lower() == "yes":
        game()
    elif again.lower() == "no":
        print("game ends!! :)")
    else :
        print("Enter from yes or no only!")
        play_again()


game()



