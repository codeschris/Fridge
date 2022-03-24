from random import randint

fridge = ["Rice and beans", "Ugali and sukuma"]

#Storing your food inside the fridge
def storeFridge():
    respond = input("Have something to add into the fridge?(yes/no) ")
    if respond == "yes":
        newFood = input("Add something new: ")
        fridge.append(newFood)
    else:
        print("Alright friend")
    print(fridge)

def foodPicker():
    food = len(fridge)
    pick = randint(0, food)
    print("\n You shall be eating:", fridge[pick])

def runSystem():
    storeFridge()
    foodPicker()

#Run the system
runSystem()
