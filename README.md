# Sistema de Log
 Primeira tentativa de criar um sistema de log.
 
 Sistema simples e prático, para logs simples. Deve ter solução melhor, mas essa foi a minha.

 Estou Satisfeito para um projeto inicial.

 - logName()
 Essa função é responsável por dois processos. Primeiro ela procura pela pasta de logs, caso a mesma não exista ela a cria. Em seguida ela cria o nome do arquivo .txt de log , ele utiliza a função datetime.now().strftime(logInfo_%d-%m-%Y_%H-%M-%S), dessa forma forta nome, data e hora ao mesmo tempo. Após isso ele cria o arquivo utilizando a função open().

 - logAppend(error)
 Basicamente responsável por escrever o conteúdo do log acompanhado de data dentro do arquivo .txt. 

'''
logAppend(‘Fatal Error’)
'''
(27-11-2022 22-46-47) Fatal error