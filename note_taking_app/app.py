from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form["note"]
        notes.append(note)
        return redirect(url_for("index"))
    else:
        set_notes=set(notes)
        return render_template("home.html", notes=set_notes)

@app.route("/clear", methods=["POST"])
def clear():
    notes.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)