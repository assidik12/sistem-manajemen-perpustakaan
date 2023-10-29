from . import Database
from .utiliy import random_string
import time


def create(tahun, judul, penulis):

    data = Database.TEMPLATE.copy()

    data["key"] =random_string(6)
    data["date_add"] = time.strftime("%y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["judul"] =judul + Database.TEMPLATE["judul"][len(judul):]
    data["penulis"] =penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["tahun"] = str(tahun)
    hasil = f'{data["key"]}, {data["date_add"]}, {data["judul"]}, {data["penulis"]}, {data["tahun"]}'

    try:
        with open(Database.DB_NAME, "a", encoding="utf-8") as file:
            file.write(f"{hasil}\n")
    except:
        print("data gagal di tambahkan, coba lagi!!!")


def create_frist_data():

    judul  = input("judul : ")
    penulis  = input("penulis : ")
    while(True):
            try:
                tahun = int(input("masukan tahun : "))
                if len(str(tahun)) == 4:
                    break
                else:
                    print("tahun harus angka, silahkan input tahun lagi!!")
            except:
                print("tahun harus angka, silahkan input tahun lagi!!")

    data = Database.TEMPLATE.copy()

    data["key"] =random_string(6)
    data["date_add"] = time.strftime("%y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["judul"] =judul + Database.TEMPLATE["judul"][len(judul):]
    data["penulis"] =penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["tahun"] = str(tahun)


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