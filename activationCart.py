import ConnectToBase


def activation(count_id):
    con = ConnectToBase.connect()
    cur = con.cursor()
    # cur.execute(
    #     "DELETE FROM discart *;"  # delete all record
    #     #"ALTER SEQUENCE discart_count_id_seq RESTART"  # reboot discart_id
    # )
    cur.execute(
        "SELECT count_id, boolean FROM discart WHERE count_id=%(count_id)s", {"count_id": count_id}
    )
    arr = cur.fetchall()
    try:
        arr[0][0] == count_id
        if arr[0][1] == False:
            data = "Операция совершена успешно"
        else:
            data = "Карта уже активирована"
    except:
        data = "Ошибка при активации карты"

    cur.execute(
        "UPDATE discart SET boolean=true WHERE count_id=%(count_id)s", {"count_id": count_id}
    )
    con.commit()
    con.close()
    return data