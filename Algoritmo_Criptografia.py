import PySimpleGUI as sg
import pyperclip

def create_Window(theme):
    sg.theme('LightBlue2')
    botao = (0,2)
    
    layout = [
        [sg.Text('Digite um texto:', justification='center', expand_x=True)],
        [sg.Input(key='mensage', expand_x=True)],
        [sg.Text('Digite a chave da criptografia:', justification='center', expand_x=True)],
        [sg.Input(key='kword', expand_x=True, password_char="*")],
        [sg.Button('Criptografar', key='cript', expand_x=True, size=botao)],
        [sg.Button('Descriptografar', key='descript', expand_x=True, size=botao)],
        [sg.Text('Mensagem final', size=(40,15), key='result')],
        [sg.Button('Copiar mensagem final', key='copy', expand_x=True)]
    ]
    return sg.Window('Cripto', layout)

window = create_Window('light')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == 'cript':
        fim = ''
        n1 = 0
        mensagem = window['mensage'].get()
        senha = window['kword'].get()

        if not mensagem or not senha:
            sg.popup_error('Preencha a mensagem e a chave!')
            continue

        for i in mensagem:
            i_num = ord(i)
            wd_num = ord(senha[n1])
            n = (i_num + wd_num) % 512
            fim += chr(n)
            n1 = (n1 + 1) % len(senha)

        window['result'].update(fim)
        window['kword'].update('')
        window['mensage'].update('')

    elif event == 'descript':
        fim = ''
        n1 = 0
        mensagem = window['mensage'].get()
        senha = window['kword'].get()

        if not mensagem or not senha:
            sg.popup_error('Preencha a mensagem e a chave!')
            continue

        for i in mensagem:
            i_num = ord(i)
            wd_num = ord(senha[n1])
            n = (i_num - wd_num) % 512
            fim += chr(n)
            n1 = (n1 + 1) % len(senha)

        window['result'].update(fim)
        window['kword'].update('')
        window['mensage'].update('')

    elif event == 'copy':
        pyperclip.copy(window['result'].get())

window.close()