import ConnectToBase


def dropList():
    con = ConnectToBase.connect()
    cur = con.cursor()
    cur.execute(
        "SELECT manager_name FROM manager"
    )
    result = cur.fetchall()
    con.commit()
    con.close()
    return result
