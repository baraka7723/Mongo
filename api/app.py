from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
username = 'admin'
password = 'secret'
client = MongoClient(f'mongodb://{username}:{password}@mongo-container:27017')
db = client['mydatabase']
collection = db['mycollection']

@app.route('/documents', methods=['POST'])
def create_document():
    document = request.get_json()
    result = collection.insert_one(document)
    if result.inserted_id:
        document['_id'] = str(result.inserted_id)
        return jsonify(document), 201
    else:
        return jsonify(error='Failed to create document.'), 500

@app.route('/documents/<document_id>', methods=['PUT'])
def update_document(document_id):
    document = request.get_json()
    result = collection.update_one({'_id': document_id}, {'$set': document})
    if result.modified_count > 0:
        return jsonify(message='Document updated successfully.'), 200
    else:
        return jsonify(error='Failed to update document.'), 404

@app.route('/documents/<document_id>', methods=['DELETE'])
def delete_document(document_id):
    result = collection.delete_one({'_id': document_id})
    if result.deleted_count > 0:
        return jsonify(message='Document deleted successfully.'), 200
    else:
        return jsonify(error='Failed to delete document.'), 404

@app.route('/documents', methods=['GET'])
def select_documents():
    documents = list(collection.find())
    if documents:
        for document in documents:
            document['_id'] = str(document['_id'])
        return jsonify(documents), 200
    else:
        return jsonify(error='No documents found.'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
