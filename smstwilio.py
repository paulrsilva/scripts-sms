#!/usr/bin/env python
# encoding: utf-8
"""
Created by Paulino Rocha e Silva on 2017-05-23.
Copyright (c) 2017 neoplace. All rights reserved.

Testes para envio de mensagens pelo Twillio
"""
import sys
#adicionando o diretorio em runtime
sys.path.insert(0, './credenciais')
# importanto credenciais de um diretorio no .gitignore
import twilio_credentials as credenciais

from twilio.rest import Client

chave = credenciais

# Credenciais de teste
test_account = chave.test_account
test_token = chave.test_token
test_number = chave.numeros_teste[2]

# Credenciais Live
account = chave.account
token = chave.token
twilio_number = chave.numeros_twilio[0]

client = Client(account,token)

lista_telefones=[]

def envia_sms(telefones,mensagem):
	for telefone in telefones:
		print("enviando para %s -  mensagem: %s | OK" %(telefone, mensagem))
		message = client.messages.create(to=telefone, from_=twilio_number, body=mensagem)
	print("------- \n foram enviadas %d mensagens com sucesso \n" %(len(telefones)))
	print(message.sid)

def mensagem(*args):
	x=0
	#elemento-1 é o numero de telefones antes da msg
	# 0 indice 0 tem o nome do programa passado pelo argsv do script
	# o ultimo argumento passado é a mensagem
	for elemento in args:
		for argumento in elemento:
			# Pegando os números e telefone para envio
			if (x > 0 and x < (len(elemento)-1)):
				lista_telefones.append(argumento)
			x += 1

    # Pega a mensagem, que é o penultimo numero de x
    # (o índice começa em 0)
	msg_sms = args[0][x-1]

	envia_sms(lista_telefones, msg_sms)


def main():
	#message = client.messages.create(to="+5541992099962", from_="+12077473005", body="teste Python local!")
	# print("This is the name of the script: ", sys.argv[0])
	# print( "Number of arguments: ", len(sys.argv))
	# print("The arguments are: " , str(sys.argv))
	# print(type(sys.argv[1]))
	# for i in range(len(sys.argv)):
	# 	print(sys.argv[i])
	# print(type(sys.argv))


	if  len(sys.argv) < 3 :
		print("\n")
		print("Coloque o numero de celular no formato +5541999999962 e 'mensagem de texto' entre aspas ")
		print("Você pode colocar vários números antes da mensagem. Ex: python testesms.py +55419999999 'mensagem' \n")
	else:
		mensagem(sys.argv)




if __name__=='__main__':
	main()