import discord
import random

TOKEN = 'NDMwODI3NjU1NjMwNDIyMDI4.DlnNTA.NNEec_7dxQ88SvVDuMw_vBsjlJE'

hello = ["Hello", "hello", "Hi", "hi", "Hey", "hey"]
east_is_up = ["East is up", "East", "West", "Down", "Up", "east is up", "east",
              "west", "down", "up", "21", "nine", "escape", "dema", "DEMA", "bishops",
              "Bishops", "prison", "Prison", "Die", "die", "DIE"]
yes = ["yes", "Yes", "YES"]
no = ["no", "No", "NO"]
menu = ["Menu", "menu", "MENU"]
menu_items = ["Slurp Juice", "Bean", "Broad Bean", "Running Bean", "Beans on toast", "Mr Bean", "Killer Bean",
              "Smol Killer Bean", "Octonauts, Skoot", "Flex Tape", "Hello Dave, Your My Wife Now", "Flex Glue"
              "Skittles", "Dead Bodies"]

,client = discord.Client()
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if hello in message.content:
        await client.send_message(message.author, "Hello!")
    if "@everyone" in message.content:
        for i in range(1,4):
            await client.send_message(message.channel, "@everyone")
    if east_is_up in message.content:
        for i in range(1,4):
            await client.send_message(message.channel, "East is up")
    if yes in message.content:
        await client.send_message(message.channel, no[random.randint(0,2)])
    if no in message.content:
        await client.send_message(message.channel, yes[random.randint(0,2)])
    if menu in message.content:
        msg = "Menu = "
        for i in range(0, len(menu_items)):
            msg = msg + menu_items[i] + ", "
        await client.send_message(message.channel, msg)
                                  
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
