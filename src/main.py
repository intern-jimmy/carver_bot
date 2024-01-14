import os
from dotenv import load_dotenv
from datetime import datetime, timezone
import calendar
import pprint
import json

from config import Config
from commands import Commands
from repeated_timer import RepeatedTimer
from carver import carverDataSet
from analysis import extractData
from messages import create_message
import discord
import twitter

config = None
timedEventLoop = None
previousData = {}
started = ''
checkCount = 0


def main():
    global timedEventLoop
    global started
    started = datetime.now().strftime("%H:%M:%S")
    print('Initializing configuration')
    setup_config()

    """ Generate the event loop """
    timedEventLoop = defineRepeater()

    while True:
        userInput = input("Enter command:\n").split(" ")
        command = userInput[0].upper()
        userInput.pop(0)
        args = userInput

        computeCommands(command, args)


def LogicalCheck():
    """
      1. query the chain to get the stone carvers away and working status
      2. extract data from that
      3. create message
      4. if message not empty send message
      5. save extracted data
    """
    global previousData
    global checkCount
    print("Starting Check: " + datetime.now().strftime("%H:%M:%S"))

    
    try:
        data = getCarverData()
        
        pastData = previousData

        extracted_data = extractData(data, pastData)
        print(extracted_data)

        onehourMessages = json.loads(config.get('bot', 'oneHourMessage'))
        #print(f"one hour message in {extracted_data['next_carver_area']}: {onehourMessages[extracted_data['next_carver_area']]}, debug: {config.get('bot', 'debug')}")

        response_data = create_message(extracted_data, onehourMessages == 'True', extracted_data['next_carver_area'], int(config.get('bot', 'interval')),  config.get('bot', 'debug') == 'True')

        if "oneHourMessage" in response_data:
            onehourMessages = response_data['oneHourMessage']
            config.set('bot', 'oneHourMessage', json.dumps(onehourMessages))

        if "interval" in response_data:
            config.set('bot', 'interval', str(response_data['interval']))
            #updateTime(int(response_data['interval']))

        previousData = extracted_data

        if response_data['message'] != None:
            if config.get('bot', 'sendTweets') == 'True': # and config.get('bot', 'debug') == 'False':

                twitter.sendTweet(config.get('tweepy', 'consumer_key'), config.get('tweepy', 'consumer_secret'), config.get('tweepy', 'access_token'), config.get('tweepy', 'access_token_secret'),,response_data['message'])
                

            if config.get('bot', 'sendDiscord') == 'True':
                discord.sendMessage(response_data['message'], config.get('Discord', 'url'))
        else:
            print('No message')
        #  discord.sendMessage('No Message', config.get('Discord', 'url'))
    except Exception as ex:
        print(ex)
        discord.sendMessage('Intern look at the bot: ' + str(ex))

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('check complete ' + current_time)
    checkCount = checkCount + 1


def setup_config():
    global config
    """ Get the base config file loaded"""
    config = Config()
    print(pprint.pprint(config.display()))
    """ Load the secret stuff into the config"""
    load_environment()


def load_environment():
    global config
    load_dotenv()
    """ Load data for Tweepy """
    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')

    config.addSection('tweepy')
    config.set('tweepy', 'consumer_key', consumer_key)
    config.set('tweepy', 'consumer_secret', consumer_secret)
    config.set('tweepy', 'access_token', access_token)
    config.set('tweepy', 'access_token_secret', access_token_secret)
    config.set('tweepy', 'client_id', client_id)
    config.set('tweepy', 'client_secret', client_secret)

    """ Load data for Discord """
    discordUrl = os.getenv('DISCORD_URL')

    config.addSection('Discord')
    config.set('Discord', 'url', discordUrl)


def defineRepeater():
    global config
    return RepeatedTimer(int(config.get('bot', 'interval')), LogicalCheck)


def updateTime(time):
    global timedEventLoop
    timedEventLoop.updateInterval(time)


def computeCommands(command, args):
    global config
    """ Process user input """
    if command == Commands.QUIT.name:
        quit()
    if command == Commands.HELP.name:
        help()
    if command == Commands.DEBUG.name:
        debug(args)
    if command == Commands.INTERVAL.name and len(args) == 0:
        displayInterval()
    if command == Commands.INTERVAL.name and len(args) == 1:
        print(args)
        config.set('bot', 'interval', args[0])
        updateTime(int(config.get('bot', 'interval')))

    if command == Commands.STATUS.name:
        displayStatus()


def getCarverData():
    global config
    result = {}
    
    # has to be a better way to deal with a list in a configfile...
    carverRealms = config.get('bot', 'carvers').replace('\'', '').replace('[', '').replace(']', '').replace(' ', '').replace('"', '')

    for carver_realm in carverRealms.split(','):
        # realm = carverRealm.strip()
        try:
            realm_carver_data = carverDataSet(config.get(carver_realm, 'rpc'), config.get(carver_realm, 'address'))
            result[carver_realm] = realm_carver_data
            
        except Exception as e:
            print('oops - ' + str(e))

    result['current_time'] = datetime.now(timezone.utc).timestamp()
    
    return result


def quit():
    global timedEventLoop
    timedEventLoop.stop()
    exit(0)


def help():
    print('exit -> stop the bot\ndebug -> Alerts the next cycle\nTodo: replace with a file')


def debug(args):
    """ Update the debug flag in the config o deplay it """
    global config
    if len(args) > 0:
        config.set('bot', 'debug', args[0])
    else:
        print(config.get('bot', 'debug'))


def displayInterval():
    global config
    print(config.get('bot', 'interval'))


def displayStatus():
    pp = pprint.PrettyPrinter(indent=4)
    global previousData
    global started
    global checkCount
    global config

    print('Start time: ' + started)
    print('Number of checks performed: ' + str(checkCount))
    print('previous data: ' + str(previousData))
    print('config:')
    pp.pprint(config.display())


if __name__ == '__main__':
    main()