import pandas as pd
from datetime import datetime, date

current_date = date.today()
current_day = date.today().day
current_month = date.today().month
current_year = date.today().year
current_second = datetime.now().second
current_minute = datetime.now().minute
current_hour = datetime.now().hour

match current_month:
    case 1:
        current_month = 'Janeiro'
    case 2:
        current_month = 'Fevereiro'
    case 3:
        current_month = 'Março'
    case 4:
        current_month = 'Abril'
    case 5:
        current_month = 'Maio'
    case 6:
        current_month = 'Junho'
    case 7:
        current_month = 'Julho'
    case 8:
        current_month = 'Agosto'
    case 9:
        current_month = 'Setembro'
    case 10:
        current_month = 'Outubro'
    case 11:
        current_month = 'Novembro'
    case 12:
        current_month = 'Dezembro'

newData = {
    'Data do Caixa': current_date,
    'Horário do Caixa': f'{current_hour}:{current_minute}:{current_second}',
    'Valor do Caixa': 90.00,
    'Dia': current_day,
    'Mes': current_month,
    'Ano': current_year
}

a = open('csv/caixa.csv', 'at')
a.write(f'\n{newData["Data do Caixa"]},{newData["Horário do Caixa"]},{newData["Valor do Caixa"]},{newData["Dia"]},{newData["Mes"]},{newData["Ano"]}')
a.close()

print(f'Data: {current_day} de {current_month} de {current_year} às {current_hour}:{current_minute}')
print(f'Valor do Caixa: {newData["Valor do Caixa"]}')

table = pd.read_csv('csv/caixa.csv')
print(table)
