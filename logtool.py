from datetime import datetime
from os import path, makedirs

dirLog = None

def logAppend(log):
    global dirLog
    fullDateTime = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
    msg = f'({fullDateTime}) Info -> {log}\n'
    
    def logName(dir='./logs/'):
        if not path.isdir(dir):
            makedirs(dir)
        logInfoName = f'logInfo_{fullDateTime}'
        return f'{dir}{logInfoName}.txt'
    
    if dirLog is None:
        dirLog = logName()
            
    with open(dirLog, 'a') as logCreate:
        logCreate.write(msg)
