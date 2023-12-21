import pandas as pd


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

