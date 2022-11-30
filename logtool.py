from datetime import datetime
from os import path, makedirs

name = None

def logAppend(log):
    global name
    fullDateTime = datetime.now().strftime('%d-%m-%Y %H-%M-%S')
    msg = f'({fullDateTime}) Info -> {log}\n'
    
    if name is None:
        name = logName()
            
    with open(name, 'a') as logCreate:
        logCreate.write(msg)


def logName(dir='./logs/'):
    if not path.isdir(dir):
        makedirs(dir)
    logInfoName = datetime.now().strftime('logInfo_%d-%m-%Y_%H-%M-%S')
    return f'{dir}{logInfoName}.txt'