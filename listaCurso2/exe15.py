import os
import datetime
import calendar
import time


diretorio_atual = os.getcwd()
print("Diretório atual:", diretorio_atual)

agora = datetime.datetime.now()
print("Data e hora atuais:", agora)

ano = agora.year
mes = agora.month
print(f"\nCalendário de {mes}/{ano}:")
print(calendar.month(ano, mes))

print("Aguardando 3 segundos...")
time.sleep(3)
print("Fim da pausa!")