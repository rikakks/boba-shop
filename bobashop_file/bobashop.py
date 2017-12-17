from datetime import datetime
now = datetime.now()
date = now.month + now.day
from PIL import Image
from playsound import playsound
import thread

thread.start_new_thread(playsound, ('music.mp3',))


tea_boba = [
    'Earl Grey Milk Tea',
    'Black Milk Tea',
    'Oolong Milk Tea',
    'Jasmine Milk Tea',
    'Classic Milk Tea',
]
recommended_tea_boba = tea_boba[date % len(tea_boba)]



fruit_boba = [
    'Mango Green Tea',
    'Peach Black Tea',
    'Lemon Darjeeling Tea',
]
recommended_fruit_boba = fruit_boba[date % len(fruit_boba)]



creama_boba = [
    'Earl Grey Creama',
    'Oreo Creama',
    'Chocolate Creama',
    'Classic Milk Tea Creama',
]
recommended_creama_boba = creama_boba[date % len(creama_boba)]


def select_boba(kind, boba_list):
    print("Okay! Here is a list of %s boba: ") % kind
    for i in range(len(boba_list)):
        print('%i. %s') % (i, boba_list[i])
    selection = int(raw_input("Which one would you like? To select one, enter a number: "))
    if 0 <= selection < len(boba_list):
        boba = boba_list[selection]
    else:
        print("I'm sorry, but I didn't quite get that. Can you repeat that again? ")
        return
    print("Okay, great! We will make you your %s in no time!") % boba
    return boba


def boba_shop():
    print("Hello, and welcome to our boba shop.")
    if raw_input("Enter 'y' or 'yes' to proceed: ") not in ('y', 'yes'):
        print("Thank you for checking us out. Please come again.")
        return

    print("""1. I want to choose a boba!
2. I want a boba recommendation!
3. I want to make my own boba!""")

    help_input = raw_input("Please enter a number: ")
    if help_input == '1':
        print("""Okay, good! Sounds like you want to choose from our wide selection of bobas!
1. Milk Tea
2. Fruit Tea
3. Sea Salt Creama""")
        type_of_boba = raw_input("What type of boba are you looking for? Please enter a number: ")

        if type_of_boba == '1':
            boba = select_boba("Milk Tea Boba", tea_boba)

        if type_of_boba == '2':
            boba = select_boba("Fruit Tea Boba", fruit_boba)

        if type_of_boba == '3':
            boba = select_boba("Creama Boba", creama_boba)

    elif help_input == '2':
        print("""Okay, sounds like you want a recommendation!
Let me ask you some questions.""")

        creamy_or_sappari = raw_input("Do you like cream? Enter 'y' or 'n': ")
        if creamy_or_sappari == 'y':
            salty_or_not = raw_input("Do you like something salty? Enter 'y' or 'n': ")

            if salty_or_not == 'y':
                boba = recommended_creama_boba
                print("Great choice! I recommend %s!") % boba

            elif salty_or_not == 'n':
                boba = recommended_tea_boba
                print("Great taste! I recommend %s!") % boba

            else:
                print("Sorry, I didn't quite get that! Please try again. ")
                return


        elif creamy_or_sappari == 'n':
            likecitrus = raw_input("Do you like citrus fruits? Enter 'y' or 'n'.")

            if likecitrus == 'y':
                boba = 'Lemon Darjeeling Tea'
                print("Great! I recommend %s!") % boba

            elif likecitrus == 'n':
                boba = recommended_fruit_boba
                print("Great! I recommend %s!") % boba

            else:
                print("Sorry, I didn't quite get that! Please try again. ")
                return
        else:
            print("Sorry, I didn't quite get that! Please try again. ")
            return


    elif help_input == '3':
        print("Okay, so you want to make your own boba! Let's get started!")
        proceed = raw_input("Enter 'y' or 'yes' to proceed: ")


        if proceed == 'y' or proceed == 'yes':
            print("Here is a list of tea that we offer: 1. Black Tea, 2. Green Tea, 3. Earl Grey Tea")
            type_of_tea = raw_input("What type of tea would you like to get? Enter a number: ")

            if type_of_tea == '1':
                boba = 'black tea'
            elif type_of_tea == '2':
                boba = 'green tea'
            elif type_of_tea == '3':
                boba = 'earl grey tea'
            else:
                print("Sorry, I didn't quite get that! Please try again. ")
                return
        # else:   TODO: fic this part
        #     print("I'm sorry, ")
        #
        #     creaminess_of_tea = raw_input("Do you want to add milk? Type 'y' or 'n'.")
        #
        #     if creaminess_of_tea == 'y':
        #         creaminess_of_tea = 'milk'
        #     else:
        #         creaminess_of_tea = 'no milk'
        #
        #     boba = "%s with %s" % (type_of_tea, creaminess_of_tea)
        #
        #     print("Okay, we've got your order!")






    proceed = raw_input("Enter 'y' or 'yes' to proceed: ")

    if proceed.lower() == 'y' or proceed.lower() == "'y'" or proceed.lower() == 'yes':

            print("Here is a list of toppings that we offer.")
            print("1. Pearls, 2. Lychee, 3.Grassjelly, 4.Creama")
            toppings = raw_input("Would you like to get any toppings? Type a number or answer 'n' for no: ")

            if toppings == '1':
                toppings = "pearls"
            elif toppings == '2':
                toppings = "lychee"
            elif toppings == '3':
                toppings = "grassjelly"
            elif toppings == '4':
                toppings = "creama"
            elif toppings == 'n':
                toppings = "no toppings"
            else:
                print("Sorry, I didn't quite get that! Please try again.")
                return

            print("Okay, great!")


    else:
        print("It seems like you didn't enter a valid number. Please come back again!")
        return




    proceed = raw_input("Enter 'y' or 'yes' to proceed: ")

    if proceed.lower() == 'y' or proceed.lower() == "'y'" or proceed.lower() == 'yes':

        print("Now, please specify preferred percentage of ice.")
        percentage_of_ice = raw_input("Enter a number between 0-100: ")

        print("Now, please specify preferred sugar level.")
        percentage_of_sugar = raw_input("Enter a number between 0-100: ")

    else:
        print("Sorry, I didn't quite get that! Please try again.")
        return




    proceed = raw_input("Enter 'y' or 'yes' to proceed: ")

    if proceed.lower() == 'y' or proceed.lower() == "'y'" or proceed.lower() == 'yes':
        print("Great! Your boba is almost ready.")
        print("We just need one more thing.")
        name = raw_input("What is your name? ")

    else:
        print("Sorry, I didn't quite get that! Please try again.")
        return





#confirmation of order
    proceed = raw_input("Enter 'y' or 'yes' to proceed: ")

    if proceed.lower() == 'y' or proceed.lower() == "'y'" or proceed.lower() == 'yes':
        print("Thanks, %s! So let's confirm your order.") % name
        print("You ordered: %s with toppings of %s, ice level is %s and sweetness level is %s.") % (boba, toppings, percentage_of_ice, percentage_of_sugar)



    else:
        print("Sorry, I didn't quite get that! Please try again.")
        return



    proceed = raw_input("Is this correct? Enter 'y' or 'yes' to proceed: ")

    if proceed.lower() == 'y' or proceed.lower() == "'y'" or proceed.lower() == 'yes':
        print("Okay, %s! Your boba is now ready.") %name

        boba = boba.replace(' ', '')
        boba = boba.lower()
        order = boba + "_" + toppings
        address = order + ".png"
        im = Image.open(address)
        im.show()


    else:
        print("Sorry, I didn't quite get that! Please try again.")
        return




    proceed = raw_input("Enter 'q' or 'quit' to leave shop: ")

    if proceed.lower() == 'q' or proceed.lower() == "'q'" or proceed.lower() == 'quit':
        print('Thanks for getting boba from us! We hope you come again!')


    else:
        print("Sorry, I didn't quite get that! Please try again.")
        return


boba_shop()
