import math

DEFAULT_PATH = "files/"

def ID3(attributes, examples, target_attribute):
    return "WIP - Test"


def merit(p, n, r):
    total = 0
    for i in range(len(r)):
        total += r[i] * info(p[i], n[i])
    return total


def info(x, y):
    return -(x * math.log2(x)) - (y * math.log2(y))

def readFile(filename):
    """ Lee el contenido de un archivo (ubicado en la ruta files/filename).
        Devuelve una lista con tantos elementos como lineas tenga
    """
    file = open(DEFAULT_PATH + filename, "r")
    result = list(map(lambda line: line.replace("\n", "").split(","), file.readlines()))
    
    if len(result) == 1:
        return result[0]

    return result

attributes = readFile("AtributosJuego.txt")
examples = readFile("Juego.txt")

output = ID3(attributes, examples)
print(output)