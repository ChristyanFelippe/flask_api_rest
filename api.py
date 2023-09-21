from flask import Flask, jsonify

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

## GET Purchases
@app.route('/purchases_orders')
def get_purchases_orders():
    return jsonify(purchase_orders)
    
## Get Purchases by id
## Post Purchases order
## Get purchases order itens
## Post Purchases order itens




@app.route('/')
def home():
    return "hello world"


app.run(port=5000)
