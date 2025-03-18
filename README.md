# Nome do Projeto
Projeto do Curso em Desenvolvimento Python para Backend Developer
## Descrição
Vem com a intenção de aprender e registrar todos os comando necessarios para um aprendizado.

## Instalação
Passos para instalar:
```bash
git clone https://github.com/roquelins25/Python_Backend_Developer.git
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


#### Algumas Boas Praticas em Python ####
    Existe um documento PEP8 para seguir um modulo padrão
    Quatro espaços para identação
    limitar linhas a 79 caracteres
    usar nome de variaveis em snake_case #Ex: total_faturado
    CamelCase para Classes #Ex: ContaBancaria
Para Ajudar a Arrumar o Codigo e manter no padrão é possivel usar ferramentas que ajuda com o formação
    Biblioteca flak8 # pip install flak8
        Para executar é somente digitar o codigo ==>  flak8 "Nome do Arquivo"
    Biblioteca black # pip install black
        Para executar é somente digitar o codigo ==> black "Nome do Arquivo"
    Biblioteca isort # pip install black
        Para executar é somente digitar o codigo ==> isort "Nome do Arquivo"

### Banco de Dados com Python ###
Toda tabela tem que ter PK ( Chave Primaria )
1. Existe 2 tipos de chaves - Chave Estrangeira e Chave Primarias
    A Chave Primarias são os IDs que nao pode se repetir ( unicos registros )
    A chave Estrangerias são IDs das chaves primarias de outras tabelas para fazer possiveis Relacionamentos.

2. Tipo Relacionamentos
    um para muitos = relacionamento de um para muitos pode ser dizer que é um relacionamento mais comum. Exemplo: UM cliente pode fazer MUITOS Pedidos
    um para um = relacionamento de um para um pode se dizer que é um relacionamento que tem somente 1 registro, Exemplo: UM cliente tem somente UM documento
    Muito para Muitos = Relacionamentos de muito para muitos usa-se para saber mais de uma informação para relacionar.

3. SQL ( Structured Query Language )
    Linguaguem utilizado para realizar as criações, modificações, consultas, funções dentro de um banco de dados.
    Segue alguns SQL mais utilizados 
    # Criar um novo Banco de Dados
        CREATE DATABASE 'nome do banco';
    # Criar uma tabela para armanezar dados ( nos () colocar os nomes das colunas e seus tipos )
        CREATE TEABLE 'nome da tabela' ( id INTERGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100),preco DECIMAL);
    # Incluir dados na tabela
        INSERT INTO 'nome da tabela' (nome, preco) VALUES ('curso de Python',250.00);
    # Listar os dados
        SELECT * FROM 'nome da tabela';
    # Atualizar dados com ID informado
        UPDATE 'nome da tabela' SET nome='CURSO DE PYTHON PARA INICIANTES' WHERE id = 1; (MUITO IMPORTANTE ESSE UPTDE COLOCAR O WHERE)
    # Excluir dados da tabela
        DELETE FROM 'nome da tabela' WHERE id = 1; (MUITO IMPORTANTE ESSE UPTDE COLOCAR O WHERE)
     SQL NAO EXISTE CTRL + Z

4. DB API
    Utiliza para fazer a conexão com o banco de dados
    Importante é saber qual banco de dados vai ser conectado para colocar o Drive correto quando Usar o DB API (mysql,mariadb,sqlite,sqlserver,oracle...)

    1. Conectar
        import sqlite3
        con = sqlite3.connect('meu banco de dados')  

        Importante ( caso queira criar o BDs dentro de uma pasta ou na mesma pasta do arquivo Python usa o comando,
            from pathlib import path
            ROOT_PATH = Path(__file__).parente
            con = sqlite3.connect(ROOT_PATH / 'meu banco de dados')
            )
    2. Criando Tabela
        cursor.execute("CREATE TABLE clientes (ID INTEGER PRIMARY KEY AUTOINCREMENT,nome VARCHAR(100),email VARCHAR(30))" )
    
    3. Inserindo dados na tabela
    existe dois modos de fazer o INSET esse seria o modo mais correto para nao ter insert desnecessario
        data = ("Gean","gean@gmail.com")
        cursor.execute("INSERT INTO clientes (nome,email) VALUES (?,?);" ,data)
        conexao.commit()


        def Atualizar_registro(conexao,cursor,nome,email,id):
            data = (nome,email,id)
            cursor.execute("UPDATE clientes SET nome = ?, email = ? WHERE ID=? ;" ,data)
            conexao.commit()

        def Deletar_registro(conexao,cursor,id):
            data = (id,)
            cursor.execute("DELETE FROM clientes WHERE ID=? ;" ,data)
            conexao.commit()

        def Inserir_Lote(conexao,cursor,dados):
            cursor.executemany("INSERT INTO clientes (nome,email) VALUES (?,?);" ,dados)
            conexao.commit()

        def Select_dados(cursor,coluna,id):
            cursor.execute("SELECT * FROM clientes WHERE ?=?", (coluna,id))
            return cursor.fetchone()