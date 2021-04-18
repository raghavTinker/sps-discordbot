# Stone paper scissors Discord bot

## Setup steps:
    a)install dependencies mentioned in requirements.txt
    b)create a bot/app in the discord developer platform
    c)get the token from the platform and add it to a new file called `.env`
    d)use the OAuth2 link and add it to your discord server
    e)run the bot.py file

### File significance
    a)bot.py => contains all the command related functionality of the bot
    b)sps.py => Some functions specific for stone paper scissors are kept here
    c)score.xlsx => a file that records all the game scores 

### Bot commands:

`&sps` starts a game of stone paper scissors<br>
`&sps_hist` excel file of all the games played by the bot<br>
`&ping` ping in ms with the bot