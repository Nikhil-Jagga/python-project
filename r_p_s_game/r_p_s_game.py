import random

# random_int = random.randint(0,1)
# if random_int == 1:
#     print("Heads")
# else:
#     print("Tails")

# arr = [1, 122, 9, 4, 10]
# arr.append(22)

# arr.insert(2, 3)
# arr.extend([29, 12])

# print(name)
# arr.sort()
# print(arr.index(10))
# print(arr)
# print(sum(arr))

# names = "vivek ram krisha"
# name = names.split(" ")
# random_name = random.randrange(0,len(name))
# person = name[random_name]
# print(person)


# arr = [124, 134, 1020, 129]
# names = ['ravi', 'mahesh', 'vivek']
# combine = [arr,names]
# print(combine[-1])

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]


user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print('Computer choose: ')
print(game_images[computer_choice])


if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose 🥲!")
elif user_choice == 0 and computer_choice == 2:
    print("you win ✌️")
elif computer_choice == 0 and user_choice == 2:
    print('you lose 🥲')
elif computer_choice > user_choice:
    print('you lose 🥲')
elif user_choice > computer_choice:
    print('you win ✌️')
elif computer_choice == user_choice:
    print('Its a draw 🥱🥱')
