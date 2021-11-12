from ftplib import FTP
import os
import re

host = "ftp.heanet.ie"
user = "anonymous"
passw = ""
dirs = []
dirs2 = []
dirs3 = []
#patron1= re.compile(".txt$|.msg$|README")

def conexionFTP(host, user, passw):
    try:
        ftp = FTP(host, user, passw)
        print("[+]Conexion correcta...")
        print("\nNos encontramos en la carrpeta: " + ftp.pwd() + "\n")
        buscarArch()   
    except Exception as e:
        print("Conexión fallida: " + str(e))

def buscarArch():
    ftp = FTP(host, user, passw)
    dirs = ftp.nlst()
    print(dirs)
    print("\n")
    for i in dirs:
        try:
            print("En " + i + "\n")
            ftp.cwd(i)
            dirs2 = ftp.nlst()
            for x in dirs2:
                print(x)
                try:
                    ftp.cwd(x)
                    dirs3 = ftp.nlst()
                    for y in dirs3:
                        print(y)
                except Exception:       
        except Exception as e:
            print("\n" + i + " no es un directorio...")

#def savefile():
    #for element in dirs:
        #print(element)
        #ftp.cwd(element)


conexionFTP(host, user, passw)

