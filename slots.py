import random
import numpy as np
from MyDB import update_data
# from main import *

low_tier_table={
    'watermelon':20,
    'Seven':50,
    'grapes':90,
    'orange':90,
    'bell':90,
    'cherries':100,
    '$':150,
    'lemon':100,
    'barx1':50,
    'barx2':100,
    'barx3':300,
    'horseshoe':150,
    'lucky charm':300,
    'apple':100,
    'coins':50,
    'hearts':50,
}

high_tier_table={
    'king':200,
    'queen':160,
    'jack':140,
    'prince':100,
    'princess':100,
    'knight':120,
    'diamond':200,
    'horseshoe':160,
    '7':180,
    '$':200
}

# def do_the_thing():
    # key1,value1=random.choice(list(high_tier_table.items()))
    # key2,value2=random.choice(list(high_tier_table.items()))
    # key3,value3=random.choice(list(high_tier_table.items()))
    # arr=np.array([key1,key2,key3])

    # arr=np.array([key1,key1,key1])

# key1,value1=random.choice(list(high_tier_table.items()))
# key2,value2=random.choice(list(high_tier_table.items()))
# key3,value3=random.choice(list(high_tier_table.items()))


# print(f"{key1} | {key2} | {key3}")

# arr=np.array([key1,key2,key3])
# print(arr)

def checker():
    if all(arr==key1):
        print('\nJackpot')
        jackpot=key1+key2+key3
        update_data(f'{member.discriminator}','+',f'{jackpot}')
        return f"{key1} | {key2} | {key3}\n{jackpot}"
        
    elif arr[0]==arr[1]:
        print(f"\n{key1} | {key2} | {key3}")
        print(f"{value1}|{value2}|{value2}")
        print(value1+value2)
        win=key1+key2
        return f"{key1} | {key2} | {key3}\n{win}"

    elif arr[0]==arr[2]:
        print(f"\n{key1} | {key2} | {key3}")
        print(f"{value1}|{value2}|{value3}")
        print(value1+value3)
        win=key1+key3
        return f"{key1} | {key2} | {key3}\n{win}"

    elif arr[1]==arr[2]:
        print(f"\n{key1} | {key2} | {key3}")
        print(f"{value1}|{value2}|{value3}")
        print(value2+value3)
        win=key2+key3
        return f"{key1} | {key2} | {key3}\n{win}"


def low_tier(password):
    key1,value1=random.choice(list(low_tier_table.items()))
    key2,value2=random.choice(list(low_tier_table.items()))
    key3,value3=random.choice(list(low_tier_table.items()))
    arr=np.array([key1,key2,key3])

    # arr=np.array([key1,key1,key1])
    # checker()
    if all(arr==key1):
        # print('\nJackpot')
        jackpot=value1+value2+value3
        # update_data(f'{member.discriminator}','+',f'{jackpot}')
        update_data(f'{password}','+',f'{jackpot}')
        return f"{key1} | {key2} | {key3}\nJACKPOT\nYou win ${value1+value2+value3}"
        
    elif arr[0]==arr[1]:
        # print(f"\n{key1} | {key2} | {key3}")
        # print(f"{value1}|{value2}|{value2}")
        # print(value1+value2)
        win=value1+value2
        update_data(f'{password}','+',f'{win}')
        return f"{key1} | {key2} | {key3}\nYou win ${value1+value2}"

    elif arr[0]==arr[2]:
        # print(f"\n{key1} | {key2} | {key3}")
        # print(f"{value1}|{value2}|{value3}")
        # print(value1+value3)
        win=value1+value3
        update_data(f'{password}','+',f'{win}')
        return f"{key1} | {key2} | {key3}\nYou win ${value1+value3}"

    elif arr[1]==arr[2]:
        # print(f"\n{key1} | {key2} | {key3}")
        # print(f"{value1}|{value2}|{value3}")
        # print(value2+value3)
        win=value2+value3
        update_data(f'{password}','+',f'{win}')
        return f"{key1} | {key2} | {key3}\nYou win ${value2+value3}"

    else:
        lost=100
        update_data(f'{password}','-',f'{lost}')
        return f"{key1} | {key2} | {key3}\nYou lose"


def high_tier(password):
    key1,value1=random.choice(list(high_tier_table.items()))
    key2,value2=random.choice(list(high_tier_table.items()))
    key3,value3=random.choice(list(high_tier_table.items()))
    arr=np.array([key1,key2,key3])

    # arr=np.array([key1,key1,key1])
    # checker()
    if all(arr==key1):
        # print('\nJackpot')
        jackpot=value1+value2+value3
        # update_data(f'{member.discriminator}','+',f'{jackpot}')
        update_data(f'{password}','+',f'{jackpot}')
        return f"{key1} | {key2} | {key3}\nJACKPOT\nYou win ${value1+value2+value3}"
        
    elif arr[0]==arr[1]:
        # print(f"\n{key1} | {key2} | {key3}")
        # print(f"{value1}|{value2}|{value2}")
        # print(value1+value2)
        win=value1+value2
        update_data(f'{password}','+',f'{win}')
        return f"{key1} | {key2} | {key3}\nYou win ${value1+value2}"

    elif arr[0]==arr[2]:
        # print(f"\n{key1} | {key2} | {key3}")
        # print(f"{value1}|{value2}|{value3}")
        # print(value1+value3)
        win=value1+value3
        update_data(f'{password}','+',f'{win}')
        return f"{key1} | {key2} | {key3}\nYou win ${value1+value3}"

    elif arr[1]==arr[2]:
        # print(f"\n{key1} | {key2} | {key3}")
        # print(f"{value1}|{value2}|{value3}")
        # print(value2+value3)
        win=value2+value3
        update_data(f'{password}','+',f'{win}')
        return f"{key1} | {key2} | {key3}\nYou win ${value2+value3}"

    else:
        lost=400
        update_data(f'{password}','-',f'{lost}')
        return f"{key1} | {key2} | {key3}\nYou lose"





# print(high_tier('3977'))
def test():
    num=0
    while True:
        # num=0
        key1,value1=random.choice(list(items.items()))
        key2,value2=random.choice(list(items.items()))
        key3,value3=random.choice(list(items.items()))
        arr=np.array([key1,key2,key3])
        # print(all(arr))
        if all(arr==key1):
            print('***JACKPOT***')
            print(arr,num)
            print(f"You win ${value1+value2+value3}")
            return f'***JACKPOT*** \n {arr} \n You win ${value1+value2+value3}'
            break

        else:
            # num+=1
            print(arr,num)
            num+=1


# test()