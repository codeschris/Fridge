from random import randint

fridge = ["Rice and beans", "Ugali and sukuma", "Noodles and minced meat", "Fries and chicken", "Rice and cabbage"]

#Storing your food inside the fridge
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
    f = open("example.txt", "w")
    response = input("Have something to add into the fridge?(yes/no) ")
    if response == "yes":
        newFood = input("Add something new: ")
        fridge.append(newFood) #adds one more dish to the fridge
        f.write("\nLet us see the new list")
        f.write(fridge) #check this because of a TypeError

    f.close()

def foodPicker():
    food = len(fridge)
    pick = randint(0, food)
    print("\nYou shall be eating:", fridge[pick])

#function containing all the other functions
def runSystem():
    #storeFridge()
    foodPicker()
    open_file()

#Run the system
runSystem()
