import ConnectToBase


def create():
    resultManager = []
    resultDiscart = []
    con = ConnectToBase.connect()
    cur = con.cursor()
    cur.execute(
        "SELECT manager_id FROM manager"
    )
    number = cur.fetchall()
    for i in range(0, len(number)):
        cur.execute(
            "SELECT manager_name FROM manager WHERE manager_id=%(number)s", {"number": number[i]}
        )
        resultManager.append(cur.fetchall())
        cur.execute(
            "SELECT count_id FROM discart WHERE discart_id=%(number)s", {"number": number[i]}
        )
        resultDiscart.append(cur.fetchall())
    con.commit()
    con.close()
    data = {
        "resultManager": resultManager,
        "resultDiscart": resultDiscart
    }
    return data
