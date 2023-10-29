from . import Operasi

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
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} {judul:.40} {penulis:.40} {tahun:5}", end="")


    #footer
    print("\n"+"="*100)