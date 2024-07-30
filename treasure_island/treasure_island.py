print("Welcome to Treasre Island.\nYour mission is to find the treasure.")
direction = input("left or right? ").lower()

if direction == "left":
    work = input("swim or wait? ").lower()
    if work == "wait":
        door = input("red , yellow or blue? ")
        if door == "red":
            print("game over :(")
        elif door == "blue":
            print("game over :(")
        elif door == "yellow":
            print("You Won!! Treasure yours....")
        else:
            print("Game over :(")
    else:
        print("Game Over :(")
else:
    print("Game Over :(")
