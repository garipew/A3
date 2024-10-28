# A3
## Instalação
Para instalar é necessário primeiro criar um ambiente virtual e instalar o Django.<br/>
Windows:
```
py -m venv env
cd env
Scripts\activate.bat
git clone https://github.com/garipew/A3.git camisas
```
Unix:
```
python3 -m venv env
cd env
source bin/activate
git clone https://github.com/garipew/A3.git camisas
```

Em seguida, é necessário instalar as dependencias com:
```
cd camisas
pip install -r requirements.txt
```

## Execução
Para executar basta seguir a forma usual do Django:<br/>
Windows:
```
py manage.py runserver
```
Unix:
```
python3 manage.py runserver
```
