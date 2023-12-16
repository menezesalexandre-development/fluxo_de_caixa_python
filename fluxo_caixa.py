from customtkinter import *

# CORES:
white = '#ffffff'
black = '#000000'

# CONFIGURAÇÃO DA INTERFACE
window = CTk()
window.title('Fluxo de Caixa com Python')
window.geometry('950x660')

default_theme = 'dark'
match default_theme:
    case 'dark':
        set_appearance_mode('dark')
    case 'light':
        set_appearance_mode('light')

titulo = CTkLabel(window, text='SISTEMA DE FLUXO DE CAIXA', text_color=white)
titulo.pack(padx=10, pady=10)

window.mainloop()
