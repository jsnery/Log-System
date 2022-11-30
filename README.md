# Logging System in Python
First attempt to create a Logging System. Simple and practical system, for error register. There must be a better solution, but this was made by myself.

I'm satisfied for that starter project.

### • logName(_dir='./logs/'_)

This role is responsible for two processes. First it looks for the logs folder, if it doesn't exist it creates it. Then it creates the name of the **.txt** logging file, it uses the:
```
>>> datetime.now().strftime("logInfo_%d-%m-%Y_%H-%M-%S")
```
    
After that it creates the file using the **open()** function.

### • logAppend(_log_)

**This is what you will actually use**. Basically responsible for writing the log content together with the error data inside the **.txt** file.
```
>>> logAppend(‘Fatal Error’)

in the file is written: (27-11-2022 22-46-47) Info -> Fatal error
```
### Implementation

I implemented the log system in a small registration and login system for its demonstration, follow the link below:

Click Here [[Login-Registration-System]](https://github.com/jsnery/Login-Registration-System)