import discord
import random

TOKEN = 'NDMwODI3NjU1NjMwNDIyMDI4.DaV6Cg.HKshLmVmZe3pxaK0zadCqRfzO30'

client = discord.Client()
anti_spam = 'Hello'

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('ping'):
        msg = 'pong!'.format(message)
        await client.send_message(message.channel, msg)
    if "@River's Dinosaur#6154" in message.content:
        await client.send_message(message.channel, "DON'T BOTHER ME, LEAVE ME ALONE! GO ANNOY SOMEONE ELSE @everyone
    if message.content.startswith('dead'):
        msg = 'YOU ARE DEAD!'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('HAIL'):
        msg = 'HAIL THE OCTOPUS'.format(message)
        await client.send_message(message.channel, msg)
        await client.send_message(message.channel, msg)
        await client.send_message(message.channel, msg)
    if message.content.startswith('random'):
        msg = random.randint(1,1000000000000000000000000000000000000000000000000000000)
        await client.send_message(message.channel, msg)
    if message.content.startswith('ROCK'):
        rpsGame = random.randint(1,3)
        #print(rpsGame)
        if rpsGame == 1:
            await client.send_message(message.channel, "ROCK VS ROCK - DRAW")
        if rpsGame == 2:
            await client.send_message(message.channel, "ROCK VS SCISSORS - WIN")
        if rpsGame == 3:
            await client.send_message(message.channel, "ROCK VS PAPER - LOSE")
    if message.content.startswith('PAPER'):
        rpsGame = random.randint(1,3)
        #print(rpsGame)
        if rpsGame == 1:
            await client.send_message(message.channel, "PAPER VS ROCK - WIN")
        if rpsGame == 2:
            await client.send_message(message.channel, "PAPER VS SCISSORS - LOSE")
        if rpsGame == 3:
            await client.send_message(message.channel, "PAPER VS PAPER - DRAW")
    if message.content.startswith('SCISSORS'):
        rpsGame = random.randint(1,3)
        #print(rpsGame)
        if rpsGame == 1:
            await client.send_message(message.channel, "SCISSORS VS ROCK - LOSE")
        if rpsGame == 2:
            await client.send_message(message.channel, "SCISSORS VS SCISSORS - DRAW")
        if rpsGame == 3:
            await client.send_message(message.channel, "SCISSORS VS PAPER - WIN")
    if "Bleach" in message.content:
        for x in client.get_all_emojis():
            if x.id == '367746698639835140':
                return await client.add_reaction(message, x)
    if "bleach" in message.content:
        for x in client.get_all_emojis():
            if x.id == '367746698639835140':
                return await client.add_reaction(message, x)
    if "BLEACH" in message.content:
        for x in client.get_all_emojis():
            if x.id == '367746698639835140':
                return await client.add_reaction(message, x)
    

##    elif 'Tetris' in message.content:
##        await client.delete_message(message)
##    elif 'tetris' in message.content:
##        await client.delete_message(message)
##    elif 'TETRIS' in message.content:
##        await client.delete_message(message)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)


#1 ROCK
#2 SCISSORS
#3 PAPER
