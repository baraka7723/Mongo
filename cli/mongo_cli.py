import requests
import json

API_ENDPOINT = 'http://api-container:6000'

# Function to create a document from a JSON file
def create_document_from_file():
    file_path = input("Enter the path to the JSON file: ")
    try:
        with open(file_path, 'r') as file:
            document = json.load(file)

        response = requests.post(f"{API_ENDPOINT}/documents", json=json.dumps(document))
        if response.status_code == 201:
            created_document = response.json()
            document_id = created_document['_id']
            print(f"Document created successfully with ID: {document_id}")
        else:
            print("Failed to create document.")
    except FileNotFoundError:
        print("File not found.")

# Function to update a document
def update_document():
    document_id = input("Enter the document ID to update: ")
    document = input("Enter the updated document: ")
    response = requests.put(f"{API_ENDPOINT}/documents/{document_id}", json=document)
    if response.status_code == 200:
        print("Document updated successfully.")
    else:
        print("Failed to update document.")

# Function to delete a document
def delete_document():
    document_id = input("Enter the document ID to delete: ")
    response = requests.delete(f"{API_ENDPOINT}/documents/{document_id}")
    if response.status_code == 200:
        print("Document deleted successfully.")
    else:
        print("Failed to delete document.")

# Function to select documents
def select_documents():
    response = requests.get(f"{API_ENDPOINT}/documents")
    if response.status_code == 200:
        documents = response.json()
        for document in documents:
            document_id = document['_id']
            del document['_id']
            print(f"Document ID: {document_id}")
            print(json.dumps(document, indent=4))
            print()
    else:
        print("Failed to retrieve documents.")

# Main loop
while True:
    print("Select an option:")
    print("1. Create a document from file")
    print("2. Update a document")
    print("3. Delete a document")
    print("4. Select documents")
    print("5. Exit")

    option = input("Enter your choice: ")
    if option == '1':
        create_document_from_file()
    elif option == '2':
        update_document()
    elif option == '3':
        delete_document()
    elif option == '4':
        select_documents()
    elif option == '5':
        break
    else:
        print("Invalid option. Try again.")

