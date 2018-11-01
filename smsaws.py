#!/usr/bin/env python
# encoding: utf-8
"""
Created by Paulino Rocha e Silva on 2017-05-23.
Copyright (c) 2017 neoplace. All rights reserved.

Script para envio de mensagens pelo SNS - AWS
"""
import sys
# adicionando o diretorio em runtime
sys.path.insert(0, './credenciais')
# importando as credenciais da AWS
import aws_credentials as credenciais
import boto3

chave = credenciais

lista_telefones = []

def envia_sms(telefones,mensagem):
	# Abre o arquivo de log ou cria se não existir
	f = open("smsaws.log","a+")
	f.write("mensagem: %s \r\n" % mensagem)

	# Cria o cliente para o AWS SNS
	sns = boto3.client(
		"sns",
		aws_access_key_id = chave.aws_access,
		aws_secret_access_key = chave.aws_secret,
		region_name = chave.region
		)

	# Envia a mensagem para lista de telefones fornecida 
	for telefone in telefones:
		print("enviando para %s -  mensagem: %s | OK" %(telefone, mensagem))
		response = sns.publish(
			PhoneNumber = telefone,
			Message = mensagem,
			)
		f.write("dados de envio para %s: \n %s \r\n" %(telefone, response))

	print("------- \n foram enviadas %d mensagens com sucesso \r\n" %(len(telefones)))
	print('relatorios de envio em smsaws.log \n')
	f.close()

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
	if  len(sys.argv) < 3 :
		print("\n")
		print("Coloque o numero de celular no formato +5541999999962 e 'mensagem de texto' entre aspas ")
		print("Você pode colocar vários números antes da mensagem. Ex: python smsaws.py +55419999999 'mensagem' \n")
	else:
		mensagem(sys.argv)

if __name__ == '__main__':
	main()
