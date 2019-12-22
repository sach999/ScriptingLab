from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        msg = "Enter details of items"
        return render_template("index.html", msg=msg)

    if request.method == "POST":
        if request.form["item"] == "" or request.form == "" or request.form["item1"] == "" or request.form["cost1"] == "":
            msg = "Enter all the fields"
            return render_template("index.html", msg=msg)

        if(int(request.form["cost"]) < 0 or int(request.form["cost1"]) < 0):
            msg = "Enter positive amount"
            return render_template("index.html", msg=msg)

        if(int(request.form["cost"]) == 0 or int(request.form["cost1"]) == 0):
            msg = "Cost entered cannnot be 0"
            return render_template("index.html", msg=msg)

        amount = int(request.form["cost"]) + int(request.form["cost1"])
        return render_template("bill.html", amount=amount)


if __name__ == '__main__':
    app.run(host="localhost", port='3000', debug=True)
