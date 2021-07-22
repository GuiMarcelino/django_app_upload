# WEB Upload Files:

## Desafio velow ##
Aplicação web que captura dados de um determinado arquivo, normaliza os dados armazena no banco (sqlite) faz o cálculo dos campos `(item_price)` / `(purchase_count)` e retorna valor bruto total de vendas para pagina web.


Arquivo utilizado de exemplo está no código.   
namefile = `example_input().tab` 



# Como Rodar o projeto:

Primeiro comando para criar o ambiente virtual e instalar todos os pacotes necessários:

`pipenv install`

Segundo comando para entrar no ambiente virtual:

`pipenv shell`

Terceiro comando para criar e migrar o banco de dados:

`python manage.py migrate`

Quarto comando para rodar o servidor:

`python manage.py runserver`

o servidor deve estar rodando no link: `localhost:8000`
