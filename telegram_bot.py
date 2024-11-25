#############################################################################
# Autor: Luis Olavo Garrido                                                 #
# E-Mail: sgtgarrido3rm@gmail.com                                           #
# Data: 2024nov24                                                           #
# Instituição: Cruzeiro do Sul Virtual (Universidade Positivo)              #
# Disciplina: Atividades de Extensão - Integração de Competências em IA II  #
# https://github.com/sgtgarrido3rm/querenciasaude                           #
#############################################################################

# importação da biblioteca do telegram
import telebot

# token exclusivo gerado pelo bot do telegram para conectar ao Telegram
CHAVE_API = "7912655832:AAEgz6ntlEq3iSBfF_cfQsLR_Dq5do9AzOo"

# objeto que conecta ao telegram com o uso da cheve
bot = telebot.TeleBot(CHAVE_API)

### INÍCIO FUNÇÕES SECUNDÁRIAS ###
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
### FIM FUNÇÕES SECUNDÁRIAS ###

# função retorna verdadeiro sempre, porque deve ser executada a função [responder] independente do que for digitado
def verificar(mensagem):
    return True

# decorator que pega a mensagem do [bot.polling()] e após receber [True] libera para chamar a função [responder]
@bot.message_handler(func=verificar)
# função padrão do chatbot
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
     /febre O que fazer em caso de febre?
     /pressao O que fazer em caso de pressão alta/baixa?
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)

# deixa o código em loop para que fique sempre ativo o chatbot
bot.polling()