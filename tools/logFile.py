from datetime import datetime
from os import path, mkdir

def logAppend(error):
    fullDateTime = datetime.now().strftime('%d-%m-%Y %H-%M-%S')
    msg = f'({fullDateTime}) {error}\n'
    log.write(msg)

def logName():
    if not path.isdir('./logs/'):
        mkdir('./logs/')
    logInfoName = datetime.now().strftime('logInfo_%d-%m-%Y_%H-%M-%S')
    return f'./logs/{logInfoName}.txt'

log = open(logName(), 'a')