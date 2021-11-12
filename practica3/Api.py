import requests

def get_response_jason(url):
    response = requests.get(url)
    json = None
    if response.status_code >= 200 <= 250:
        json = response.json()
    return json

#usr = input("Escribe el nombre del usuario para buscar sus repos: ")

respuesta = get_response_jason('https://api.github.com/users/Azlath02/repos')

for repo in respuesta:
    nombre = [repo["name"]]
    url = [repo["html_url"]]
    lang = [repo["language"]]
    desc = [repo["description"]]

    if repo["private"] == "false":
        estado = "Privado"
    else:
        estado = "Publico"

    print(nombre,desc,lang,estado,url)

#print(get_response_jason("https://github.com/Azlath02/LPCenc-dec"))
#print(get_response_jason("https://github.com/Azlath02/automata_theory"))
