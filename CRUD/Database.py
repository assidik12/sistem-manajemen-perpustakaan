from . import Operasi

DB_NAME = "data.txt"
TEMPLATE = {
    "key" : "xxxxxx",
    "date_add": "yyyy-mm-dd",
    "judul" : 255*" ",
    "penulis": 255*" ",
    "tahun": "yyyy"
}


def init_console():
    try:
        with open(DB_NAME, "r") as file:
            print("db tersedia")
    except:
        print("db tidak ditemukan, silahkan membuat db baru")
        Operasi.create_frist_data()
            