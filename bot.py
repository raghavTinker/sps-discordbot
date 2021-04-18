from discord.ext import commands
import os
import asyncio
import random
import discord
from sps import computerChoose
from sps import writeExcelSheet

options = ["scissors", "paper", "stone"]
prefix = "&"
client = commands.Bot(command_prefix=prefix, case_insensitive=True)

user_score = 0
computer_score = 0

def compete(user, computer):
    global user_score
    global computer_score

    print("User choice: {}\tMy choice: {}".format(user, computer))

    #conditions where the user will win
    if(user == "scissors" and computer == "paper"):
        user_score = user_score + 1
        return "You won!"

    elif(user == "stone" and computer == "scissors"):
        user_score = user_score + 1
        return "You won!"

    elif(user == "paper" and computer == "stone"):
        user_score = user_score + 1
        return "You won!"
    #=============================================
    #conditions where the computer would win

    elif(user == "scissors" and computer == "stone"):
        computer_score = computer_score + 1
        return "I won!"
        
        
    elif(user == "paper" and computer == "scissors"):
        computer_score = computer_score + 1
        return "I won!"
        

    elif(user == "stone" and computer == "paper"):
        computer_score = computer_score + 1
        return "I won!"
        

    else:
        return "Its a draw!"

@client.command(name="ping")
async def _ping(ctx):
    await ctx.send(f"Ping: ```{client.latency}```")

@client.command(name="sayhello")
async def sayHello(ctx):
    await ctx.send("Hi! Please type in your name!")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    msg = await client.wait_for("message", check=check)
    await ctx.send("Hi " + msg.content + "!")
    print(msg.content)



@client.command(name="sps")
async def sps(ctx):
    global user_score
    global computer_score
    user_name = ""
    
    #Intro
    await ctx.send("Lets play stone paper scissor!!!")
    await ctx.send("Number of rounds?")

    #check if the answer is valid
    def check(rounds_str):
        return rounds_str.author == ctx.author and rounds_str.channel == ctx.channel
    
    rounds_str = await client.wait_for("message", check=check)
    
    #Storing username
    user_name = str(rounds_str.author).split('#')[0]

    rounds = 0
    try:
        rounds = int(rounds_str.content)
    except:
        await ctx.send("Enter a valid integer")
    
    count = 0
    user_score = 0
    computer_score = 0

    while count < rounds:
        await ctx.send("ROUND " + str(count + 1) + " \nEnter ```[stone, paper or scissors]```")

        def checkOption(option):
            return option.author == ctx.author and option.channel == ctx.channel
        
        option  = await client.wait_for("message", check=checkOption)

        computer_choice = computerChoose()

        if option.content in options:
            result = compete(option.content, computer_choice)
            await ctx.send("```Your choice: {}\n My choice: {}```\n{}".format(option.content, computer_choice, result))
            count = count + 1
        else:
            await ctx.send("Enter a valid option")
            await ctx.send("Retry!")
            pass
    
    await ctx.send("Competition over!")
    await ctx.send("SCOREBOARD")
    await ctx.send("```Your score = {}\nMy score = {}```".format(user_score, computer_score))
    writeExcelSheet(user_score, computer_score, user_name)

@client.command(name="sps_hist")
async def sps_histSend(ctx):
    await ctx.send("Here are all my game results till now")
    await ctx.send(file=discord.File("score.xlsx"))

client.run(os.getenv('TOKEN'))