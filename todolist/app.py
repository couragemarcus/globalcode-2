
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


# Temporary task storage
tasks = [
    {
        "id": 1,
        "title": "Complete Python assignment",
        "completed": False
    },
    {
        "id": 2,
        "title": "Study for exam",
        "completed": False
    }
]


# HOME - READ
@app.route("/")
def home():

    return render_template("index.html", tasks=tasks)


# ADD TASK - CREATE
@app.route("/tasks/add", methods=["GET", "POST"])
def add_task():

    if request.method == "POST":

        title = request.form["title"]

        new_task = {
            "id": len(tasks) + 1,
            "title": title,
            "completed": False
        }

        tasks.append(new_task)

        return redirect("/")

    else:

        return render_template("add_task.html")


# EDIT TASK - UPDATE
@app.route("/tasks/edit/<int:id>", methods=["GET", "POST"])
def edit_task(id):

    task = None

    # Find the task
    for item in tasks:

        if item["id"] == id:

            task = item

            break

        else:

            continue


    # Check if task exists
    if task is None:

        return "Task not found", 404

    else:

        # Update the task
        if request.method == "POST":

            task["title"] = request.form["title"]

            return redirect("/")

        else:

            return render_template(
                "edit_task.html",
                task=task
            )


# COMPLETE TASK - UPDATE
@app.route("/tasks/complete/<int:id>")
def complete_task(id):

    for task in tasks:

        if task["id"] == id:

            task["completed"] = True

            break

        else:

            continue

    return redirect("/")


# DELETE TASK - DELETE
@app.route("/tasks/delete/<int:id>")
def delete_task(id):

    task_found = False

    for task in tasks:

        if task["id"] == id:

            tasks.remove(task)

            task_found = True

            break

        else:

            continue


    if task_found:

        return redirect("/")

    else:

        return "Task not found", 404


# ABOUT
@app.route("/about")
def about():

    return render_template("about.html")


# RUN APPLICATION
if __name__ == "__main__":

    app.run(debug=True)

else:

    print("Flask application imported.")

