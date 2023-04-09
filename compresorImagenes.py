from PIL import Image
import os

ruta = r"C:\Users\lealm\Desktop\proyectos\imagenes"

if __name__ == "__main__":
    for filename in os.listdir(ruta):
        name, extension = os.path.splitext(os.path.join(ruta, filename)) # name = nombre del archivo, extension = extensión del archivo, os.path.join(ruta, filename) = ruta completa del archivo

        if extension in [".jpg", ".jpeg", ".png"]: # Si la extensión del archivo es una de las siguientes, se comprime la imagen
            picture = Image.open(os.path.join(ruta, filename)) # Se abre la imagen
            picture.save(os.path.join(ruta, "compressed_" + filename), optimize=True, quality=80) # Se guarda la imagen comprimida
