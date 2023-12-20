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
        f.write(nome_empresa)
        f.write("\n")


def deletar_empresa(filepath, nome_empresa):
    df = pd.read_csv(filepath)
    df = df[df.Empresa != nome_empresa]
    df.to_csv(filepath, index=False)

