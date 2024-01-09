import pandas as pd
from datetime import date

current_day = date.today().day
if len(str(current_day)) == 1:
    current_day = str(f'0{str(current_day)}')

current_month = date.today().month
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

current_year = date.today().year


def registrar_caixa(filepath, caixa):
    global current_day, current_month, current_year
    csv_table = pd.read_csv(filepath)
    new_id = len(csv_table['ID']) + 1
    novo_caixa = f'{new_id},{caixa:.2f},{current_day},{current_month},{current_year}'

    with open(filepath, 'a') as file:
        file.write("\n")
        file.write(novo_caixa)


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

