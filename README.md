# Desafio-2-Backend

Nome do Projeto: desafio_2

A aplicação tem por objetivo receber arquivos CNAB contendo transações financeiras de várias lojas e armazená-los em um banco de dados 

Foram utilizados Python. Django, DjangoRestFramework, HTML

Criação de ambiente virtual
python -m venv venv

Iniciando ambiente virtual
(Windows)
.\venv\Scripts\activate
(Linux)
source venv/bin/activate

Instalação de dependencias
pip install -r requirements.txt

Execução de Migrations
python manage.py makemigrations
python manage.py migrate

Execução de Servidor
python manage.py runserver