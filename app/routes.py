from flask import request, jsonify
from app import app, mongo

# Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    if 'name' not in data or 'description' not in data:
        return jsonify({'error': 'Both name and description are required fields'}), 400

    items_collection = mongo.db.items
    item_id = items_collection.insert_one(data).inserted_id

    return jsonify({'message': 'Item created successfully', 'item_id': str(item_id)}), 201

# Get all items
@app.route('/items', methods=['GET'])
def get_items():
    items_collection = mongo.db.items
    items = list(items_collection.find({}, {'_id': 0}))
    return jsonify({'items': items})

# Get an item by ID
@app.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    items_collection = mongo.db.items
    item = items_collection.find_one({'_id': item_id}, {'_id': 0})

    if not item:
        return jsonify({'error': 'Item not found'}), 404

    return jsonify(item)

# Update an item by ID
@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()

    items_collection = mongo.db.items
    result = items_collection.update_one({'_id': item_id}, {'$set': data})

    if result.modified_count == 0:
        return jsonify({'error': 'Item not found'}), 404

    return jsonify({'message': 'Item updated successfully'})

# Delete an item by ID
@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    items_collection = mongo.db.items
    result = items_collection.delete_one({'_id': item_id})

    if result.deleted_count == 0:
        return jsonify({'error': 'Item not found'}), 404

    return jsonify({'message': 'Item deleted successfully'})
