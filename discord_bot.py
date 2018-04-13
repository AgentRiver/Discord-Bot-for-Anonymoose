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
    if "Hello" in message.content:
        await client.send_message(message.author, "Hello!")
    if "hello" in message.content:
        await client.send_message(message.author, "Hello!")
    if "Blame" in message.content:
        blameUsers = []
        blames = ["being Satan", "being blamed for", "burning down a building", "whatever Leyham did", "deleting System32", "the sky falling", "...", "not voting for Donald Trump", "smashing a window", "eating McDonalds", "blowing up the moon", "the moon landing being fake", "Leyham losing his game! GRRRR", "stabbing people", "handing out knifes to kids", "being too happy", "speling this wroong", "crashing a bus", "playing Fortnite", "staying up past their bedtime", "being too small", "being too big", "writing looooooooooooooooooong words", "writing", "MURDER", "not murdering someone", "spreading juicy leaks", "eating juicy leaks", "making up fake juicy leaks", "being a meme", "not being as *cool* as freddie", "dumping plastic in the ocean", "making a water level", "enjoying sports", "making WATCHMOJO PROPAGANDA", "bloatware", "viruses", "pretending to listen", "mass producing babies", "being a screaming child", "dead", "paying for WinRAR", "still making We are Number One Memes", "being a dead meme", "liking memes that are already dead", "playing *Mario Tennis*", "putting mushrooms on pizza", "not having cheese in a cheese sandwich", "liking Tetris (please don't leave Leyham, it was a mistake)", "being a mistake"]
        x = message.server.members
        for member in x:
            #print(member.name)
            blameUsers.append(member)
        #print(blameUsers)
        #print(len(blames))
        await client.send_message(message.channel, blameUsers[ random.randint( 0,len(blameUsers)-1 ) ].mention + " is being blamed for " + blames[ random.randint( 0,len(blames)-1 ) ])
   
## 1 - Annoy Leyham!
##tetris_banned_words = ['tetris', 'tetriS', 'tetrIs', 'tetrIS', 'tetRis', 'tetRiS', 'tetRIs', 'tetRIS', 'teTris', 'teTriS', 'teTrIs', 'teTrIS', 'teTRis', 'teTRiS', 'teTRIs', 'teTRIS', 'tEtris', 'tEtriS', 'tEtrIs', 'tEtrIS', 'tEtRis', 'tEtRiS', 'tEtRIs', 'tEtRIS', 'tETris', 'tETriS', 'tETrIs', 'tETrIS', 'tETRis', 'tETRiS', 'tETRIs', 'tETRIS', 'Tetris', 'TetriS', 'TetrIs', 'TetrIS', 'TetRis', 'TetRiS', 'TetRIs', 'TetRIS', 'TeTris', 'TeTriS', 'TeTrIs', 'TeTrIS', 'TeTRis', 'TeTRiS', 'TeTRIs', 'TeTRIS', 'TEtris', 'TEtriS', 'TEtrIs', 'TEtrIS', 'TEtRis', 'TEtRiS', 'TEtRIs', 'TEtRIS', 'TETris', 'TETriS', 'TETrIs', 'TETrIS', 'TETRis', 'TETRiS', 'TETRIs', 'TETRIS']
##    elif tetris_banned_words in message.content:
##        await client.delete_message(message)
            
## 2 - 10% Destruction
##random = random.randint(1,10)
##if random == 1:
##    await client.delete_message(message)

## 3 - Nickname Change
##await client.change_nickname(message.author, message.content)

## 4 -  0.1% Kick
## random = random.randint(1,1000)
## if random == 1:
##    await client.kick(message.author)



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
