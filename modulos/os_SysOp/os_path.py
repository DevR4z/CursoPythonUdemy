import os

caminho = os.path.join(
    r"C:\\Users\\rf001\\OneDrive\\Documentos", "CursoPythonUdemy",
    "modulos", "os_SysOp", "arquivo.txt"
)
print(caminho)
diretorio, arquivo = os.path.split(caminho)
print(diretorio)
print(arquivo)
print(os.path.exists(r"C:\\Users\\rf001\\OneDrive\\Documentos\\"
                     r"CursoPythonUdemy\\modulos\\os_SysOp"))
