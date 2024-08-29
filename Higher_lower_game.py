import game_art
import random
import os
import game_database
score=0
def display_info(account):
    name=account['name']
    des=account['description']
    country=account['country']
    return f"{name},{des}, from {country}"

def check_answer(choice,count1,count2):
    global score
    if (choice==1 and count1>count2) or (choice==2 and count2>count1) or(choice==1 and count1==count2) or (choice==2 and count1==count2):
        return True
    else:
        return False

def game(s1,s2):
    global score
    result1=display_info(s1)
    print(f"Compare 1: {result1}")
    print(game_art.vs)
    result2=display_info(s2)
    print(f"Compare 2: {result2}")
    count1=s1['follower_count']
    count2=s2['follower_count']
    print(count1)
    print(count2)
    choice=int(input("Who has more followers?Type '1' or '2':"))
    answer=check_answer(choice,count1,count2)
    if answer:
        score+=1
        s1=s2
        os.system('cls')
        print(game_art.art)
        s2=random.choice(game_database.data)
        print(f"You are right .Your score is {score}")
        game(s1,s2)
    else:
        os.system('cls')
        print(game_art.art)
        print(f"You are wrong.Your final score is {score}")
    
print(game_art.art)
s1=random.choice(game_database.data)
s2=random.choice(game_database.data)
game(s1,s2)
