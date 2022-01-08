import discord
from dotenv import load_dotenv
import os
import random
from slots import *
from MyDB import *
from blackjack import *
from test_table import *


##docs##
#https://discordpy.readthedocs.io/en/latest/api.html
#dev portal (make a bot)

##needs intents to check member status's like when joining/leaving server...
intents = discord.Intents.default()
intents.members = True
client=discord.Client(intents=intents)

load_dotenv()

@client.event
async def on_ready():
    #on startup says (bot name) is here-means code is working
    print(f"{client.user} is here")




@client.event
async def on_message(message):
    global dealer_draw_count,game_on

    #detect if someone says (.hello) in any channel
    if message.content=='.hello':
        await message.channel.send(f'hello {message.author}')
    
    #differentiate between channels
    if message.channel.name=='general':
        print('message in general')

    #ignore this person messages
    if message.author.name!='SecondAccount':
        pass

    ##for setting up personal commands
    if message.author.name=='Enemy of my Enemy' and message.author.discriminator=='3977':
        print("\nmessage details:")
        print(message)
        print("\nmessage content:")
        print(f"{message.content} \n")
        my_message=message.content.lower().split(' ')
        print("message after split:")
        print(my_message)

        ##add a user to db
        if my_message[0]=='.create':
            try:
                insert_user(f"{my_message[1]}",f"{my_message[2]}")
            except:
                await message.channel.send('To create a user you need a username and discriminator id (4 digit code on profile)')

        ##Show all the intries in db
        if my_message[0]=='.show_db':
            await message.channel.send(show_entries('Discord_db'))

        if my_message[0]=='.balance':
            await message.channel.send(show_balance(f'{message.author.discriminator}'))

        ##delete a user from db
        if my_message[0]=='.delete_user':
            try:
                delete_user(f"{my_message[1]}",f"{my_message[2]}")
            except:
                await message.channel.send('check the username and discriminator id')

        #give away money
        if my_message[0]=='.gift':
            try:
                update_data(f"{my_message[1]}","+",f"{my_message[2]}")
            except:
                await message.channel.send('to gift money need password(4 numbers of id) and how much money you wish to gift')


        ##take away money
        if my_message[0]=='.take_away':
            try:
                update_data(f"{my_message[1]}","-",f"{my_message[2]}")
            except:
                await message.channel.send('to keep order you need username and how much money to take away')

    ##public commands (games and stuff)
    my_message=message.content.lower().split(' ')


    if my_message[0]=='.slot':
        if len(my_message)>1:
            if my_message[1]=='high':
                if balance_check(f"{message.author.discriminator}") == True:
                    await message.channel.send('We got a high roller today huh:')
                    await message.channel.send(high_tier(f'{message.author.discriminator}'))
                
                else:
                    await message.channel.send('You dont have enough money for high roller table')

            if my_message[1]=='low':
                await message.channel.send('You chose the low tier table:')
                await message.channel.send(low_tier(f'{message.author.discriminator}'))

        else:
            await message.channel.send('Choose between low or high tier table (Ex. (.slot high))')


        
    if my_message[0]=='.gift': ##Ex. (.gift 3977 1000)
        try:
            print(message.content)
            update_data(f'{message.author.discriminator}', '-', f'{my_message[2]}')
            update_data(f"{my_message[1]}","+",f"{my_message[2]}")
            await message.channel.send(show_balance(f'{message.author.discriminator}'))
        except:
            await message.channel.send('to gift money need password(4 numbers of id) and how much money you wish to gift')

    if my_message[0]=='.balance':
        await message.channel.send(show_balance(f'{message.author.discriminator}'))



    if my_message[0]=='.sit':
        add(message.author)



    if my_message[0]=='.bj':
        game_on=True
        deal_cards(dict_[message.author]['player hand'],dict_[message.author]['dealer hand'],dict_[message.author]['player hand count'],dict_[message.author]['dealer hand count'])
        
        await message.channel.send('Dealer has:')
        for card in show_hand(dict_[message.author]['dealer hand'],dict_[message.author]['dealer hand count'],'Dealer'):
            await message.channel.send(f"-{card}")
        await message.channel.send(get_hand_total(dict_[message.author]['dealer hand count'],'Dealer'))

        await message.channel.send('-'*20)

        await message.channel.send('Player has:')
        for card in show_hand(dict_[message.author]['player hand'],dict_[message.author]['player hand count'],'Player'):
            await message.channel.send(f"-{card}")
        await message.channel.send(get_hand_total(dict_[message.author]['player hand count'],'Player'))


    if my_message[0]=='.hit':
        if game_on==True:
            hit(dict_[message.author]['player hand'],dict_[message.author]['player hand count'])
            dealer_draw_count+=1

            await message.channel.send('Dealer has:')
            for card in show_hand(dict_[message.author]['dealer hand'],dict_[message.author]['dealer hand count'],'Dealer'):
                await message.channel.send(f"-{card}")
            await message.channel.send(get_hand_total(dict_[message.author]['dealer hand count'],'Dealer'))

            await message.channel.send('-'*20)

            await message.channel.send('Player has:')
            for card in show_hand(dict_[message.author]['player hand'],dict_[message.author]['player hand count'],'Player'):
                await message.channel.send(f"-{card}")
            await message.channel.send(get_hand_total(dict_[message.author]['player hand count'],'Player'))

        else:
            await message.channel.send('You need to start the game using (.bj) command')

    if my_message[0]=='.stand':
        if game_on==True:

            dict_[message.author]['dealer hand'].pop(0)
            card=deck.pop()
            dict_[message.author]['dealer hand'].append(card.card)
            dict_[message.author]['dealer hand count'].append(card.value)

            for i in range(dealer_draw_count):
                hit(dict_[message.author]['dealer hand'],dict_[message.author]['dealer hand count'])


            await message.channel.send('Dealer has:')
            for card in show_hand(dict_[message.author]['dealer hand'],dict_[message.author]['dealer hand count'],'Dealer'):
                await message.channel.send(f"-{card}")
            await message.channel.send(get_hand_total(dict_[message.author]['dealer hand count'],'Dealer'))

            await message.channel.send('-'*20)

            await message.channel.send('Player has:')
            for card in show_hand(dict_[message.author]['player hand'],dict_[message.author]['player hand count'],'Player'):
                await message.channel.send(f"-{card}")
            await message.channel.send(get_hand_total(dict_[message.author]['player hand count'],'Player'))


            await message.channel.send(stand(dict_[message.author]['dealer hand'],dict_[message.author]['player hand'],dict_[message.author]['dealer hand count'],dict_[message.author]['player hand count']))

            dict_[message.author]['dealer hand']=[]
            dict_[message.author]['player hand']=[]
            dict_[message.author]['dealer hand count']=[]
            dict_[message.author]['player hand count']=[]





@client.event
async def on_member_join(member):
    print(member)
    print(f"{member} joins the frey")
    insert_user(f'{member.name}',f'{member.discriminator}')
    await member.send(f"Welcome to the Server")



@client.event
async def on_member_remove(member):
    print(member)
    print(f"{member} has left the server")
    
    delete_user(f"{member.name}",f"{member.discriminator}")



client.run(os.getenv('discord_token'))
