from flask import render_template
import ConnectToBase


def create(manager):
    con = ConnectToBase.connect()
    cur = con.cursor()
    # cur.execute(
    #     "DELETE FROM manager *;"  # delete all record
    #     "ALTER SEQUENCE manager_manager_id_seq RESTART WITH 1"  # reboot counter id
    # )
    try:
        cur.execute(
            "INSERT INTO manager (manager_name) VALUES (%(manager_name)s)", {"manager_name": manager}
        )
    except:
        con
    closeCon(con)


def insertRecord(arr, managerName):
    resArr = []
    con = ConnectToBase.connect()
    cur = con.cursor()
    cur.execute(
        "SELECT manager_id FROM manager WHERE manager_name=%(managerName)s", {"managerName": managerName}
    )
    number = cur.fetchall()
    cur.execute(
        "SELECT count_id FROM discart"
    )
    count_id = cur.fetchall()
    cur.execute(
        "SELECT NOW()::DATE"
    )
    date = cur.fetchall()[0][0]
    for i in range(0, len(arr)):
        for j in range(0, len(count_id)):
            if arr[i] == count_id[j][0]:
                arr[i] = 0
        if arr[i] != 0:
            resArr.append(arr[i])
    for i in range(0, len(resArr)):
        cur.execute(
            "INSERT INTO discart (discart_id, count_id, boolean, add_date) VALUES (%(number)s, %(count)s, FALSE, %(date)s)",
            {"number": number[0], "count": resArr[i], "date": date}
        )
    closeCon(con)
    return render_template("success.html", data="Операция выполнена успешно")


def closeCon(con):
    con.commit()
    con.close()
