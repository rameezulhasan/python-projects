import random

"""
    snake ---> water
    water ---> gun
    gun   ---> snake
    
    1 = snake
    0 = gun
    -1 = water
"""
while True:
    print("\n \n Welcome To Rock, Paper, Scissor Game \n Please Write rock, paper, scissor as you want")
    computer = random.choice([-1,0,1])
    take_player_value = input("Enter any choice: ")
    player_value_dic = {
    "rock":1,
    "paper":0,
    "scissor":-1
     }
    reversed_player_value_dic = {
    1:"rock",
    0:"paper",
    -1:"scissor"
    }

    final_value = player_value_dic[take_player_value]

    print(f"\n You choose '{reversed_player_value_dic[final_value]}' and   computer choose '{reversed_player_value_dic[computer]}'")
    
    # if(computer == 1 and final_value == -1):    2
#         print(" You are lose!")
#       elif(computer == 1 and final_value == 0):  1
#         print(" Congratulations! You are win")
#       elif(computer == -1 and final_value == 0):  -1
#         print(" You are lose!")
#       elif(computer == -1 and final_value == 1): -2 
#         print(" Congratulations! You are win")
#       elif(computer == 0 and final_value == 1):  -1
#         print(" You are lose!")
#       elif(computer == 0 and final_value == -1): 1
#         print(" Congratulations! You are win")

    if (computer == final_value):
      print(" Game is Draw")
    else:
      if(computer - final_value == -1 or computer - final_value == 2):
        print(" You are lose!")
      elif(computer - final_value == 1 or computer - final_value == -2):  
        print(" Congratulations! You are win")
      
      else:
        print("Something Went Wrong!")