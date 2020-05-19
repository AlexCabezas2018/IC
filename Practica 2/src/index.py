DEFAULT_PATH = "files/"

def readFile(filename):
    """ Lee el contenido de un archivo (ubicado en la ruta files/filename).
        Devuelve una lista con tantos elementos como lineas tenga
    """
    file = open(DEFAULT_PATH + filename, "r")
    result = list(map(lambda line: line.replace("\n", "").split(","), file.readlines()))
    
    if len(result) == 1:
        return result[0]

    return result

def ID3(attributes, examples):
    return "WIP - Test"


attributes = readFile("AtributosJuego.txt")
examples = readFile("Juego.txt")

output = ID3(attributes, examples)
print(output)