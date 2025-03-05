# Nome do Projeto
Projeto do Curso em Desenvolvimento Python para Backend Developer
## Descrição
Vem com a intenção de aprender e registrar todos os comando necessarios para um aprendizado.

## Instalação
Passos para instalar:
```bash
git clone https://github.com/roquelins25/Python-Backend-Developer.git
cd developer

### Alguns Comandos quando cria novo arquivos
1 - Ambiente Virtual
    Sempre trabalhar com ambientes Vituais para ter as versões correta de cada biblioteca que esteje utilizando para evitar conflitos.
    Para Criar ambientes Virtuais siga o passo a passo
    1- pip venv -m "Nome do Arquivo"
    2- .venv/script/activate ( Para Ativar o Ambiente Virtual)
    3- Instalar as Bibliotecas necessarias
    4- pip freeze > requeriments.txt ( Muito importante para armazenar os dados das versões das suas Bibliotecas)
    5- Desactivate ( Sair do ambiente virtual)
    *Ponto muito importante é sempre que for instalar uma biblioteca nova tera que acessar o ambiente virtual*

    Alguns Comandos importantes sobre o PIP
    #Instalar Pacotes
        pip install nome_pacote
    #Desinstalar pacotes
        pip unistall nome_pacote
    # Listar Pacotes Instalados
        pip list
    # Atualizar Pacotes
        pip install --upgrade nome_pacote

2 - Versionamento do Codigo com GitHub
    Utilizei o Versionamento do codigo para ir ja aprendendo a usar o Git e Github no Dia a Dia.O principal objetivo do github é para ter versoes do codigo sempre que necessario para compartilhamentos e construções.
    Foi seguido alguns passos para criação do repositório no GitHub
    
    # Inicializar o repositório (se ainda não for um repositório Git)
    git init

    # Adicionar os arquivos ao Git
    git add .

    # Criar um commit inicial
    git commit -m "Primeiro commit"

    # Adicionar o repositório remoto
    git remote add origin https://github.com/seu-usuario/nome-do-repositorio.git ( Link encontra-se no github)

    # Enviar os arquivos para o GitHub
    git push -u origin main

    * Quando temos um ponto importante no codigo sempre realizaremos um Git Commit e daremos um Push para o github - tendo assim uma marca histórica como se fosse um checkpoint para a proxima fase.

    !Um ponto muito importante é usar o GitIgnore para ignorar a pasta VENV para nao subir para o repositório
