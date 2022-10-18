from random import randint

fridge = ["Rice and beans", "Ugali and sukuma", "Noodles and minced meat", "Fries and chicken", "Rice and cabbage"]

#Storing your food inside the fridge: shadowed to check functionality of File I/O
def storeFridge():
    respond = input("Have something to add into the fridge?(yes/no) ")
    if respond == "yes":
        newFood = input("Add something new: ")
        fridge.append(newFood) #adds one more dish to the fridge
        print("\nLet us see the new list")
        print(fridge)
    else:
        print("Let me show you what is present")
        print(fridge)

def open_file():
    jibu = input("Wanna add something? (yes/no)")

    f = open("example.txt", "w")    #opening a file for writing (done)
    if jibu == "yes":
        new_food = input("Add new stuff: ")
        fridge.append(new_food)
        for item in fridge:
            f.write(f"{item}\t")    #splitting for easy reading (done)
    else:
        for item in fridge:
            f.write(f"{item}\t")   #split items to make it easier to read (done)

    f.close()   #closing the file

def foodPicker():
    food = len(fridge)
    pick = randint(0, food)
    print("\nYou shall be eating:", fridge[pick])  

    #write result inside the text file

#function containing all the other functions
def runSystem():
    #storeFridge()
    open_file()
    foodPicker()

#Run the system
runSystem()