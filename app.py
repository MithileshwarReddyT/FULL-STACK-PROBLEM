# app.py

from flask import Flask, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)
# Sample data for dishes
dishes = [
    {
        'dishId': 1,
        'dishName': 'Jeera Rice',
        'imageUrl': 'https://nosh-assignment.s3.ap-south-1.amazonaws.com/jeera-rice.jpg',
        'isPublished': False
    
    },
    {
        'dishId': 2,
        'dishName': 'Paneer Tikka',
        'imageUrl': 'https://nosh-assignment.s3.ap-south-1.amazonaws.com/paneer-tikka.jpg',
        'isPublished': True
    },
    {
        'dishId': 3,
        'dishName': 'Rabdi',
        'imageUrl': 'https://nosh-assignment.s3.ap-south-1.amazonaws.com/rabdi.jpg',
        'isPublished': True
    },
    {
        'dishId': 4,
        'dishName': 'Chicken Biryani',
        'imageUrl': 'https://nosh-assignment.s3.ap-south-1.amazonaws.com/chicken-biryani.jpg',
        'isPublished': True
    },
    {
        'dishId': 5,
        'dishName': 'Alfredo Pasta',
        'imageUrl': 'https://nosh-assignment.s3.ap-south-1.amazonaws.com/alfredo-pasta.jpg',
        'isPublished': True
    }
]

@app.route('/api/dishes', methods=['GET'])
def get_dishes():
    return jsonify(dishes)

@app.route('/api/dishes/<int:dish_id>/toggle', methods=['POST'])
def toggle_dish(dish_id):
    for dish in dishes:
        if dish['dishId'] == dish_id:
            dish['isPublished'] = not dish['isPublished']
            return jsonify(dish)
    return jsonify({'error': 'Dish not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
