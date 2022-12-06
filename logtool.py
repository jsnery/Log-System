from datetime import datetime
from pathlib import Path

__all__ = ['LogPrint', 'LogFile']


DATE = datetime.now().strftime('%d-%m-%Y')
TIME = datetime.now().strftime('%H:%M:%S')
DIR = Path(__file__).parent / 'logs'
FILE = DIR  / f"log_{DATE}.txt"

class Log:
    
    def _logsys(self, msg, prefix):
        raise NotImplementedError('Log System not implemented')
    
    def log_Info(self, msg, prefix='logInfo'):
        return self._logsys(msg, prefix)
    
    
class LogPrint(Log):
    
    def _logsys(self, msg, prefix):
        print(f"{prefix}: {msg}")
    
class LogFile(Log):
    
    def _logsys(self, msg, prefix):
        if not DIR.exists():
            DIR.mkdir()
            
        with FILE.open('a') as file:
            file.write(f"({TIME}) {prefix} -> {msg}")



if __name__ == "__main__":
    l = LogFile()
    l.log_Info('Hi\n')
    l2 = LogPrint()
    l2.log_Info('Hi\n')
