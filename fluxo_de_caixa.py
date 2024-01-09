from customtkinter import *
from csv_functions import *
from os.path import isfile, exists
from os import remove
from tkinter import ttk
import tkinter
import pandas as pd
import csv

# GLOBAIS:
app = CTk()

# EMPRESA.CSV:
empresa_csv_path = "csv/empresas.csv"
empresa_csv_table = ""


def start_app():
    global app
    global empresa_csv_path
    global empresa_csv_table
    if isfile(empresa_csv_path):
        empresa_csv_table = pd.read_csv(empresa_csv_path)

    app = CTk()
    app.geometry("600x500")
    app.title('Fluxo de Caixa com Python')

    def gerenciar_empresa(empresa_nome):
        print(empresa_nome)
        empresa_caixa = CTkToplevel(app)
        empresa_caixa.transient(app)
        empresa_caixa.geometry('500x400')

        titulo_empresa = CTkLabel(empresa_caixa, text=f'CAIXA DO {empresa_nome}', font=('Ubuntu Bold', 25), text_color='#fff')
        titulo_empresa.pack(pady=15)

        caixa_csv = open(f'csv/{empresa_nome}.csv')
        ler_csv = csv.reader(caixa_csv)
        l1 = []
        l1 = next(ler_csv)
        print(l1)
        r_set = [row for row in ler_csv]
        r_set = r_set[::-1]
        print(r_set)

        trv = ttk.Treeview(empresa_caixa, selectmode='browse')
        trv.pack()
        trv['height'] = 10
        trv['show'] = 'headings'
        trv['columns'] = l1

        for i in l1:
            trv.column(i, width=100, anchor='c')
            trv.heading(i, text=i)

        for dt in r_set:
            v = [r for r in dt]
            trv.insert('', 'end', iid=v[0], values=v)

        realizar_caixa = CTkButton(empresa_caixa, text='Realizar novo caixa', font=('Ubuntu Bold', 12))
        realizar_caixa.pack(pady=20)

    def add_empresa_window():
        global app
        global empresa_csv_path
        global empresa_csv_table
        add_emp = CTkToplevel(app)
        add_emp.transient(app)
        add_emp.geometry("400x300")

        title = CTkLabel(add_emp, text='Adicionar empresa', text_color='#fff', font=("Ubuntu Bold", 26))
        title.pack(pady=10)

        name_status = CTkLabel(add_emp, text='', text_color='#ff0000', font=("Ubuntu Bold", 12))
        name_status.pack(padx=10, pady=10)

        nome_empresa = CTkEntry(add_emp, placeholder_text='Nome da Empresa', fg_color='#fff', font=("Ubuntu Bold", 12), text_color='#000')
        nome_empresa.pack(padx=10, pady=10)

        def add_empresa():
            global app
            global empresa_csv_path
            global empresa_csv_table
            new_empresa = nome_empresa.get()
            nome_empresa.delete(0, END)

            if new_empresa == '':
                name_status.configure(text='Campo obrigatório!')
            elif 255 <= len(new_empresa) <= 0:
                name_status.configure(text='Digite entre 1 e 255 caracteres!')
            else:
                new_empresa = new_empresa.upper()
                register_empresa(empresa_csv_path, new_empresa)
                with open(f'csv/{new_empresa}.csv', 'a') as f_caixa:
                    f_caixa.write("Caixa,Dia,Mes,Ano")
                    f_caixa.write("\n")
                add_emp.destroy()
                app.destroy()
                start_app()

        add_button = CTkButton(add_emp, text='Adicionar', text_color='#fff', font=("Ubuntu Bold", 12), command=add_empresa)
        add_button.pack(padx=10, pady=10)

    def del_empresa_window():
        global app
        global empresa_csv_path
        global empresa_csv_table
        del_emp = CTkToplevel(app)
        del_emp.transient(app)
        del_emp.geometry("400x300")

        remove_title = CTkLabel(del_emp, text='Remover empresa', text_color='#fff', font=("Ubuntu Bold", 26))
        remove_title.pack(padx=10, pady=10)

        if not check_empresas(empresa_csv_path):
            no_empresas = CTkLabel(del_emp, text='Não há empresas cadastradas', text_color='#fff', font=("Ubuntu Bold", 12))
            no_empresas.pack(padx=1, pady=1)
        else:
            aviso = CTkLabel(del_emp, text='AVISO: ESCREVA CORRETAMENTE O NOME DA EMPRESA!', text_color='#ff0000', font=("Ubuntu Bold", 12))
            aviso.pack(padx=1, pady=1)

            name_status = CTkLabel(del_emp, text='', text_color='#ff0000', font=("Ubuntu Bold", 12))
            name_status.pack(padx=1, pady=1)

            del_emp_entry = CTkEntry(del_emp, placeholder_text='Nome da empresa', fg_color="#fff", placeholder_text_color='#000', font=("Ubuntu Bold", 12), text_color="#000")
            del_emp_entry.pack(padx=10, pady=10)

            def del_empresa():
                global app
                global empresa_csv_path
                global empresa_csv_table
                del_instance = del_emp_entry.get()
                del_emp_entry.delete(0, END)

                if del_instance == '':
                    name_status.configure(text='Campo obrigatório!')
                elif 255 <= len(del_instance) <= 0:
                    name_status.configure(text='Digite entre 1 e 255 caracteres!')
                else:
                    del_instance = del_instance.upper()
                    deletar_empresa(empresa_csv_path, del_instance)
                    if exists(f'csv/{del_instance}.csv'):
                        remove(f'csv/{del_instance}.csv')
                    else:
                        print('Não foi possível remover o caixa da empresa!')
                    del_emp.destroy()
                    app.destroy()
                    start_app()

            del_button = CTkButton(del_emp, text='Deletar', text_color='#fff', font=("Ubuntu Bold", 12), command=del_empresa)
            del_button.pack(padx=10, pady=10)

    # DEFAULT THEME & DEFAULT COLOR:
    default_theme = 'dark'
    match default_theme:
        case 'dark':
            set_appearance_mode('dark')
        case 'light':
            set_appearance_mode('light')

    default_color = 'dark-blue'
    match default_color:
        case 'dark-blue':
            set_default_color_theme('blue')
        case 'green':
            set_default_color_theme('green')
        case 'blue':
            set_default_color_theme('blue')

    # WIDGETS:
    titulo = CTkLabel(app, text='SISTEMA DE FLUXO DE CAIXA', text_color='#fff', font=("Ubuntu Bold", 36))
    titulo.pack(padx=10, pady=30)

    empresas_title = CTkLabel(app, text='Lista de empresas:', text_color='#fff', font=("Ubuntu Bold", 15))
    empresas_title.pack(padx=1, pady=1)

    if len(empresa_csv_table) == 0:
        zero_empresas = CTkLabel(app, text='Não há empresas cadastradas', text_color='#fff', font=("Ubuntu Bold", 12))
        zero_empresas.pack(padx=1, pady=1)
    else:
        for c in range(0, len(empresa_csv_table)):
            empresa = CTkButton(app, text=empresa_csv_table["Empresa"][c], text_color='#fff', font=("Ubuntu Bold", 12), command=lambda: gerenciar_empresa(empresa.cget('text')))
            empresa.pack(padx=1, pady=1)

    empty_text = CTkLabel(app, text='')
    empty_text.pack(padx=1, pady=15)

    adicionar_empresa = CTkButton(app, text='Adicionar empresa +', text_color='#fff', font=("Ubuntu Bold", 12), command=add_empresa_window)
    adicionar_empresa.pack(padx=1, pady=1)

    remover_empresa_btn = CTkButton(app, text='Remover empresa -', text_color='#fff', font=("Ubuntu Bold", 12), fg_color='#ff0000', state='normal', command=del_empresa_window)
    remover_empresa_btn.pack(padx=1, pady=1)

    if len(empresa_csv_table) == 0:
        remover_empresa_btn.configure(state='disabled')
    else:
        remover_empresa_btn.configure(state='normal')

    try:
        app.mainloop()
    except KeyboardInterrupt:
        print('Programa interrompido')


while True:
    if isfile(empresa_csv_path):
        start_app()
        break
    else:
        with open(empresa_csv_path, 'a') as arquivo:
            arquivo.write("Empresa")
            arquivo.write("\n")
