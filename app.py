from flask import Flask,jsonify,request

app=Flask(__name__)

books=[]

@app.route('/')
def home():
    return "Library API is running"

@app.route('/books',methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books',methods=['POST'])

def add_book():
    data = request.json

    book = {
        "id": len(books) + 1,
        "title": data["title"],
        "author": data["author"]
    }

    books.append(book)

    return jsonify(book), 201

@app.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    for book in books:
        if book["id"] == id:
            return jsonify(book)

    return jsonify({"message": "Book not found"}), 404

@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    data = request.json

    for book in books:
        if book["id"] == id:
            book["title"] = data.get("title", book["title"])
            book["author"] = data.get("author", book["author"])

            return jsonify(book)

    return jsonify({"message": "Book not found"}), 404

@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    for book in books:
        if book["id"] == id:
            books.remove(book)
            return jsonify({"message": "Book deleted"})

    return jsonify({"message": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)