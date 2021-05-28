# Stone paper scissors Discord bot

## Setup steps:
    a)install dependencies mentioned in requirements.txt
    b)create a bot/app in the discord developer platform
    c)get the token from the platform
    d)add the TOKEN environment variable: $export TOKEN="YOUR TOKEN"
    e)use the OAuth2 link and add add the bot to your discord server
    f)run the bot.py file
    
    Note: To change the prefix from & to any other character create a the PREFIX environment variable
        &export PREFIX='char'

## Execution:
    python3 bot.py

### File significance
    a)bot.py => contains all the command related functionality of the bot
    b)sps.py => Some functions specific for stone paper scissors are kept here
    c)score.xlsx => a file that records all the game scores 

### Bot commands:

`&sps` starts a game of stone paper scissors<br>
`&sps_hist` excel file of all the games played by the bot<br>
`&ping` ping in ms with the bot

Please note if you have changed the prefix then use your respective character.


### Its avaialable on Docker now!
  https://hub.docker.com/repository/docker/raghavtinker/spsdiscordbot#
