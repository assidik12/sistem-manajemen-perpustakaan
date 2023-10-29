# membuat perpustakaan digital
import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name
    match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")
    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print("=========================")


    #chek database ada atau tidak
    CRUD.init_console()
    while(True):
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN")
        print("=========================")
        
        print(f"1. Read data")
        print(f"2. Create data")
        print(f"3. Update data")
        print(f"4. Delete data")

        user_option = input("masukan opsi : ")
        match user_option:
            case "1": CRUD.read_console()
            case "2": print("Create data")
            case "3": print("Update data")
            case "4": print("delete data")
    
        isDone = input("apakah lanjut (y/n)?")
        if isDone == "n":
            break
print("program selesai")
