import PySimpleGUI as sg
from pdf2image import convert_from_path
import webbrowser, os, io
from time import sleep
from PIL import Image, ImageTk
from datetime import datetime

def gerar_capa(path):    
    try:
        image = Image.open(f'{path}{now}{1}.jpg')
        image.thumbnail((300, 300))
        bio = io.BytesIO()
        image.save(bio, format="PNG")
        janela["capa"].update(data=bio.getvalue())
        
    except:
        janela["capa"].update('')

def converter(file, pg):
    images = convert_from_path(file)
    
    try:
        if pg == 'all':
            for i in range(len(images)):
                images[i].save(f'{path}{now}{i+1}.jpg', 'JPEG')
        else:
            images[pg-1].save(f'{path}{now}{1}.jpg', 'JPEG')
            
        janela['-msg-'].update("Página(s) do arquivo convertidas para JPEG...")
    
    except:        
        sg.popup_error('Verifique se você tem o pacote "poppler-utils" \
instalado em seu computador ou a quantidade de páginas de seu arquivo PDF...', title='Erro!!!')
        janela['-msg-'].update('')
        
sg.theme('Reddit')

menu = [
    ['&Arquivo', ['Abrir Arquiv&o','&Cancelar']],
    ['A&juda', ['&Manual do Software', '&Sobre o Autor', ['&Linkedin', '&GitHub']]]
    ]

layout =  [
    [sg.Menu(menu)],    
    [sg.Stretch(), sg.Image('', key='capa', size=(0, 0)), sg.Stretch()],
    [sg.Stretch(), sg.Button('Abrir Arquivo', size=(15, 3)), sg.Button('Cancelar', size=(15, 3)), sg.Stretch()],
    [sg.HorizontalSeparator()],
    [sg.Text('Status'), sg.VerticalSeparator(), sg.Text('', key='-msg-', font=('Verdana', 8))]
    ]

janela = sg.Window('PDF2IMAGE CONVERSOR', layout, resizable=True)

while True:    
    evento, valores = janela.read()
    
    if evento in (sg.WIN_CLOSED, 'Cancelar'):
        break
    
    if evento in ('Manual do Software'):        
        sg.popup('==============MANUAL DO USUÁRIO==============',
               '''=============================================

(1) Abra um arquivo PDF através do menu ou botão [Abrir Arquivo].
(2) No Popup clique em [browse] para navegar até o Diretório/Arquivo.
(3) Com o Arquivo escolhido clique em [Open] e em [Ok]...
(4) Agora clique em [Yes] para Converter todas as páginas ou em [No]
caso queira converter apenas uma determinado página em Imagem...
(5) Agora só Aguardar seu arquivo PDF ser convertida em JPG...
=============================================
''', location=(0,0), title='MANUAL DO USUÁRIO')    
    
    if evento in ('Abrir Arquivo'):        
        janela["capa"].update('')
        janela['-msg-'].update('A Conversão de Arquivos com Várias páginas é demorada...')
        date = str(datetime.now())
        now = date.replace(' ', ':').replace(':', '.').replace('.','-').replace('-','')
        
        try:                        
            file = sg.popup_get_file('Abrir Arquivo PDF', title='Abrir Arquivo', file_types=(("PDF","*.pdf"),("Outros", "*.*"),),)
            path = f'{os.path.normpath(os.path.dirname(file))}/'            
           
        except:            
            sg.popup('Você não escolheu nenhum arquivo PDF para converter em imagem...', title='Arquivo Vazio')           
                 
        if file != None and file != '' and file != './':            
            janela['-msg-'].update(f'Seu PDF Está Sendo Convertido Em Imagem... Aguarde...')            
            status = sg.popup_yes_no('Deseja Converter TODAS as páginas? \nYes = sim e No = para escolher página')
            
            if status == 'Yes':                            
                try:
                    converter(file, 'all')                

                except:
                    sg.popup_error('Vou ficar devendo essa! Não consegui converter seu arquivo em imagens...', title='Sinto muito!')
                
                gerar_capa(path) 
                            
            if status == 'No':
                pg = sg.popup_get_text('Qual página do arquivo você quer converter em imagem?: ')
                
                try:
                    converter(file, int(pg))
                    
                except:
                    sg.popup_error('Vou ficar devendo essa! Não consegui converter seu arquivo em imagens...', title='Sinto muito!')
                
                gerar_capa(path)            
    
    if evento in ('Linkedin'):
        webbrowser.open('https://www.linkedin.com/in/elizeu-barbosa-abreu')
                 
    if evento in ('GitHub'):
        webbrowser.open('https://github.com/elizeubarbosaabreu')
        

janela.close()