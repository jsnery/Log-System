# Sistema de Log
 First attempt to create a log system. Simple and practical system, for error register in log. There must be a better solution, but this was made by myself.

 I'm satisfied for that starter project.

 - logName()

 This role is responsible for two processes. First it looks for the logs folder, if it doesn't exist it creates it. Then it creates the name of the **.txt** log file, it uses the:
 ```
 >>> datetime.now().strftime("logInfo_%d-%m-%Y_%H-%M-%S")
 ```
 After that it creates the file using the **open()** function.

 - logAppend(error)

 basically responsible for writing the content of the log accompanied by the error data inside the **.txt** file.
 ```
 >>> logAppend(‘Fatal Error’)

 in the file is written: (27-11-2022 22-46-47) Fatal error
 ```
 ### additional

- clear()

Serves to clean the console, works with MAC, Linux and Windows.