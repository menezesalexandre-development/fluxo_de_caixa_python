import pandas as pd


def del_emp(filepath, nome_empresa):
    with open('csv/empresas.csv') as file:
        contador = 0
        for line in file:
            if contador == 0:
                pass
            elif contador >= 1 and nome_empresa in line:
                df = pd.read_csv(filepath)
                df = df[df.Empresa != nome_empresa]
                df.to_csv(filepath, index=False)
                print(line)
            contador += 1


del_emp('csv/empresas.csv', 'Restaurante')
