from flask import Flask, render_template, request, url_for
import random
import createManager
import dropList
import json
import activationCart
import ConnectToBase

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        return render_template("generation.html")
    else:
        return render_template("index.html")


@app.route("/manager", methods=['POST', 'GET'])
def manager():
    if request.method == "POST":
        manager = request.form["manager"]
        createManager.create(manager)
        return render_template("success.html", data="Менеджер успешно добавлен")
    else:
        return render_template("manager.html")


@app.route("/generation")
def generation():
    arr = list()
    for i in range(0, 9):
        arr.append(random.randrange(100000, 999999999))
    return render_template("generation.html", result=arr)


@app.route("/assign", methods=['POST', 'GET'])
def assign():
    if request.method == "POST":
        if len(request.form) == 1:
            return json.dumps(dropList.dropList())
        else:
            arr = list()
            for i in range(int(request.form["countid1"]), int(request.form["countid2"])):
                arr.append(i)
            return createManager.insertRecord(arr, request.form['Manager'])
    else:
        con = ConnectToBase.connect()
        cur = con.cursor()
        cur.execute(
            "SELECT manager_name FROM manager"
        )
        data = cur.fetchall()
        return render_template("assign.html", data=data)


@app.route("/activation", methods=['POST', 'GET'])
def activation():
    if request.method == "POST":
        count_id = request.form["count_id"]
        data = activationCart.activation(count_id)
        return render_template("success.html", data=data)
    else:
        return render_template("activation.html")


@app.route("/information", methods=['POST', 'GET'])
def information():
    con = ConnectToBase.connect()
    cur = con.cursor()
    cur.execute(
        "SELECT manager_name FROM manager"
    )
    data = cur.fetchall()
    if request.method == "POST":
        manager = request.form["manager"]
        cur.execute(
            "SELECT manager_id FROM manager WHERE manager_name=%(manager)s", {'manager': manager}
        )
        id = cur.fetchall()
        cur.execute(
            "SELECT count_id, add_date, boolean FROM discart WHERE discart_id=%(id)s", {'id': id[0][0]}
        )
        info = cur.fetchall()
        return render_template("information.html", data=data, info=info, manager=manager)
    else:
        return render_template("information.html", data=data, info='', manager='')


@app.route("/settings")
def settings():
    return render_template("settings.html")


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)

