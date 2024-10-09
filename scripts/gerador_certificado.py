from fpdf import FPDF
import pandas as pd
import pyautogui
import webbrowser
import pyperclip
import time
import os

# Caminho com os dados
dados = pd.read_csv("../banco_dados/base_dados.csv", sep=',')
if dados.empty:
    print("A base de dados está vazia ou o arquivo não foi encontrado.")
    exit()

# Caominho com a fonte que será usada
font_path = '../fontes/PINYONSCRIPT-REGULAR.TTF'
if not os.path.exists(font_path):
    print(f"Fonte não encontrada: {font_path}")
    exit()

# Caminho do template
template_path = '../certificado/template.png'
if not os.path.exists(template_path):
    print(f"Template não encontrado: {template_path}")
    exit()

# 96 DPI é um valor padrão para muitas telas e interfaces digitais.
dpi = 96
# Dimensões em pixels do template
largura_pixels = 2000
altura_pixels = 1414

# Convertendo pixels para milímetros
largura_mm = (largura_pixels * 25.4) / dpi
altura_mm = (altura_pixels * 25.4) / dpi

def gera_certificado():
    '''
    Função que irá criar um Certificado personalizado com o nome do aluno no formato de PDF.
    '''
    for i in dados.index:
        # Criando uma nova instância do FPDF para cada PDF
        pdf = FPDF(format=(largura_mm, altura_mm))
        pdf.add_page()

        # Adicionar o template de imagem e configurar fonte
        pdf.image(template_path, x=0, y=0, w=largura_mm, h=altura_mm)
        pdf.add_font('Pinyon Script Regular', '', font_path, uni=True)
        pdf.set_font('Pinyon Script Regular', '', 72)
        pdf.set_text_color(162, 116, 48)

        # Obter o nome e calcular a largura do texto
        nome = str(dados.loc[i, "Nome"])
        largura_texto = pdf.get_string_width(nome)

        # Calcular a posição x para centralizar o nome
        x = (largura_mm - largura_texto) / 2
        y = 180

        # Adicionar o texto ao PDF
        pdf.text(x, y, nome)

        # Salvar o PDF com o nome do aluno no certificado
        pdf_output_path = f"../Certificado_{nome}.pdf"
        pdf.output(pdf_output_path)
        print(f"Certificado gerado: {pdf_output_path}") #Quando finalizado, irá gerar uma mensagem no terminal informando que o pdf foi gerado com sucesso.


def envia_email():
    '''
    Função de enviar e-mail automatico com um texto personalizado com o nome do aluno e o seu certificado Certificado.
    '''
    #Percorrendo a base de dados csv para gerar o Cerficado.
    time.sleep(4)
    for i in dados.index:
        nome = str(dados.loc[i, "Nome"]) #Variavel recebe o nome do aluno de acordo com a base de dados
        destinatario = str(dados.loc[i, "Email"]) #Variavel que irá guardar o e-mail que será enviado o Certificado.
        pdf_path = f"../Certificado_{nome}.pdf"

        # Constroe oum caminho completo absoluto do PDF
        pdf_output_path = os.path.abspath(pdf_path)

        # Verificar se o arquivo PDF existe antes de tentar anexá-lo
        if not os.path.exists(pdf_output_path):
            print(f"Arquivo não encontrado: {pdf_output_path}")
            continue

        # Abre o Gmail
        webbrowser.open("https://mail.google.com")
        time.sleep(8) #Os valores usados no time podem ser modificados visando a velocidade da internet e da maquina que será utilizada

        # Clique no botão de composição de novo e-mail
        pyautogui.click(x=81, y=171)
        time.sleep(4)

        # Preenche o destinatário
        pyautogui.write(destinatario)
        pyautogui.press('tab')
        pyautogui.press('tab')
        time.sleep(2)

        # Preenche o assunto
        assunto = "CERTIFICADO DO CURSO \"Introdução a Python\" - Coding Courses"
        pyperclip.copy(assunto)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press('tab')
        time.sleep(2)

       # Preencher o corpo do e-mail
        mensagem = f"""
        Olá {nome}!

        Espero que esta mensagem o(a) encontre bem.

        É com grande alegria que informamos que você concluiu com sucesso o curso de Introdução a Python! Parabéns pela sua dedicação e esforço ao longo dessa jornada.

        Como reconhecimento pela sua conquista, estamos enviando em anexo o seu certificado de conclusão.

        Se tiver alguma dúvida ou precisar de mais informações, não hesite em nos contactar. Estamos sempre à disposição para ajudar.

        Desejamos muito sucesso em suas futuras empreitadas e esperamos que as habilidades adquiridas neste curso sejam valiosas para você em sua trajetória profissional.


        Atenciosamente,

        Equipe Coding Courses
        """
        # Remove os espaços da mensagem devido a indentação do for
        cleaned_mensagem = '\n'.join(line.strip() for line in mensagem.strip().split('\n'))

        # Cola a mensagem no corpo do e-mail
        pyperclip.copy(cleaned_mensagem)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(3)

        # Clica no botão para anexiar arquivo
        pyautogui.click(x=1419, y=1002)
        time.sleep(3)

        # Usa o caminha absoluto do PDF
        pyperclip.copy(pdf_output_path)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(3)

        # Procura o certificado com o nome da pessoa
        pyautogui.write("pdf_path")
        pyautogui.press('enter')
        time.sleep(10)  # Tempo de espera maior para aguarda o upload do arquivo no e-mail

        # Envia o e-mail usando o botão de atalho do gmail
        pyautogui.hotkey('ctrl', 'enter')
        time.sleep(6)
        print(f"E-mail enviado para {destinatario}") #Quando finalizado irá gerar uma mensagem no terminal informando que o e-mail foi enviado com sucesso.

gera_certificado()
envia_email()
