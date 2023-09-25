from flask import Flask, jsonify, request

app = Flask(__name__)

purchase_orders = [
    {
        'id': 1,
        'description': 'Pedido de compra',
        'itens': [
            {
                'id': 1,
                'description': 'Descrição do item',
                'price': 20.00
            }
        ]
    }
]

# GET Purchases


@app.route('/purchases_orders')
def get_purchases_orders():
    return jsonify(purchase_orders)

# Get Purchases by id


@app.route('/purchases_orders/<int:id>')
def get_purchases_order_by_id(id):
    for po in purchase_orders:
        if (po.get('id') == id):
            return jsonify(po)
    return (jsonify({'message': f' ID {id} não encontrado'}))


# Post Purchases order

@app.route('/purchase_orders', methods=['POST'])
def create_purchase_order():
    request_data = request.get_json()
    purchase_order = {
        'id': request_data['id'],
        'description': request_data['description'],
        'itens': []
    }

    purchase_orders.append(purchase_order)

    return jsonify(purchase_order)

# Get order itens

@app.route('/purchases_orders/<int:id>/itens')
def get_order_itens(id):
    for po in purchase_orders:
        if (po.get('id') == id):
            return jsonify(po.get('itens'))
    return (jsonify({'message': f' ID {id} não encontrado'}))


# Post Purchases order itens


@app.route('/')
def home():
    return "hello world"


app.run(port=5000)
