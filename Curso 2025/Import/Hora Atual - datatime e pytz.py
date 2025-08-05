'''
Atividade 13

Você quer mostrar a hora certa para marcar uma videochamada.

Crie uma função hora_atual() que retorna a hora atual formatada como "HH:MM:SS".

Use a função datetime.now() do import datetime que pega a data nesse momento
'''
import datetime
import pytz

print ("=== Hora Atual (Brasil) ===")

def hora_atual():
    
    # Define o fuso horário para São Paulo
    fuso_brasil = pytz.timezone("America/Sao_Paulo")
    
    # O módulo datetime tem uma classe também chamada datetime
    agora = datetime.datetime.now(fuso_brasil)
    
    # Formata para HH:MM:SS 
    hora_formatada = agora.strftime("%H:%M:%S")
    print(f"Hora atual: {hora_formatada}")
    
hora_atual()
