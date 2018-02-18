#!/usr/bin/python
import telepot, time


def handle(msg):

	list userName = ['ana','anne','derick']

	content_type, chat_type, chat_id = telepot.glance(msg)

	if (content_type == 'text'):
		command = msg['text']
		print ('Got command: %s' % command)

	if userName in command:
		bot.sendMessage(chat_id, "Ola "+userName+ ", Seja bem vindo a nossa nova sede, para entrar conecte-se à rede wifi da Acception.")
	

	if '/open' in command:
		bot.sendMessage(chat_id, "Tranca aberta, "+userName+" entrando.")


	
bot = telepot.Bot('token')

# Adiciona a função hanldle para ser chamada sempre que uma nova mensagem for recebida
bot.message_loop(handle)

while 1:
	time.sleep(20)
