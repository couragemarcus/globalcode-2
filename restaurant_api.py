from flask import Flask, jsonify, request

app = Flask(__name__)


# Restaurant menu data
menu = [
    {
        "id": 1,
        "name": "Jollof Rice",
        "category": "Main Meal",
        "price": 45.00,
        "available": True
    },
    {
        "id": 2,
        "name": "Fried Rice and Chicken",
        "category": "Main Meal",
        "price": 50.00,
        "available": True
    },
    {
        "id": 3,
        "name": "Banku and Tilapia",
        "category": "Main Meal",
        "price": 70.00,
        "available": True
    },
    {
        "id": 4,
        "name": "Pizza",
        "category": "Fast Food",
        "price": 80.00,
        "available": True
    },
    {
        "id": 5,
        "name": "Coca Cola",
        "category": "Drink",
        "price": 15.00,
        "available": True
    }
]


# Home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Restaurant API"
    })


# 1. Get all menu items
@app.route("/api/menu", methods=["GET"])
def get_menu():
    return jsonify(menu)


# 2. Get one menu item
@app.route("/api/menu/<int:item_id>", methods=["GET"])
def get_menu_item(item_id):

    item = next(
        (item for item in menu if item["id"] == item_id),
        None
    )

    if item is None:
        return jsonify({
            "message": "Menu item not found"
        }), 404

    return jsonify(item)


# 3. Add a new menu item
@app.route("/api/menu", methods=["POST"])
def add_menu_item():

    data = request.get_json()

    new_item = {
        "id": len(menu) + 1,
        "name": data["name"],
        "category": data["category"],
        "price": data["price"],
        "available": data.get("available", True)
    }

    menu.append(new_item)

    return jsonify({
        "message": "Menu item added successfully",
        "item": new_item
    }), 201


# 4. Update a menu item
@app.route("/api/menu/<int:item_id>", methods=["PUT"])
def update_menu_item(item_id):

    item = next(
        (item for item in menu if item["id"] == item_id),
        None
    )

    if item is None:
        return jsonify({
            "message": "Menu item not found"
        }), 404

    data = request.get_json()

    item["name"] = data.get("name", item["name"])
    item["category"] = data.get("category", item["category"])
    item["price"] = data.get("price", item["price"])
    item["available"] = data.get("available", item["available"])

    return jsonify({
        "message": "Menu item updated successfully",
        "item": item
    })


# 5. Delete a menu item
@app.route("/api/menu/<int:item_id>", methods=["DELETE"])
def delete_menu_item(item_id):

    item = next(
        (item for item in menu if item["id"] == item_id),
        None
    )

    if item is None:
        return jsonify({
            "message": "Menu item not found"
        }), 404

    menu.remove(item)

    return jsonify({
        "message": "Menu item deleted successfully"
    })


if __name__ == "__main__":
    app.run(debug=True)