DEFAULT_PATH = "files/"

# Lee el contenido de un fichero
def readFile(filename):
    result = None

    file = open(DEFAULT_PATH + filename, "r")
    try:
        print("Leyendo el archivo {}...".format(filename))
        result = list(map(lambda line: line.replace("\n", ""), file.readlines()))
    finally:
        file.close()

    return result

# Devuelve los datos transformados al formato deseado
def processData(data):
    processedData = {}

    for className in getClasses(data):
        processedData[className] = filterByClass(data, className)

    return processedData
    
def processSample(sample):
    splittedItem = sample.split(',')
    return transform_to_float(splittedItem[: len(splittedItem) - 1])

# Devuelve el número de clases que tiene un conjunto de datos
def getClasses(data):
    classes = []

    for item in data:
        className = item.split(",")[-1]
        if className not in classes:
            classes.append(className)
    
    return classes

# Devuelve una lista de conjuntos de valores (cada conjunto es otra lista) cuya clase pertenece a la de del ejemplo
def filterByClass(data, className):
    values = []

    for item in data:
        splittedItem = item.split(',')
        if splittedItem[-1] == className:
            values.append(transform_to_float(splittedItem[: len(splittedItem) - 1]))

    return values

# Devuelve una muestra convertida en floats, en lugar de strings
def transform_to_float(sample):
    float_sample = []
    for value in sample:
        float_sample.append(float(value))

    return float_sample

def get_data_from_file(file_name):
    return processData(readFile(file_name))

def get_sample_from_file(file_name):
    return processSample(readFile(file_name)[0])