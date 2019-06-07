import telepot
import json
from telepot.namedtuple import ForceReply, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

load = open("token.json")   # Lendo o Json que contém o token do bot
token = json.loads(load.read()) # Inserindo o token bot a variavel "token"
bot = telepot.Bot(token['token'])   # Inserindo o token no Bot

'''SOBRE: condicoes
Pega o a interacao do usuario (via mensagem ou botao), e faz alguma tomada de acao
'''
def condicoes(chatID, msg):
            if(msg == '/start'):
                    inicio(chatID, bot)

############################### HORÁRIO ###############################
            elif(msg == 'Horário'):
                    bot.sendMessage(
                        chatID,
                        "Escolha o curso",
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Análise e Desenvolvimento de Sistemas", callback_data='ADS')],
                                [InlineKeyboardButton(text="Automação e Manufatura Digital", callback_data='AMD')],
                                [InlineKeyboardButton(text="Banco de Dados", callback_data='BD')],
                                [InlineKeyboardButton(text="Gestão de Produção Industrial", callback_data='GPI')],
                                [InlineKeyboardButton(text="Logística(Manhã)", callback_data='LOGMA')],
                                [InlineKeyboardButton(text="Logística(Noite)", callback_data='LOGNO')],
                                [InlineKeyboardButton(text="Manufatura Avançada", callback_data='MAVAN')],
                                [InlineKeyboardButton(text="Manutenção de Aeronaves", callback_data='MAERO')],
                                [InlineKeyboardButton(text="Projetos de Estruturas Aeronáuticas", callback_data='PEA')]
                                
                            ]
                        )
                    )
          
            elif(msg == 'ADS'):
                    bot.sendMessage(
                        chatID,
                        'Qual o semestre que você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="1° Semestre", callback_data='1SEMADS')],
                                [InlineKeyboardButton(text="2° Semestre", callback_data='2SEMADS')],
                                [InlineKeyboardButton(text="3° Semestre", callback_data='3SEMADS')],
                                [InlineKeyboardButton(text="4° Semestre", callback_data='4SEMADS')],
                                [InlineKeyboardButton(text="5° Semestre", callback_data='5SEMADS')],
                                [InlineKeyboardButton(text="6° Semestre", callback_data='6SEMADS')]
                            ]
                        )
                    )
                    
            elif(msg == 'AMD'):
                    bot.sendMessage(
                        chatID,
                        'Qual o semestre que você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="4° Semestre", callback_data='4SEMAMD')],
                                [InlineKeyboardButton(text="5° Semestre", callback_data='5SEMAMD')],
                                [InlineKeyboardButton(text="6° Semestre", callback_data='6SEMAMD')]
                            ]
                        )
                    )
                    
            elif(msg == 'BD'):
                    bot.sendMessage(
                        chatID,
                        'Qual o semestre que você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="1° Semestre", callback_data='1SEMBD')],
                                [InlineKeyboardButton(text="2° Semestre", callback_data='2SEMBD')],
                                [InlineKeyboardButton(text="3° Semestre", callback_data='3SEMBD')],
                                [InlineKeyboardButton(text="4° Semestre", callback_data='4SEMBD')],
                                [InlineKeyboardButton(text="5° Semestre", callback_data='5SEMBD')],
                                [InlineKeyboardButton(text="6° Semestre", callback_data='6SEMBD')]
                            ]
                        )
                    )
            elif(msg == 'GPI'):
                    bot.sendMessage(
                        chatID,
                        'Qual o semestre que você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="1° Semestre", callback_data='1SEMGPI')],
                                [InlineKeyboardButton(text="2° Semestre", callback_data='2SEMGPI')],
                                [InlineKeyboardButton(text="3° Semestre", callback_data='3SEMGPI')],
                                [InlineKeyboardButton(text="4° Semestre", callback_data='4SEMGPI')],
                                [InlineKeyboardButton(text="5° Semestre", callback_data='5SEMGPI')],
                                [InlineKeyboardButton(text="6° Semestre", callback_data='6SEMGPI')]
                            ]
                        )
                    )
            elif(msg == 'LOGMA'):
                    bot.sendMessage(
                        chatID,
                        'Qual o semestre que você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="1° Semestre", callback_data='1SEMLOGMA')],
                                [InlineKeyboardButton(text="2° Semestre", callback_data='2SEMLOGMA')],
                                [InlineKeyboardButton(text="3° Semestre", callback_data='3SEMLOGMA')],
                                [InlineKeyboardButton(text="4° Semestre", callback_data='4SEMLOGMA')],
                                [InlineKeyboardButton(text="5° Semestre", callback_data='5SEMLOGMA')],
                                [InlineKeyboardButton(text="6° Semestre", callback_data='6SEMLOGMA')]
                            ]
                        )
                    )


            elif(msg == 'LOGNO'):
                    bot.sendMessage(
                        chatID,
                        'Qual o semestre que você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="1° Semestre", callback_data='1SEMLOGNO')],
                                [InlineKeyboardButton(text="2° Semestre", callback_data='2SEMLOGNO')],
                                [InlineKeyboardButton(text="3° Semestre", callback_data='3SEMLOGNO')],
                                [InlineKeyboardButton(text="4° Semestre", callback_data='4SEMLOGNO')],
                                [InlineKeyboardButton(text="5° Semestre", callback_data='5SEMLOGNO')],
                                [InlineKeyboardButton(text="6° Semestre", callback_data='6SEMLOGNO')]
                            ]
                        )
                    )
                    

            elif(msg == 'MAERO'):
                    bot.sendMessage(
                        chatID,
                        'Qual o semestre que você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="1° Semestre", callback_data='1SEMMAERO')],
                                [InlineKeyboardButton(text="2° Semestre", callback_data='2SEMMAERO')],
                                [InlineKeyboardButton(text="3° Semestre", callback_data='3SEMMAERO')],
                                [InlineKeyboardButton(text="4° Semestre", callback_data='4SEMMAERO')],
                                [InlineKeyboardButton(text="5° Semestre", callback_data='5SEMMAERO')],
                                [InlineKeyboardButton(text="6° Semestre", callback_data='6SEMMAERO')]
                            ]
                        )
                    )
                    
            elif(msg == 'MAVAN'):
                    bot.sendMessage(
                        chatID,
                        'Qual o semestre que você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="1° Semestre", callback_data='1SEMMAVAN')],
                                [InlineKeyboardButton(text="2° Semestre", callback_data='2SEMMAVAN')],
                                [InlineKeyboardButton(text="3° Semestre", callback_data='3SEMMAVAN')]
                            ]
                        )
                    )
                    
            elif(msg == 'PEA'):
                    bot.sendMessage(
                        chatID,
                        'Qual o semestre que você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="1° Semestre", callback_data='1SEMPEA')],
                                [InlineKeyboardButton(text="2° Semestre", callback_data='2SEMPEA')],
                                [InlineKeyboardButton(text="3° Semestre", callback_data='3SEMPEA')],
                                [InlineKeyboardButton(text="4° Semestre", callback_data='4SEMPEA')],
                                [InlineKeyboardButton(text="5° Semestre", callback_data='5SEMPEA')],
                                [InlineKeyboardButton(text="6° Semestre", callback_data='6SEMPEA')]
                            ]
                        )
                    )
            

############################### 1 SEMESTRE ADS ###############################                   

            elif(msg == '1SEMADS'):
                    bot.sendMessage(
                        chatID,
                        'Qual turma você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Turma A", callback_data='1SEMTurmaA')],
                                [InlineKeyboardButton(text="Turma B", callback_data='1SEMTurmaB')]
                            ]
                        )
                    ) 
            elif(msg == '1SEMTurmaA'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegAds1A')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerAds1A')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaAds1A')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiAds1A')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexAds1A')],
                            ]
                        )
                    )
            
            elif(msg == '1SEMTurmaB'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegAds1B')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerAds1B')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaAds1B')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiAds1B')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexAds1B')],
                            ]
                        )
                    )
                 

            elif(msg == 'SegAds1A'):
                    txt = open('Horario/ADS/1Semestre/TurmaA/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerAds1A'):
                    txt = open('Horario/ADS/1Semestre/TurmaA/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaAds1A'):
                   txt = open('Horario/ADS/1Semestre/TurmaA/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiAds1A'):
                   txt = open('Horario/ADS/1Semestre/TurmaA/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexAds1A'):
                   txt = open('Horario/ADS/1Semestre/TurmaA/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

            elif(msg == 'SegAds1B'):
                   txt = open('Horario/ADS/1Semestre/TurmaB/SFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'TerAds1B'):
                   txt = open('Horario/ADS/1Semestre/TurmaB/TFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuaAds1B'):
                   txt = open('Horario/ADS/1Semestre/TurmaB/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuiAds1B'):
                   txt = open('Horario/ADS/1Semestre/TurmaB/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'SexAds1B'):
                   txt = open('Horario/ADS/1Semestre/TurmaB/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                   
############################### 1 SEMESTRE ADS ^^^^^^^ ###############################


############################### 2 SEMESTRE ADS #######################################                   

            elif(msg == '2SEMADS'):
                    bot.sendMessage(
                        chatID,
                        'Qual turma você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Turma A", callback_data='2SEMTurmaA')],
                                [InlineKeyboardButton(text="Turma B", callback_data='2SEMTurmaB')]
                            ]
                        )
                    )
                    
            elif(msg == '2SEMTurmaA'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegAds2A')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerAds2A')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaAds2A')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiAds2A')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexAds2A')],
                            ]
                        )
                    )
            
            elif(msg == '2SEMTurmaB'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegAds2B')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerAds2B')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaAds2B')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiAds2B')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexAds2B')],
                            ]
                        )
                    )
                 

            elif(msg == 'SegAds2A'):
                    txt = open('Horario/ADS/2Semestre/TurmaA/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerAds2A'):
                    txt = open('Horario/ADS/2Semestre/TurmaA/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaAds2A'):
                   txt = open('Horario/ADS/2Semestre/TurmaA/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiAds2A'):
                   txt = open('Horario/ADS/2Semestre/TurmaA/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexAds2A'):
                   txt = open('Horario/ADS/2Semestre/TurmaA/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

            elif(msg == 'SegAds2B'):
                   txt = open('Horario/ADS/2Semestre/TurmaB/SFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'TerAds2B'):
                   txt = open('Horario/ADS/2Semestre/TurmaB/TFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuaAds2B'):
                   txt = open('Horario/ADS/2Semestre/TurmaB/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuiAds2B'):
                   txt = open('Horario/ADS/2Semestre/TurmaB/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'SexAds2B'):
                   txt = open('Horario/ADS/3Semestre/TurmaB/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                   
############################### 2 SEMESTRE ADS ^^^^^^^ ###############################


                    
############################### 3 SEMESTRE ADS #######################################                   

            elif(msg == '3SEMADS'):
                    bot.sendMessage(
                        chatID,
                        'Qual turma você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Turma A", callback_data='3SEMTurmaA')],
                                [InlineKeyboardButton(text="Turma B", callback_data='3SEMTurmaB')]
                            ]
                        )
                    ) 
            elif(msg == '3SEMTurmaA'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegAds3A')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerAds3A')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaAds3A')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiAds3A')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexAds3A')],
                            ]
                        )
                    )
            
            elif(msg == '3SEMTurmaB'):
                
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegAds3B')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerAds3B')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaAds3B')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiAds3B')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexAds3B')],
                            ]
                        )
                    )
                 

            elif(msg == 'SegAds3A'):
                    txt = open('Horario/ADS/3Semestre/TurmaA/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerAds3A'):
                    txt = open('Horario/ADS/3Semestre/TurmaA/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaAds3A'):
                   txt = open('Horario/ADS/3Semestre/TurmaA/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiAds3A'):
                   txt = open('Horario/ADS/3Semestre/TurmaA/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexAds3A'):
                   txt = open('Horario/ADS/3Semestre/TurmaA/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

            elif(msg == 'SegAds3B'):
                   txt = open('Horario/ADS/3Semestre/TurmaB/SFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'TerAds3B'):
                   txt = open('Horario/ADS/3Semestre/TurmaB/TFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuaAds3B'):
                   txt = open('Horario/ADS/3Semestre/TurmaB/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuiAds3B'):
                   txt = open('Horario/ADS/3Semestre/TurmaB/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'SexAds3B'):
                   txt = open('Horario/ADS/3Semestre/TurmaB/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                   
############################### 3 SEMESTRE ADS ^^^^^^^ ###############################


############################### 4 SEMESTRE ADS ###############################                   

            elif(msg == '4SEMADS'):
                    bot.sendMessage(
                        chatID,
                        'Qual turma você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Turma A", callback_data='4SEMTurmaA')],
                                [InlineKeyboardButton(text="Turma B", callback_data='4SEMTurmaB')]
                            ]
                        )
                    ) 
            elif(msg == '4SEMTurmaA'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegAds4A')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerAds4A')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaAds4A')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiAds4A')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexAds4A')]
                            ]
                        )
                    )
            
            elif(msg == '4SEMTurmaB'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegAds4B')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerAds4B')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaAds4B')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiAds4B')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexAds4B')],
                            ]
                        )
                    )
                 

            elif(msg == 'SegAds4A'):
                    txt = open('Horario/ADS/4Semestre/TurmaA/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerAds4A'):
                    txt = open('Horario/ADS/4Semestre/TurmaA/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaAds4A'):
                   txt = open('Horario/ADS/4Semestre/TurmaA/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiAds4A'):
                   txt = open('Horario/ADS/4Semestre/TurmaA/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexAds4A'):
                   txt = open('Horario/ADS/4Semestre/TurmaA/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

            elif(msg == 'SegAds4B'):
                   txt = open('Horario/ADS/4Semestre/TurmaB/SFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'TerAds4B'):
                   txt = open('Horario/ADS/4Semestre/TurmaB/TFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuaAds4B'):
                   txt = open('Horario/ADS/4Semestre/TurmaB/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuiAds4B'):
                   txt = open('Horario/ADS/4Semestre/TurmaB/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'SexAds4B'):
                   txt = open('Horario/ADS/4Semestre/TurmaB/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                   
############################### 4 SEMESTRE ADS ^^^^^^^ ###############################


############################### 5 SEMESTRE ADS #######################################                   

            elif(msg == '5SEMADS'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegAds5')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerAds5')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaAds5')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiAds5')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexAds5')],
                            ]
                        )
                    )

            
        

            elif(msg == 'SegAds5'):
                    txt = open('Horario/ADS/5Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerAds5'):
                    txt = open('Horario/ADS/5Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaAds5'):
                   txt = open('Horario/ADS/5Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiAds5'):
                   txt = open('Horario/ADS/5Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexAds5'):
                   txt = open('Horario/ADS/5Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 5 SEMESTRE ADS ^^^^^^^ ###############################


                    
############################### 6 SEMESTRE ADS #######################################                   

            elif(msg == '6SEMADS'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegAds6')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerAds6')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaAds6')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiAds6')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexAds6')],
                            ]
                        )
                    )
                                        

            elif(msg == 'SegAds6'):
                   txt = open('Horario/ADS/6Semestre/SFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'TerAds6'):
                   txt = open('Horario/ADS/6Semestre/TFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuaAds6'):
                   txt = open('Horario/ADS/6Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuiAds6'):
                   txt = open('Horario/ADS/6Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'SexAds6'):
                   txt = open('Horario/ADS/6Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                   
############################### 6 SEMESTRE ADS ^^^^^^^ ###############################







############################### 4 SEMESTRE AMD ###############################                   
            
            elif(msg == '4SEMAMD'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegAmd4')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerAmd4')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaAmd4')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiAmd4')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexAmd4')],
                            ]
                        )
                    )
                                        
            elif(msg == 'SegAmd4'):
                   txt = open('Horario/AMD/4Semestre/SFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'TerAmd4'):
                   txt = open('Horario/AMD/4Semestre/TFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuaAmd4'):
                   txt = open('Horario/AMD/4Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuiAmd4'):
                   txt = open('Horario/AMD/4Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'SexAmd4'):
                   txt = open('Horario/AMD/4Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                   
############################### 4 SEMESTRE AMD ^^^^^^^ ###############################


############################### 5 SEMESTRE AMD #######################################                   

                    
            elif(msg == '5SEMAMD'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegAmd5')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerAmd5')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaAmd5')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiAmd5')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexAmd5')],
                            ]
                        )
                    )

                 

            elif(msg == 'SegAmd5'):
                    txt = open('Horario/AMD/5Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerAmd5'):
                    txt = open('Horario/AMD/5Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaAmd5'):
                   txt = open('Horario/AMD/5Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiAmd5'):
                   txt = open('Horario/AMD/5Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexAmd5'):
                   txt = open('Horario/AMD/5Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()

                   
############################### 5 SEMESTRE AMD ^^^^^^^ ###############################


                    
############################### 6 SEMESTRE AMD #######################################                   

          
            elif(msg == '6SEMAMD'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegAmd6')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerAmd6')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaAmd6')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiAmd6')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexAmd6')],
                            ]
                        )
                    )

                 

            elif(msg == 'SegAmd6'):
                    txt = open('Horario/AMD/6Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerAmd6'):
                    txt = open('Horario/AMD/6Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaAmd6'):
                   txt = open('Horario/AMD/6Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiAmd6'):
                   txt = open('Horario/AMD/6Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexAmd6'):
                   txt = open('Horario/AMD/6Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()

                   
############################### 6 SEMESTRE AMD ^^^^^^^ ###############################                   






############################### 1 SEMESTRE BD ###############################                   

            elif(msg == '1SEMBD'):
                        bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegBd1')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerBd1')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaBd1')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiBd1')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexBd1')],
                            ]
                        )
                    )

            elif(msg == 'SegBd1'):
                   txt = open('Horario/BD/1Semestre/SFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'TerBd1'):
                   txt = open('Horario/BD/1Semestre/TFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuaBd1'):
                   txt = open('Horario/BD/1Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuiBd1'):
                   txt = open('Horario/BD/1Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'SexBd1'):
                   txt = open('Horario/BD/1Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                   
############################### 1 SEMESTRE BD ^^^^^^^ ###############################


############################### 2 SEMESTRE BD #######################################                   

            elif(msg == '2SEMBD'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegBd2')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerBd2')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaBd2')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiBd2')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexBd2')],
                            ]
                        )
                    )

                 
        

            elif(msg == 'SegBd2'):
                   txt = open('Horario/BD/2Semestre/SFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'TerBd2'):
                   txt = open('Horario/BD/2Semestre/TFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuaBd2'):
                   txt = open('Horario/BD/2Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuiBd2'):
                   txt = open('Horario/BD/2Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'SexBd2'):
                   txt = open('Horario/BD/2Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                   
############################### 2 SEMESTRE BD ^^^^^^^ ###############################

                    
############################### 3 SEMESTRE BD #######################################                   

            elif(msg == '3SEMBD'):
                 bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegBd3')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerBd3')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaBd3')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiBd3')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexBd3')],
                            ]
                        )
                    )
                 
                                        

            elif(msg == 'SegBd3'):
                   txt = open('Horario/BD/3Semestre/SFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'TerBd3'):
                   txt = open('Horario/BD/3Semestre/TFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuaBd3'):
                   txt = open('Horario/BD/3Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuiBd3'):
                   txt = open('Horario/BD/3Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'SexBd3'):
                   txt = open('Horario/BD/3Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                   
############################### 3 SEMESTRE BD ^^^^^^^ ###############################


############################### 4 SEMESTRE BD ###############################
                   
            elif(msg == '4SEMBD'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegBd4')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerBd4')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaBd4')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiBd4')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexBd4')],
                            ]
                        )
                    )

            elif(msg == 'SegBd4'):
                    txt = open('Horario/BD/4Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerBd4'):
                    txt = open('Horario/BD/4Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaBd4'):
                   txt = open('Horario/BD/4Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiBd4'):
                   txt = open('Horario/BD/4Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexBd4'):
                   txt = open('Horario/BD/4Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 4 SEMESTRE BD ^^^^^^^ ###############################


############################### 5 SEMESTRE BD #######################################                   

            elif(msg == '5SEMBD'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegBd5')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerBd5')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaBd5')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiBd5')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexBd5')],
                            ]
                        )
                    )
                  

            elif(msg == 'SegBd5'):
                    txt = open('Horario/BD/5Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerBd5'):
                    txt = open('Horario/BD/5Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaBd5'):
                   txt = open('Horario/BD/5Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiBd5'):
                   txt = open('Horario/BD/5Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexBd5'):
                   txt = open('Horario/BD/5Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 5 SEMESTRE BD ^^^^^^^ ###############################


                    
############################### 6 SEMESTRE BD #######################################                   
 
            elif(msg == '6SEMBD'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegBd6')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerBd6')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaBd6')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiBd6')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexBd6')],
                            ]
                        )
                    )

            

            elif(msg == 'SegBd6'):
                    txt = open('Horario/BD/6Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerBd6'):
                    txt = open('Horario/BD/6Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaBd6'):
                   txt = open('Horario/BD/6Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiBd6'):
                   txt = open('Horario/BD/6Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexBd6'):
                   txt = open('Horario/BD/6Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 6 SEMESTRE BD ^^^^^^^ ###############################










############################### 1 SEMESTRE GPI ###############################                   

            elif(msg == '1SEMGPI'):
                        bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegGpi1')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerGpi1')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaGpi1')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiGpi1')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexGpi1')],
                            ]
                        )
                    )

            elif(msg == 'SegGpi1'):
                   txt = open('Horario/GPI/1Semestre/SFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'TerGpi1'):
                   txt = open('Horario/GPI/1Semestre/TFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuaGpi1'):
                   txt = open('Horario/GPI/1Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuiGpi1'):
                   txt = open('Horario/GPI/1Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'SexGpi1'):
                   txt = open('Horario/GPI/1Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                   
############################### 1 SEMESTRE GPI ^^^^^^^ ###############################


############################### 2 SEMESTRE GPI #######################################                   

            elif(msg == '2SEMGPI'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegGpi2')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerGpi2')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaGpi2')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiGpi2')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexGpi2')],
                            ]
                        )
                    )

                 
        

            elif(msg == 'SegGpi2'):
                   txt = open('Horario/GPI/2Semestre/SFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'TerGpi2'):
                   txt = open('Horario/GPI/2Semestre/TFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuaGpi2'):
                   txt = open('Horario/GPI/2Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuiGpi2'):
                   txt = open('Horario/GPI/2Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'SexGpi2'):
                   txt = open('Horario/GPI/2Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                   
############################### 2 SEMESTRE GPI ^^^^^^^ ###############################

                    
############################### 3 SEMESTRE GPI #######################################                   

            elif(msg == '3SEMGPI'):
                 bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegGpi3')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerGpi3')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaGpi3')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiGpi3')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexGpi3')],
                            ]
                        )
                    )
                 
                                        

            elif(msg == 'SegGpi3'):
                   txt = open('Horario/GPI/3Semestre/SFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'TerGpi3'):
                   txt = open('Horario/GPI/3Semestre/TFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuaGpi3'):
                   txt = open('Horario/GPI/3Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuiGpi3'):
                   txt = open('Horario/GPI/3Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'SexGpi3'):
                   txt = open('Horario/GPI/3Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                   
############################### 3 SEMESTRE GPI ^^^^^^^ ###############################


############################### 4 SEMESTRE GPI ###############################
                   
            elif(msg == '4SEMGPI'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegGpi4')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerGpi4')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaGpi4')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiGpi4')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexGpi4')],
                            ]
                        )
                    )

            elif(msg == 'SegGpi4'):
                    txt = open('Horario/GPI/4Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerGpi4'):
                    txt = open('Horario/GPI/4Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaGpi4'):
                   txt = open('Horario/GPI/4Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiGpi4'):
                   txt = open('Horario/GPI/4Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexGpi4'):
                   txt = open('Horario/GPI/4Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 4 SEMESTRE GPI ^^^^^^^ ###############################


############################### 5 SEMESTRE GPI #######################################                   

            elif(msg == '5SEMGPI'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegGpi5')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerGpi5')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaGpi5')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiGpi5')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexGpi5')],
                            ]
                        )
                    )
                  

            elif(msg == 'SegGpi5'):
                    txt = open('Horario/GPI/5Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerGpi5'):
                    txt = open('Horario/GPI/5Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaGpi5'):
                   txt = open('Horario/GPI/5Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiGpi5'):
                   txt = open('Horario/GPI/5Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexGpi5'):
                   txt = open('Horario/GPI/5Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 5 SEMESTRE GPI ^^^^^^^ ###############################


                    
############################### 6 SEMESTRE GPI #######################################                   
 
            elif(msg == '6SEMGPI'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegGpi6')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerGpi6')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaGpi6')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiGpi6')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexGpi6')],
                            ]
                        )
                    )

            

            elif(msg == 'SegGpi6'):
                    txt = open('Horario/GPI/6Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerGpi6'):
                    txt = open('Horario/GPI/6Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaGpi6'):
                   txt = open('Horario/GPI/6Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiGpi6'):
                   txt = open('Horario/GPI/6Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexGpi6'):
                   txt = open('Horario/GPI/6Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 6 SEMESTRE GPI ^^^^^^^ ###############################









############################### 1 SEMESTRE LOGÍSTICA MANHÃ ###############################
                   
            elif(msg == '1SEMLOGMA'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegLogMa1')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerLogMa1')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaLogMa1')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiLogMa1')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexLogMa1')],
                            ]
                        )
                    )

            elif(msg == 'SegLogMa1'):
                    txt = open('Horario/MAERO/1Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerLogMa1'):
                    txt = open('Horario/MAERO/1Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaLogMa1'):
                   txt = open('Horario/MAERO/1Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiLogMa1'):
                   txt = open('Horario/MAERO/1Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexLogMa1'):
                   txt = open('Horario/MAERO/1Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 1 SEMESTRE LOGÍSTICA MANHÃ ^^^^^^^ ###############################


############################### 2 SEMESTRE LOGÍSTICA MANHÃ #######################################                   

            elif(msg == '2SEMLOGMA'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegLogMa2')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerLogMa2')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaLogMa2')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiLogMa2')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexLogMa2')],
                            ]
                        )
                    )

            elif(msg == 'SegLogMa2'):
                    txt = open('Horario/MAERO/2Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerLogMa2'):
                    txt = open('Horario/MAERO/2Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaLogMa2'):
                   txt = open('Horario/MAERO/2Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiLogMa2'):
                   txt = open('Horario/MAERO/2Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexLogMa2'):
                   txt = open('Horario/MAERO/2Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 2 SEMESTRE LOGÍSTICA MANHÃ ^^^^^^^ ###############################


                    
############################### 3 SEMESTRE LOGÍSTICA MANHÃ #######################################                   
 
            elif(msg == '3SEMLOGMA'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegLogMa3')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerLogMa3')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaLogMa3')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiLogMa3')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexLogMa3')],
                            ]
                        )
                    )
            

            elif(msg == 'SegLogMa3'):
                    txt = open('Horario/MAERO/3Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerLogMa3'):
                    txt = open('Horario/MAERO/3Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaLogMa3'):
                   txt = open('Horario/MAERO/3Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiLogMa3'):
                   txt = open('Horario/MAERO/3Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexLogMa3'):
                   txt = open('Horario/MAERO/3Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 3 SEMESTRE LOGÍSTICA MANHÃ ^^^^^^^ ###############################
                   

############################### 4 SEMESTRE LOGÍSTICA MANHÃ ###############################
                   
            elif(msg == '4SEMLOGMA'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegLogMa4')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerLogMa4')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaLogMa4')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiLogMa4')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexLogMa4')],
                            ]
                        )
                    )

            elif(msg == 'SegLogMa4'):
                    txt = open('Horario/MAERO/4Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerLogMa4'):
                    txt = open('Horario/MAERO/4Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaLogMa4'):
                   txt = open('Horario/MAERO/4Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiLogMa4'):
                   txt = open('Horario/MAERO/4Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexLogMa4'):
                   txt = open('Horario/MAERO/4Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 4 SEMESTRE LOGÍSTICA MANHÃ ^^^^^^^ ###############################


############################### 5 SEMESTRE LOGÍSTICA MANHÃ #######################################                   

            elif(msg == '5SEMLOGMA'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegLogMa5')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerLogMa5')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaLogMa5')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiLogMa5')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexLogMa5')],
                            ]
                        )
                    )
                  

            elif(msg == 'SegLogMa5'):
                    txt = open('Horario/MAERO/5Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerLogMa5'):
                    txt = open('Horario/MAERO/5Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaLogMa5'):
                   txt = open('Horario/MAERO/5Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiLogMa5'):
                   txt = open('Horario/MAERO/5Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexLogMa5'):
                   txt = open('Horario/MAERO/5Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 5 SEMESTRE LOGÍSTICA MANHÃ ^^^^^^^ ###############################


                    
############################### 6 SEMESTRE LOGÍSTICA MANHÃ #######################################                   
 
            elif(msg == '6SEMLOGMA'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegLogMa6')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerLogMa6')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaLogMa6')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiLogMa6')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexLogMa6')],
                            ]
                        )
                    )

            

            elif(msg == 'SegLogMa6'):
                    txt = open('Horario/MAERO/6Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerLogMa6'):
                    txt = open('Horario/MAERO/6Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaLogMa6'):
                   txt = open('Horario/MAERO/6Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiLogMa6'):
                   txt = open('Horario/MAERO/6Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexLogMa6'):
                   txt = open('Horario/MAERO/6Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 6 SEMESTRE LOGÍSTICA MANHÃ ^^^^^^^ ###############################





############################### 1 SEMESTRE LOGÍSTICA NOITE ###############################
                   
            elif(msg == '1SEMLOGNO'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegLogNo1')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerLogNo1')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaLogNo1')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiLogNo1')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexLogNo1')],
                            ]
                        )
                    )

            elif(msg == 'SegLogNo1'):
                    txt = open('Horario/LOGNO/1Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerLogNo1'):
                    txt = open('Horario/LOGNO/1Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaLogNo1'):
                   txt = open('Horario/LOGNO/1Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiLogNo1'):
                   txt = open('Horario/LOGNO/1Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexLogNo1'):
                   txt = open('Horario/LOGNO/1Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 1 SEMESTRE LOGÍSTICA NOITE ^^^^^^^ ###############################


############################### 2 SEMESTRE LOGÍSTICA NOITE #######################################                   

            elif(msg == '2SEMLOGNO'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegLogNo2')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerLogNo2')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaLogNo2')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiLogNo2')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexLogNo2')],
                            ]
                        )
                    )

            elif(msg == 'SegLogNo2'):
                    txt = open('Horario/LOGNO/2Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerLogNo2'):
                    txt = open('Horario/LOGNO/2Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaLogNo2'):
                   txt = open('Horario/LOGNO/2Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiLogNo2'):
                   txt = open('Horario/LOGNO/2Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexLogNo2'):
                   txt = open('Horario/LOGNO/2Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 2 SEMESTRE LOGÍSTICA NOITE ^^^^^^^ ###############################


                    
############################### 3 SEMESTRE LOGÍSTICA NOITE #######################################                   
 
            elif(msg == '3SEMLOGNO'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegLogNo3')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerLogNo3')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaLogNo3')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiLogNo3')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexLogNo3')],
                            ]
                        )
                    )
            

            elif(msg == 'SegLogNo3'):
                    txt = open('Horario/LOGNO/3Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerLogNo3'):
                    txt = open('Horario/LOGNO/3Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaLogNo3'):
                   txt = open('Horario/LOGNO/3Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiLogNo3'):
                   txt = open('Horario/LOGNO/3Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexLogMa3'):
                   txt = open('Horario/LOGNO/3Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 3 SEMESTRE LOGÍSTICA NOITE ^^^^^^^ ###############################
                   

############################### 4 SEMESTRE LOGÍSTICA NOITE ###############################
                   
            elif(msg == '4SEMLOGNO'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegLogNo4')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerLogNo4')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaLogNo4')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiLogNo4')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexLogNo4')],
                            ]
                        )
                    )

            elif(msg == 'SegLogNo4'):
                    txt = open('Horario/LOGNO/4Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerLogNo4'):
                    txt = open('Horario/LOGNO/4Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaLogNo4'):
                   txt = open('Horario/LOGNO/4Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiLogNo4'):
                   txt = open('Horario/LOGNO/4Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexLogNo4'):
                   txt = open('Horario/LOGNO/4Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 4 SEMESTRE LOGÍSTICA NOITE ^^^^^^^ ###############################


############################### 5 SEMESTRE LOGÍSTICA NOITE #######################################                   

            elif(msg == '5SEMLOGNO'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegLogNo5')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerLogNo5')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaLogNo5')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiLogNo5')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexLogNo5')],
                            ]
                        )
                    )
                  

            elif(msg == 'SegLogNo5'):
                    txt = open('Horario/LOGNO/5Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerLogNo5'):
                    txt = open('Horario/LOGNO/5Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaLogNo5'):
                   txt = open('Horario/LOGNO/5Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiLogNo5'):
                   txt = open('Horario/LOGNO/5Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexLogNo5'):
                   txt = open('Horario/LOGNO/5Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 5 SEMESTRE LOGÍSTICA NOITE ^^^^^^^ ###############################


                    
############################### 6 SEMESTRE LOGÍSTICA NOITE #######################################                   
 
            elif(msg == '6SEMLOGNO'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegLogNo6')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerLogNo6')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaLogNo6')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiLogNo6')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexLogNo6')],
                            ]
                        )
                    )

            

            elif(msg == 'SegLogNo6'):
                    txt = open('Horario/LOGNO/6Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerLogNo6'):
                    txt = open('Horario/LOGNO/6Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaLogNo6'):
                   txt = open('Horario/LOGNO/6Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiLogNo6'):
                   txt = open('Horario/LOGNO/6Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexLogNo6'):
                   txt = open('Horario/LOGNO/6Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 6 SEMESTRE LOGÍSTICA NOITE ^^^^^^^ ###############################







############################### 1 SEMESTRE MANUFATURA AVANÇADA ###############################
                   
            elif(msg == '1SEMMAVAN'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegMavan1')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerMavan1')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaMavan1')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiMavan1')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexMavan1')],
                            ]
                        )
                    )

            elif(msg == 'SegMavan1'):
                    txt = open('Horario/MAVAN/1Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerMavan1'):
                    txt = open('Horario/MAVAN/1Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaMavan1'):
                   txt = open('Horario/MAVAN/1Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiMavan1'):
                   txt = open('Horario/MAVAN/1Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexMavan1'):
                   txt = open('Horario/MAVAN/1Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 1 SEMESTRE MANUFATURA AVANÇADA ^^^^^^^ ###############################


############################### 2 SEMESTRE MANUFATURA AVANÇADA #######################################                   

            elif(msg == '2SEMMAVAN'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegMavan2')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerMavan2')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaMavan2')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiMavan2')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexMavan2')],
                            ]
                        )
                    )

            elif(msg == 'SegMavan2'):
                    txt = open('Horario/MAVAN/2Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerMavan2'):
                    txt = open('Horario/MAVAN/2Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaMavan2'):
                   txt = open('Horario/MAVAN/2Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiMavan2'):
                   txt = open('Horario/MAVAN/2Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexMavan2'):
                   txt = open('Horario/MAVAN/2Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 2 SEMESTRE MANUFATURA AVANÇADA ^^^^^^^ ###############################


                    
############################### 3 SEMESTRE MANUFATURA AVANÇADA #######################################                   
 
            elif(msg == '3SEMMAVAN'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegMavan3')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerMavan3')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaMavan3')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiMavan3')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexMavan3')],
                            ]
                        )
                    )
            

            elif(msg == 'SegMavan3'):
                    txt = open('Horario/MAVAN/3Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerMavan3'):
                    txt = open('Horario/MAVAN/3Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaMavan3'):
                   txt = open('Horario/MAVAN/3Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiMavan3'):
                   txt = open('Horario/MAVAN/3Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexMavan3'):
                   txt = open('Horario/MAVAN/3Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 3 SEMESTRE MANUFATURA AVANÇADA ^^^^^^^ ###############################




############################### 1 SEMESTRE MANUTENÇÃO DE AERONAVES ###############################
                   
            elif(msg == '1SEMMAERO'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegMaero1')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerMaero1')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaMaero1')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiMaero1')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexMaero1')],
                            ]
                        )
                    )

            elif(msg == 'SegMaero1'):
                    txt = open('Horario/MAERO/1Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerMaero1'):
                    txt = open('Horario/MAERO/1Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaMaero1'):
                   txt = open('Horario/MAERO/1Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiMaero1'):
                   txt = open('Horario/MAERO/1Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexMaero1'):
                   txt = open('Horario/MAERO/1Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 1 SEMESTRE MANUTENÇÃO DE AERONAVES ^^^^^^^ ###############################


############################### 2 SEMESTRE MANUTENÇÃO DE AERONAVES #######################################                   

            elif(msg == '2SEMMAERO'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegMaero2')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerMaero2')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaMaero2')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiMaero2')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexMaero2')],
                            ]
                        )
                    )

            elif(msg == 'SegMaero2'):
                    txt = open('Horario/MAERO/2Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerMaero2'):
                    txt = open('Horario/MAERO/2Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaMaero2'):
                   txt = open('Horario/MAERO/2Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiMaero2'):
                   txt = open('Horario/MAERO/2Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexMaero2'):
                   txt = open('Horario/MAERO/2Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 2 SEMESTRE MANUTENÇÃO DE AERONAVES ^^^^^^^ ###############################


                    
############################### 3 SEMESTRE MANUTENÇÃO DE AERONAVES #######################################                   
 
            elif(msg == '3SEMMAERO'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegMaero3')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerMaero3')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaMaero3')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiMaero3')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexMaero3')],
                            ]
                        )
                    )
            

            elif(msg == 'SegMaero3'):
                    txt = open('Horario/MAERO/3Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerMaero3'):
                    txt = open('Horario/MAERO/3Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaMaero3'):
                   txt = open('Horario/MAERO/3Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiMaero3'):
                   txt = open('Horario/MAERO/3Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexMaero3'):
                   txt = open('Horario/MAERO/3Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 3 SEMESTRE MANUTENÇÃO DE AERONAVES ^^^^^^^ ###############################

############################### 4 SEMESTRE MANUTENÇÃO DE AERONAVES ###############################
                   
            elif(msg == '4SEMMAERO'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegMaero4')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerMaero4')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaMaero4')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiMaero4')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexMaero4')],
                            ]
                        )
                    )

            elif(msg == 'SegMaero4'):
                    txt = open('Horario/MAERO/4Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerMaero4'):
                    txt = open('Horario/MAERO/4Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaMaero4'):
                   txt = open('Horario/MAERO/4Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiMaero4'):
                   txt = open('Horario/MAERO/4Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexMaero4'):
                   txt = open('Horario/MAERO/4Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 4 SEMESTRE MANUTENÇÃO DE AERONAVES ^^^^^^^ ###############################


############################### 5 SEMESTRE MANUTENÇÃO DE AERONAVES #######################################                   

            elif(msg == '5SEMMAERO'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegMaero5')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerMaero5')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaMaero5')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiMaero5')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexMaero5')],
                            ]
                        )
                    )
                  

            elif(msg == 'SegMaero5'):
                    txt = open('Horario/MAERO/5Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerMaero5'):
                    txt = open('Horario/MAERO/5Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaMaero5'):
                   txt = open('Horario/MAERO/5Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiMaero5'):
                   txt = open('Horario/MAERO/5Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexMaero5'):
                   txt = open('Horario/MAERO/5Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 5 SEMESTRE MANUTENÇÃO DE AERONAVES ^^^^^^^ ###############################


                    
############################### 6 SEMESTRE MANUTENÇÃO DE AERONAVES #######################################                   
 
            elif(msg == '6SEMMAERO'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegMaero6')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerMaero6')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaMaero6')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiMaero6')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexMaero6')],
                            ]
                        )
                    )

            

            elif(msg == 'SegMaero6'):
                    txt = open('Horario/MAERO/6Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerMaero6'):
                    txt = open('Horario/MAERO/6Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaMaero6'):
                   txt = open('Horario/MAERO/6Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiMaero6'):
                   txt = open('Horario/MAERO/6Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexMaero6'):
                   txt = open('Horario/MAERO/6Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 6 SEMESTRE MANUTENÇÃO DE AERONAVES ^^^^^^^ ###############################






############################### 1 SEMESTRE PROJETOS DE ESTRUTURAS AERONÁUTICAS ###############################
                   
            elif(msg == '1SEMPEA'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegPea1')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerPea1')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaPea1')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiPea1')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexPea1')],
                            ]
                        )
                    )

            elif(msg == 'SegPea1'):
                    txt = open('Horario/PEA/1Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerPea1'):
                    txt = open('Horario/PEA/1Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaPea1'):
                   txt = open('Horario/PEA/1Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiPea1'):
                   txt = open('Horario/PEA/1Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexPea1'):
                   txt = open('Horario/PEA/1Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 1 SEMESTRE PROJETOS DE ESTRUTURAS AERONÁUTICAS ^^^^^^^ ###############################


############################### 2 SEMESTRE PROJETOS DE ESTRUTURAS AERONÁUTICAS #######################################                   

            elif(msg == '2SEMPEA'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegPea2')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerPea2')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaPea2')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiPea2')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexPea2')],
                            ]
                        )
                    )

            elif(msg == 'SegPea2'):
                    txt = open('Horario/PEA/2Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerPea2'):
                    txt = open('Horario/PEA/2Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaPea2'):
                   txt = open('Horario/PEA/2Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiPea2'):
                   txt = open('Horario/PEA/2Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexPea2'):
                   txt = open('Horario/PEA/2Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 2 SEMESTRE PROJETOS DE ESTRUTURAS AERONÁUTICAS ^^^^^^^ ###############################


                    
############################### 3 SEMESTRE PROJETOS DE ESTRUTURAS AERONÁUTICAS #######################################                   
 
            elif(msg == '3SEMPEA'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegPea3')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerPea3')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaPea3')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiPea3')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexPea3')],
                            ]
                        )
                    )
            

            elif(msg == 'SegPea3'):
                    txt = open('Horario/PEA/3Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerPea3'):
                    txt = open('Horario/PEA/3Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaPea3'):
                   txt = open('Horario/PEA/3Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiPea3'):
                   txt = open('Horario/PEA/3Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexPea3'):
                   txt = open('Horario/PEA/3Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 3 SEMESTRE PROJETOS DE ESTRUTURAS AERONÁUTICAS ^^^^^^^ ###############################


############################### 4 SEMESTRE PROJETOS DE ESTRUTURAS AERONÁUTICAS ###############################
                   
            elif(msg == '4SEMPEA'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegPea4')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerPea4')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaPea4')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiPea4')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexPea4')],
                            ]
                        )
                    )

            elif(msg == 'SegPea4'):
                    txt = open('Horario/PEA/4Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerPea4'):
                    txt = open('Horario/PEA/4Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaPea4'):
                   txt = open('Horario/PEA/4Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiPea4'):
                   txt = open('Horario/PEA/4Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexPea4'):
                   txt = open('Horario/PEA/4Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 4 SEMESTRE PROJETOS DE ESTRUTURAS AERONÁUTICAS ^^^^^^^ ###############################


############################### 5 SEMESTRE PROJETOS DE ESTRUTURAS AERONÁUTICAS #######################################                   

            elif(msg == '5SEMPEA'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegPea5')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerPea5')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaPea5')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiPea5')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexPea5')],
                            ]
                        )
                    )
                  

            elif(msg == 'SegPea5'):
                    txt = open('Horario/PEA/5Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerPea5'):
                    txt = open('Horario/PEA/5Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaPea5'):
                   txt = open('Horario/PEA/5Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiPea5'):
                   txt = open('Horario/PEA/5Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexPea5'):
                   txt = open('Horario/PEA/5Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
#################### 5 SEMESTRE PROJETOS DE ESTRUTURAS AERONÁUTICAS ^^^^^^^ ###############################


                    
#################### 6 SEMESTRE PROJETOS DE ESTRUTURAS AERONÁUTICAS #######################
 
            elif(msg == '6SEMPEA'):
                    bot.sendMessage(
                        chatID,
                        'Qual dia da semana você deseja ver?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegPea6')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerPea6')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaPea6')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiPea6')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexPea6')],
                            ]
                        )
                    )

            

            elif(msg == 'SegPea6'):
                    txt = open('Horario/PEA/6Semestre/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerPea6'):
                    txt = open('Horario/PEA/6Semestre/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaPea6'):
                   txt = open('Horario/PEA/6Semestre/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiPea6'):
                   txt = open('Horario/PEA/6Semestre/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexPea6'):
                   txt = open('Horario/PEA/6Semestre/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

                   
############################### 6 SEMESTRE PROJETOS DE ESTRUTURAS AERONÁUTICAS ^^^^^^^ ###############################







##########################################################################################################

############################CALENDÁRIO##########
            elif (msg == 'Calendário'):
                bot.sendMessage(chatID, "Enviando calendário...")
                doc = open ("Calendário/calendario_2019-1.pdf",'rb')
                bot.sendDocument(chatID, doc)
                doc.close()
                keyboard=ReplyKeyboardMarkup(
                        keyboard=[
                            [
                                KeyboardButton(text="Voltar")
                            ]
                        ],resize_keyboard=True
                    )
                bot.sendMessage(chatID,"O seu calendário estudantil está pronto...", reply_markup=keyboard)

                  

##########################################################################################################


############################AVISOS##########
            elif(msg == 'Avisos'):
                txt = open('Avisos/AvisosGerais.md','r')	
                bot.sendMessage(chatID,txt.read(),'Markdown')   
                txt.close()
              	













            elif (msg == 'Voltar'):
                    inicio(chatID, bot)

'''SOBRE: callback
O parametro desta funcao eh um Json enviado do message_loop com os campos referente a interacao feita via a chave 'callback_query', ou seja, esta funcao eh responsavel por
por pegar o que foi emitido pelo usuario (texto iniline_keyboard) e seu respectivo ID, e repassar para a funcao 'condicoes' e que sera processado a requisicao
e sera emitido o devido comportamento que o usuario quer em relacao ao bot
'''
def callback(msg):
            query_id, from_id, query_data = telepot.glance(msg, flavor="callback_query")
            #Forma facilitada pela biblioteca "telepot" de quebrar inserir as informacoes para as respectivas variaveis
            #Ou seja, pega o Json com a chave callback_queryt' e quebra as informacoes em tres jogando o valor de 'text' para a variavel tipoMsg,
            #assim por adiante...

            chatID = from_id
            #ID do usuario que apertou o botao

            texto = query_data
            #o valor do botao que foi apertado

            print(chatID)

            bot.answerCallbackQuery(query_id, text="Só um instante")
            #retorna um POP-UP para o usuario quando ele digitou alguma coisa

            print("callback query", query_id, from_id, query_data)

            condicoes(chatID, texto)
            # pega o que foi clicado pelo usuario (callback_data) e seu ID manda para a funcao 'condicoes' que vai processar o clique


'''SOBRE: ir
O parametro desta funcao eh um Json enviado do message_loop com os campos referente a interacao via a chave 'chat', ou seja, esta funcao eh responsavel por
por pegar o que foi emitido pelo usuario (texto via mensagem) e seu respectivo ID, e repassar para a funcao  'condicoes' e que sera processado a requisicao
e sera emitido o devido comportamento que o usuario quer em relacao ao bot
'''
def ir(msg):
            #Forma facilitada pela biblioteca "telepot" de quebrar inserir as informacoes para as respectivas variaveis
            #Ou seja, pega o Json com a chave 'chat' e quebra as informacoes em tres jogando o valor de 'text' para a variavel tipoMsg,
            #assim por adiante...
            tipoMsg, tipoChat, chatID = telepot.glance(msg)

            texto = msg['text']     #variavel Auxiliar para receber a texto que o usuario digitou, fiz ela porque se eu chamasse --condicoes(chatID, msg['text'])--
                                    #tava dando erro

            condicoes(chatID, texto)    # pega o que foi digitado pelo usuario e seu ID manda para a funcao 'condicoes' que vai processar o a mensagem

'''SOBRE: inico
Esta funcao eh uma forma de facilitar o a primeira interacao ao usuario
'''
def inicio(chatID, bot):
            keyboard=ReplyKeyboardMarkup(
                        keyboard=[
                            [
                                KeyboardButton(text="Avisos"),
                                KeyboardButton(text="Calendário"),
                                KeyboardButton(text="Horário"),
                            ]
                        ],resize_keyboard=True
                    )

            txt = open('Inicializacao/Hello.md','r')    #Abre o arquivo Hello.md com o atributo leitura
            bot.sendMessage(chatID,txt.read(),'Markdown',reply_markup=keyboard)
            txt.close()

''' SOBRE: message_loop
o message_loop eh o "listenen" das interacoes dos usuarios com o bot, ele retorna um Json, que quando uma interacao eh feita via mensagem,
recorre a chave 'chat' e redireciona o comportamento do bot para a funcao "ir", e quando uma interacao eh feita via inline_keyboard (callback_query)
recorre a chave callback
'''
bot.message_loop(
    {
        'chat': ir,
        'callback_query': callback,
    }
)

#responsavel por deixa o programa sempre em execucao, mas quando ocorre uma interacao, o message_loop e invocado, e quebra este laco infinito,
#e faz o comportamento requirido pelo usuario
while True:
            pass
