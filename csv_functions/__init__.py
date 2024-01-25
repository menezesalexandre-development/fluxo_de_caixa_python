import pandas as pd
from csv import reader
from datetime import date

current_day = date.today().day
if len(str(current_day)) == 1:
    current_day = str(f'0{str(current_day)}')

current_month_num = date.today().month
if len(str(current_month_num)) == 1:
    current_month_num = str(f'0{str(current_month_num)}')

current_month = date.today().month
match current_month:
    case 1:
        current_month = 'Janeiro'
    case 2:
        current_month = 'Fevereiro'
    case 3:
        current_month = 'Marco'
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

current_year = date.today().year


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def calcular_saldo(filepath):
    table = pd.read_csv(filepath)
    soma = table['Valor'].sum()
    soma = f'R${soma:.2f}'
    soma = soma.replace('.', ',')
    return soma


def registrar_caixa(filepath, caixa, tipo, entry_day, entry_month, entry_year):
    global current_day, current_month, current_year

    entry_day = entry_day
    if len(str(entry_day)) == 1:
        entry_day = str(f'0{str(entry_day)}')

    entry_month_num = entry_month
    if len(str(entry_month_num)) == 1:
        entry_month_num = str(f'0{str(entry_month_num)}')

    match entry_month_num:
        case '01':
            entry_month = 'Janeiro'
        case '02':
            entry_month = 'Fevereiro'
        case '03':
            entry_month = 'Marco'
        case '04':
            entry_month = 'Abril'
        case '05':
            entry_month = 'Maio'
        case '06':
            entry_month = 'Junho'
        case '07':
            entry_month = 'Julho'
        case '08':
            entry_month = 'Agosto'
        case '09':
            entry_month = 'Setembro'
        case '10':
            entry_month = 'Outubro'
        case '11':
            entry_month = 'Novembro'
        case '12':
            entry_month = 'Dezembro'

    with open(filepath, 'a') as file:
        file.write("\n")
        file.write(f'{caixa},{tipo},{entry_day},{entry_month},{entry_year},{entry_year}-{entry_month_num}-{entry_day}')


def check_empresas(filepath):
    table = pd.read_csv(filepath)
    if len(table) == 0:
        return False
    else:
        print(table)
        return True


def register_empresa(filepath, nome_empresa):
    with open(filepath, 'a') as f:
        f.write("\n")
        f.write(nome_empresa)


def deletar_empresa(filepath, nome_empresa):
    with open(filepath) as file:
        contador = 0
        exclusao = False
        for line in file:
            if contador == 0:
                pass
            elif contador >= 1 and nome_empresa in line:
                df = pd.read_csv(filepath)
                df = df[df.Empresa != nome_empresa]
                df.to_csv(filepath, index=False)
                print(line)
                exclusao = True
            contador += 1

        if exclusao:
            exclusao_msg = 'Empresa deletada com sucesso!'
        else:
            exclusao_msg = 'Empresa não encontrada!'

        return exclusao_msg

