import requests
from bs4 import BeautifulSoup 

def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, "html.parser")

def uni():
    soup = get_soup("https://www.uanl.mx")
    nota = soup.find_all('span', class_="hidden share_title")
    a = [ele.text.strip('<') for ele in nota]
    print('Notacias UANL: ')
    for z in a:
        print(z)
        guardar(z)

def guardar(z):
    f = open('NoticiasUANL.txt','a')
    f.write(z)
    f.write('\n')

if __name__ == "__main__":
    uni()