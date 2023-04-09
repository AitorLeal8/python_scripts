import requests

def detectar_protocolo(url):
  respuesta = requests.get(url)
  protocolo = respuesta.url.split(":")[0]
  resultado = url + " --------> " + protocolo
  return resultado

print(detectar_protocolo("https://es.godaddy.com"))
print(detectar_protocolo("http://www.ionos.es"))
