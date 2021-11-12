from ftplib import FTP
import os

host = "ftp.heanet.ie"
user = "anonymous"
passw = ""
dirs = []

def conexionFTP (host, user, passw):
    try:
        ftp = FTP(host, user, passw)
        print("[+]Conexion correcta...")
        print("\nNos encontramos en la carrpeta: " + ftp.pwd() + "\n")
        dirs = ftp.nlst()
        savefile(dirs)
    except Exception as e:
        print("Conexión fallida: " + str(e))

def savefile:
    for element in dirs:
        print(element)
        ftp.cwd(element)
        
        
try:
    ftp = FTP(host, user, passw)
    print("[+]Conexión correcta...")
    print("\nNos encontramos en la carrpeta: " + ftp.pwd() + "\n")
    #listar el contenido de donde nos encontramos
    ftp.dir();
    #acceder a alguna carpeta
    ftp.cwd("mirrors")
    print("\nNos encontramos en la carrpeta: " + ftp.pwd() + "\n")
    ftp.dir();
    os.chdir("descargasFTP/")
except Exception as e:
    print("Conexión errada: " + str(e))
    


