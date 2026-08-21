import os

caminho = os.path.join("/Users", "rf001", "OneDrive", "Documentos", "Exemplo")
# C:\Users\rf001\OneDrive\Documentos\CursoPythonUdemy\modulos\os_SysOp
caminho_exist = os.path.exists(caminho)
print(caminho_exist)

for pasta in os.listdir(caminho):
    caminho_pasta = os.path.join(caminho, pasta)
    print(pasta)
    if not os.path.isdir(caminho_pasta):
        continue
    for arch in os.listdir(caminho_pasta):
        print("   ", arch)
