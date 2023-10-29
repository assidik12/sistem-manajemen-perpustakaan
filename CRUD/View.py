from . import Operasi

def create_console():
    print("\n\n"+"="*100)
    print("silahkan tambah buku\n")
    penulis = input("masukan nama penulis : ")
    judul = input("masukan judul buku : ")
    while(True):
        try:
            tahun = int(input("masukan tahun : "))
            if len(str(tahun)) == 4:
                break
            else:
                print("tahun harus angka, silahkan input tahun lagi!!")
        except:
            print("tahun harus angka, silahkan input tahun lagi!!")
    Operasi.create(tahun, judul, penulis)
    print("berikut data baru anda")
    read_console()

def read_console():
    data_file = Operasi.read()
    index  ="nomor"
    penulis  ="penulis"
    judul  ="judul"
    tahun ="tahun"

#header
    print("\n"+ "="*100)
    print(f"{index:4} {judul:40} {penulis:40} {tahun:5}")
    print("-"*100)
    #data
    for index, data in enumerate(data_file):
        data_break = data.split(",")
        key = data_break[0]
        date_add = data_break[1]
        judul = data_break[2]
        penulis = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} {judul:.40} {penulis:.40} {tahun:5}", end="")


    #footer
    print("\n"+"="*100)