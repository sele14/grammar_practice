# Language practice
def words():
    print("This program lets you practice sentences in English, French, or German.")
    # French file
    fnFr = "fransk.txt"
    filFr = open(fnFr, "r")

    # English file
    fnEn = "engelsk.txt"
    filEn = open(fnEn, "r")
    
    # German file
    fnTy = "tysk.txt"
    filTy = open(fnTy, "r")

    user = input("Enter a language: ")

    # English word game
    if user == "English":

        # Line 1
        for i in range(1):
            line = filEn.readline()
            print(line[:6])
        correct = False
        while not correct:
            svar = input("Translate to English: ")
            if svar == "I am":
                print("Correct.")
                correct = True
            else:
                print("Wrong. Try again")

        # Line 2
        for i in range(1,2):
            line = filEn.readline()
            print(line[:6])
        correct = False
        while not correct:
            svar = input("Translate to English: ")
            if svar == "You are":
                print("Correct.")
                correct = True
            else:
                print("Wrong. Try again")
        # Line 3
        for i in range(2,3):
            line = filEn.readline()
            print(line[:6])
        correct = False
        while not correct:
            svar = input("Translate to English: ")
            if svar == "He is":
                print("Correct.")
                correct = True
            else:
                print("Wrong. Try again")

        # Line 4
        for i in range(3,4):
            line = filEn.readline()
            print(line[:6])
        correct = False
        while not correct:
            svar = input("Translate to English: ")
            if svar == "We are":
                print("Correct.")
                correct = True
            else:
                print("Wrong. Try again")

        # Line 5
        for i in range(3,4):
            line = filEn.readline()
            print(line[:6])
        correct = False
        while not correct:
            svar = input("Oversett til Engelsk: ")
            if svar == "You are":
                print("Correct.")
                correct = True
            else:
                print("Wrong. Try again")

        # Line 5
        for i in range(3,4):
            line = filEn.readline()
            print(line[:6])
        correct = False
        while not correct:
            svar = input("Oversett til Engelsk: ")
            if svar == "They are":
                print("Correct.")
                correct = True
            else:
                print("Wrong. Try again")
 

    # French word game        
    elif user == "French":

        # Line 1
        for i in range(1):
            line = filFr.readline()
            print(line[:6])
        correct = False
        while not correct:
            svar = input("Translate to French: ")
            if svar == "Je suis":
                print("Correct.")
                correct = True
            else:
                print("Wrong. Try again")
        
        # Line 2
        for i in range(1,2):
            line = filFr.readline()
            print(line[:6])
        correct = False
        while not correct:
            svar = input("Translate to French: ")
            if svar == "Tu es":
                print("Correct.")
                correct = True
            else:
                print("Wrong. Try again")

        # Line 3
        for i in range(2,3):
            line = filFr.readline()
            print(line[:6])
        correct = False
        while not correct:
            svar = input("Translate to French: ")
            if svar == "Il est":
                print("Correct.")
                correct = True
            else:
                print("Wrong. Try again")

        # Line 4
        for i in range(3,4):
            line = filFr.readline()
            print(line[:6])
        correct = False
        while not correct:
            svar = input("Oversett til Engelsk: ")
            if svar == "Nous sommes":
                print("Correct.")
                correct = True
            else:
                print("Wrong. Try again")

        # Line 5
        for i in range(4,5):
            line = filFr.readline()
            print(line[:7])
        correct = False
        while not correct:
            svar = input("Oversett til Engelsk: ")
            if svar == "Vous etes":
                print("Correct.")
                correct = True
            else:
                print("Wrong. Try again")

        # Line 6
        for i in range(5,6):
            line = filFr.readline()
            print(line[:6])
        correct = False
        while not correct:
            svar = input("Translate to French: ")
            if svar == "Ils sont":
                print("Correct.")
                correct = True
            else:
                print("Wrong. Try again")


    # German word game
    elif user == "German":
        # Body, German

        # Line 1
        for i in range(1):
            line = filTy.readline()
            print(line[:6])
        correct = False
        while not correct:
            svar = input("Translate to German: ")
            if svar == "Ich bin":
                print("Correct.")
                correct = True
            else:
                print("Wrong. Try again")
        
        # Line 2
        for i in range(1,2):
            line = filFr.readline()
            print(line[:6])
        correct = False
        while not correct:
            svar = input("Translate to German: ")
            if svar == "Du bist":
                print("Correct.")
                correct = True
            else:
                print("Wrong. Try again")

        # Line 3
        for i in range(2,3):
            line = filFr.readline()
            print(line[:6])
        correct = False
        while not correct:
            svar = input("Translate to German: ")
            if svar == "Er ist":
                print("Correct.")
                correct = True
            else:
                print("Wrong. Try again")

        # Line 4
        for i in range(3,4):
            line = filFr.readline()
            print(line[:6])
        correct = False
        while not correct:
            svar = input("Translate to German: ")
            if svar == "Wir sind":
                print("Correct.")
                correct = True
            else:
                print("Wrong. Try again")

        # Line 5
        for i in range(4,5):
            line = filFr.readline()
            print(line[:7])
        correct = False
        while not correct:
            svar = input("Translate to German: ")
            if svar == "Ihr seid":
                print("Correct.")
                correct = True
            else:
                print("Wrong. Try again")

        # Line 6
        for i in range(5,6):
            line = filFr.readline()
            print(line[:6])
        correct = False
        while not correct:
            svar = input("Translate to German: ")
            if svar == "Sie sind":
                print("Correct.")
                correct = True
            else:
                print("Wrong. Try again")

