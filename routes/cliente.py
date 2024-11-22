from flask import Blueprint,render_template

cliente_route = Blueprint('cliente', __name__)

"""
Rotas de Clientes

     - /clientes/ (GET) - Listar os clientes
     - /clientes/ (POSST) - inserir o cliente no servidor
     - /cleintes/new (GET) - renderizar o formulario para criar um cliente
     - /clientes/<id> (GET) - obter os dados de um cliente 
     - /clientes/<id>/edit (GET) - renderizar um formulario para editar um cliente
     - /clientes/<id>/update (PUT) - atualizar os dados do cliente
     - /clientes/<id>/delete (DELETE) - deleta o registro do usuario 
"""

@cliente_route.route('/')
def lsita_clientes():
    """Listar os clientes"""
    return render_template('lista_clientes.html')


@cliente_route.route('/', methods=['POST'])
def inserir_cleinte():
    """Inserir os dados Clientes"""
    pass


@cliente_route.route('/new')
def form_cleinte():
    """Formulario para cadastrar um cliente"""
    return render_template('form_cliente.html')


@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """exibir detalhes do cliente"""
    return render_template('detalhe_cliente.html')

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """Formulario para editar um cliente"""
    return render_template('form_edit_cliente.html')

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """atualizar informacoes do cliente"""
    pass 

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    """atualizar informacoes do cliente"""
    pass   