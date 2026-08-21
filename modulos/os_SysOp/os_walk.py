import os
from itertools import count
import subprocess
subprocess.run("cls", shell=True)

caminho = os.path.join("/Users", "rf001", "OneDrive", "Documentos", "Exemplo")
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print("Pasta atual:", root)

    for dir_ in dirs:
        print("   Dir:", dir_)
    for file_ in files:
        caminho_arquivo = os.path.join(root, file_)
        print("   File:", caminho_arquivo)
