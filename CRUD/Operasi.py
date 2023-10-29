from . import Database
from .utiliy import random_string
import time

def create_frist_data():

    judul  = input("judul : ")
    penulis  = input("penulis : ")
    tahun  = input("tahun : ")

    data = Database.TEMPLATE.copy()

    data["key"] =random_string(6)
    data["date_add"] = time.strftime("%y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["judul"] =judul + Database.TEMPLATE["judul"][len(judul):]
    data["penulis"] =penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["tahun"] = tahun + Database.TEMPLATE["tahun"][len(tahun):]


    hasil = f'{data["key"]}, {data["date_add"]}, {data["judul"]}, {data["penulis"]}, {data["tahun"]}'
    print(hasil)
    try:
        with open(Database.DB_NAME, "w", encoding="utf-8") as file:
            file.write(hasil)
    except:
        print("gagal")

def read():
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            return content
    except:
        print("database error")
        return False