from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/helo/<name>')
def home(name):
    return f"hello {name} you are in ghana!"

@app.route('/ghana')
def ghana():
    return {"country": "Ghana",
        "capital": "Accra",
        "population": 31072940,
        "currency": "Ghanaian cedi"
    }
@app.route("/site")
def site():
    return "<h1>Welcome to my website</h1><p>This is a sample website built using Flask.</p><ol><li>Home</li><li>About</li><li>Contact</li></ol>"

@app.route("/site1")
def site1():
    user={
        "name": "marcus",
        "age": 30,
        "location": "Ghana"
    }
    return render_template("index.html",  user_names=user)


@app.route("/open/<name>")
def open(name):
    return render_template("index.html", user_name=name, data="user data")

@app.route("/open1/<name>", methods=["GET", "POST"])
def open1(name):
    user_names = ["Alice", "Bob", "Charlie"]
    if request.method == "POST":
        name = request.form.get("user_Name")
        user_names.append(name)
        return render_template("index.html", user_name=name, user_names=user_names)
    else:
        return "it is a get request"
    

if __name__ == '__main__':
    app.run(debug=True) 
