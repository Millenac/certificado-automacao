# Certificado Automação

## Descrição

O projeto **Certificado Automação** é uma ferramenta desenvolvida em Python para gerar e enviar certificados personalizados automaticamente via e-mail. Através da leitura de uma base de dados em formato CSV, o programa cria certificados em PDF com os nomes dos alunos e envia-os para os respectivos e-mails.

## Funcionalidades

- **Geração de Certificados**: Cria certificados personalizados a partir de um template e os salva em formato PDF.
- **Envio Automático de E-mails**: Envia os certificados gerados diretamente para os e-mails dos alunos.
- **Personalização**: Mensagens e informações do certificado podem ser facilmente personalizadas.

## Tecnologias Utilizadas

- **Python 3**: Linguagem de programação utilizada para desenvolver todo o projeto, aproveitando suas bibliotecas para manipulação de dados e automação.

- **Pandas**: Utilizada para ler e manipular a base de dados em formato CSV. Facilita a extração de nomes e e-mails dos alunos, permitindo o acesso fácil a esses dados.

- **FPDF**: Biblioteca utilizada para gerar documentos PDF. Ela é responsável pela criação dos certificados, permitindo a inserção de texto, imagens (como o template do certificado) e formatação de fonte.

- **PyAutoGUI**: Usada para automação da interface gráfica, permitindo o envio automático de e-mails pelo Gmail. O PyAutoGUI simula cliques e digitação, interagindo com a interface do usuário de forma programática.

- **Webbrowser**: Utilizada para abrir o navegador da web e acessar o Gmail, permitindo que o script inicie o processo de envio de e-mails de forma automatizada.

- **Time**: Biblioteca padrão do Python que permite controlar o tempo de espera entre as ações automáticas, garantindo que as interações com a interface gráfica ocorram de forma sincronizada e evitando erros devido à velocidade de execução.


## Estrutura do Projeto

Automação Certificado/ │ ├── banco_dados/ │ └── base_dados_copy.csv # Base de dados com nomes e e-mails dos alunos │ ├── certificados/ │ └── template.png # Imagem do template do certificado │ ├── fontes/ │ └── PINYONSCRIPT-REGULAR.TTF # Fonte utilizada no certificado │ └── scripts/ └── automacao_certificado.py # Script principal do projeto



## Como Usar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu_usuario/certificado_automacao.git
   cd certificado_automacao/scripts
   
2. Instale as dependências: Certifique-se de ter o Python instalado e as bibliotecas necessárias. Você pode instalar as dependências usando o pip:
   ```bash
   pip install pandas fpdf pyautogui

3. Configure a Base de Dados: Adicione os nomes e e-mails dos alunos no arquivo base_dados_copy.csv dentro da pasta banco_dados.
4. Configure o Template: Coloque sua imagem do template do certificado na pasta certificados e a fonte na pasta fontes.
5. Execute o Script: Execute o script principal para gerar e enviar os certificados:
   ```bash
   python automacao_certificado.py
