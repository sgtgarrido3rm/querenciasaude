import telebot

CHAVE_API = "7912655832:AAEgz6ntlEq3iSBfF_cfQsLR_Dq5do9AzOo"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["baixa"])
def baixa(mensagem):
    texto = """
    O que fazer em caso de pressão baixa?
    - Deite-se e eleve as pernas
    - Beba líquidos
    - Faça um pequeno lanche
    - Levante-se lentamente
    - Consulte um médico

    Clique aqui para voltar ao menu: /voltar"""

    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["alta"])
def alta(mensagem):
    texto = """
    O que fazer em caso de pressão alta?
    - Medir a pressão arterial
    - Relaxar e descansar
    - Evitar alimentos que elevem a pressão
    - Tomar a medicação prescrita (se for o caso)
    - Procurar ajuda médica imediata

    Clique aqui para voltar ao menu: /voltar"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["febre"])
def opcao1(mensagem):
    texto = """
    O que fazer em caso de febre alta?
    - Medicar (com orientação médica): com antitérmicos como paracetamol ou ibuprofeno para aliviar a febre e o desconforto
    - Evite automedicação, especialmente em crianças, gestantes ou pessoas com condições pré-existentes"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["pressao"])
def pressao(mensagem):
    texto = """
    Escolher Alta ou Baixa (Clique em uma opção):
    /alta Alta
    /baixa Baixa"""
    bot.send_message(mensagem.chat.id, texto)


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
     /febre O que fazer em caso de febre?
     /pressao O que fazer em caso de pressão alta/baixa?
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)

bot.polling()