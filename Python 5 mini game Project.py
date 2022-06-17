                                            # Hello everyone!

                                    # Python mini game Project.

                                # Xush kelibsiz mening kompyuter o'yinimga!


#print("Xush kelibsiz mening kompyuter o'yinimga!")

#savol = input("O'yin o'ynashni xohlaysizmi? ")

#if savol.lower() == "ha":
    #print("Yaxshi, unda bowladik! ")
#else:
    #print("Xayr!")
    #quit()
#score = 0

#savol1 = input("Jonubiy Koreyani Poytaxti? " )

#if savol1.lower() == "seul":
    #print("Topdingiz!")
    #score += 1
#else:
    #print("Topolmadingiz!")

#savol1 = input("Xitoyni Poytaxti? " )

#if savol1.lower() == "pekin":
    #print("Topdingiz!")
    #score += 1
#else:
    #print("Topolmadingiz!")

#savol1 = input("USni Poytaxti? ")

#if savol1.lower() == "vashington":
    #print("Topdingiz!")
    #score += 1
#else:
     #print("Topolmadingiz!")

#savol1 = input("O'zbekistonni Poytaxti? ")

#if savol1.lower() == "toshkent":
    #print("Topdingiz!")
    #score += 1
#else:
    #print("Topolmadingiz!")

#savol1 = input("UKni Poytaxti? ")

#if savol1.lower() == "london":
    #print("Topdingiz!")
    #score += 1
#else:
    #print("Topolmadingiz!")

#print("Siz "+ str(score) + " ta to'g'ri javob topdingiz!")
#print("Siz "+ str((score/5)*100) + " % " "to'g'ri javob berdingiz!")


                                                    #Project2

#import random

#top_of_range = input("Type a number: ")

#if top_of_range.isdigit():
    #top_of_range = int(top_of_range)

    #if top_of_range <= 0:
        #print("Please type a number larger than 0 next time.")
        #quit()
#else:
    #print("Please type a number next time.")
    #quit()

#random_number = random.randint(0,top_of_range)
#guess = 0

#while True:
    #guess += 1
    #user_guess = input("Make a guess:")
    #if user_guess.isdigit():
        #user_guess = int(user_guess)
    #else:
        #print("Please type a number next time.")
        #continue

    #if user_guess == random_number:
        #print("You got it!")
        #break
    #elif user_guess > random_number:
        #print("You were above the number!")
    #else:
        #print("You were below the number!")

#print("You got it in", guess, "guesses")


