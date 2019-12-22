from flask import Flask, render_template, request, url_for
import time
import re
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        msg = "Enter the details"
        return render_template("index.html", msg=msg)

    if request.method == "POST":
        if request.form["usn"] == "" or request.form["dob"] == "" or request.form["marks1"] == "" or request.form["marks2"] == "" or request.form["marks3"] == "":
            msg = "Enter the fields"
            return render_template("index.html", msg=msg)

        try:
            time.strptime(request.form["dob"], "%d/%m/%Y")
        except ValueError:
            msg = "Invalid dob"
            return render_template("index.html", msg=msg)

        usn_format = "^[1][A-Z][A-Z][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9]$"
        if not re.match(usn_format, request.form["usn"]):
            msg = "Invalid usn"
            return render_template("index.html", msg=msg)

        if int(request.form["marks1"]) < 0 or int(request.form["marks2"]) < 0 or int(request.form["marks3"]) < 0:
            msg = "Enter valid marks"
            return render_template("index.html", msg=msg)

        avg = (int(request.form["marks1"]) +
               int(request.form["marks2"])+int(request.form["marks2"]))/3
        l = [request.form["usn"], request.form["dob"]]
        return render_template("success.html", avg=avg, l=l)


if __name__ == "__main__":
    app.run(host="localhost", port="3000", debug=True)
