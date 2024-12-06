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


## Uso
A presente API tem como objetivo garantir suporte à um ecommerce, especificamente uma loja de camisetas. Para alcançar tal objetivo, foram definidas certas funções com finalidades diferentes. As principais são:

**Registrar produtos**: Essa operação serve para adicionar novos produtos no banco de dados da loja. Para utiliza-la basta enviar uma requisição POST para '/api/camiseta/' contendo no corpo: nome, preco, quantidade, descricao e img (o link para a imagem do produto).
O mesmo caminho, ou seja, '/api/camiseta/', em uma requisição GET retorna como resposta uma lista de todas as camisetas registradas e seus detalhes.

**Criar usuario**: Para criar um novo usuário envie, com o método POST, um json contendo {"username": , "password": , "email": } para "/signup/"

**Login**: Para autenticar um usuario, envie, com o método POST, um json contendo {"username": , "password": } para "/login/". Caso o usuário exista, e as informações estejam corretas, como resposta será recebido um token. Este mesmo token será utilizado nas próximas operações.

### Todas as seguintes operações devem incluir "Authorization: Token \<seu-token\>" na HEADER
**Adicionar ao carrinho**: Usuários podem adicionar itens ao carrinho fazendo uma requisição POST para '/api/carrinho/adicionar\_item/\<int:camiseta\_id\>/', no corpo da requisição, opcionalmente pode ser enviada a quantidade desejada.

**Remover do carrinho**: Seguindo a mesma lógica, caso seja desejado remover algum item do carrinho é possível faze-lo enviando uma requisicao POST para '/api/carrinho/remover\_item/\<int:camiseta\_id\>/', é possível incluir a quantidade no corpo da requisição também.

**Limpar carrinho**: Para remover todos os itens do carrinho basta enviar uma requisição POST para '/api/carrinho/esvaziar/'.

**Realizar compra**: Para concluir a compra envie uma requisição POST para '/api/carrinho/comprar/'. Dessa forma, um novo pedido será criado e o carrinho esvaziado.

**Listar pedidos**: Para visualizar os pedidos existentes, basta enviar uma requisição GET para '/api/pedidos/'.

