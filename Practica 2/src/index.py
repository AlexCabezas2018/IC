import math

DEFAULT_PATH = "files/"

# Devuelve el arbol de decisión resultante de aplicar el algoritmo sobre un conjunto de atributos y ejemplos.
def ID3(attributes, examples, target_attribute, target_value, file):
    file.write("========================\n")
    if len(attributes) == 0 and attributes[0] == classAttribute:
        return None
    else:
        if areAllPositiveOrNegative(examples, "si"):
            file.write("El atributo {} con el valor {} ha dado resultado positivo\n".format(target_attribute, target_value))
            return {
                "attribute": target_attribute,
                "value": target_value,
                "final_value": "yes"
            }
        elif areAllPositiveOrNegative(examples, "no"):
            file.write("El atributo {} con el valor {} ha dado resultado negativo\n".format(target_attribute, target_value))
            return {
                "attribute": target_attribute,
                "value": target_value,
                "final_value": "no"
            }
        else:
            merits = []
            for attr in attributes:
                subtypes = getSubtypes(attr, examples)
                params = []
                for subtype in subtypes:
                    rows = getRows(attr, subtype, examples)
                    params.append(calculateParameters(rows, len(examples)))
                if attr != classAttribute:
                    merits.append({
                        "attribute": attr,
                        "merit": merit(params)
                    })

            if target_attribute == None:
                file.write("Inicio del algoritmo\n")
            else:
                file.write("Estamos evaluando el atributo {} con el valor {}\n".format(target_attribute, target_value))
                file.write("\n")

            for mer in merits:
                file.write("Atributo: {}, Merito: {}\n".format(mer['attribute'], mer['merit']))
            file.write("\n")

            lessMeritAttr = lessMeritAttribute(merits)
            file.write("El mejor atributo seleccionado es: {}\n".format(lessMeritAttr['attribute']))
            file.write("Evaluaremos el atributo {} con los valores {}\n".format(lessMeritAttr['attribute'], getSubtypes(lessMeritAttr['attribute'], examples)))
            children = []
            for subtype in getSubtypes(lessMeritAttr['attribute'], examples):
                filtered_attributes = removeAttribute(attributes, lessMeritAttr['attribute'])
                filtered_examples = examplesWithSubtype(lessMeritAttr['attribute'], subtype, examples)
                children.append(ID3(filtered_attributes, filtered_examples, lessMeritAttr['attribute'], subtype, file))
            
            return {
                "attribute": target_attribute if target_attribute != None else lessMeritAttr['attribute'],
                "value": target_value,
                "children": children
            }
        
# Funciones auxiliares para ID3
def merit(params):
    return sum(params[i]['r'] * entropy(params[i]['n'], params[i]['p']) for i in range(len(params)))

def entropy(x, y):
    return -(x * safeLog2(x)) - (y * safeLog2(y))


def safeLog2(x):
    try:
        return math.log2(x)
    except ValueError:
        return 0

# Elimina un atributo de la lista de atributos, pero sin modificar el dado en la entrada
def removeAttribute(attributes, attr):
    ret = []
    for at in attributes:
        if at != attr:
            ret.append(at)
    return ret

# Elimina una clave de los ejemplos
def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

# Devuelve los ejemplos que contienen el valor del atributo
def examplesWithSubtype(column, subtype, examples):
    ret = []
    for ex in examples:
        if ex[column] == subtype:
            ret.append(removekey(ex, column))

    return ret

# Devuelve si los ejemplos son todos positivos o negativos, dependiendo del valor
def areAllPositiveOrNegative(examples, value):
    return len(list(filter(lambda ex: ex[classAttribute] == value, examples))) == len(examples)

# Devuelve el mejor atributo, basándose en su mérito
def lessMeritAttribute(merits):
    merit = merits[0]
    for m in merits:
        if m['attribute'] != classAttribute and m['merit'] < merit['merit']:
            merit = m

    return merit


# Devuelve las subcategorías (valores distintos) de un atributo
def getSubtypes(column, examples):
    subtypes = []
    for ex in examples:
        if ex[column] not in subtypes:
            subtypes.append(ex[column])
    return subtypes

# Devuelve las filas asociadas al subtipo
def getRows(column, subtype, examples):    
    rows = []
    for ex in examples:
        if ex[column] == subtype:
            rows.append(ex)
    return rows

# Calcula la p, la n y las r
def calculateParameters(rows, size):
    p = n = r = 0
    for row in rows:
        if row[classAttribute] == "si":
            p += 1
        elif row[classAttribute] == "no":
            n += 1

    return {
        "p": p / len(rows),
        "n": n / len(rows),
        "r": (p + n) / size
    }


def readFile(filename):
    """ Lee el contenido de un archivo (ubicado en la ruta files/filename).
        Devuelve una lista con tantos elementos como lineas tenga
    """
    print("Leyendo el archivo {}...".format(filename))
    file = open(DEFAULT_PATH + filename, "r")
    result = list(map(lambda line: line.replace("\n", "").split(","), file.readlines()))
    file.close()
    
    return result[0] if len(result) == 1 else result

def processExamples(attributes, examples):
    processed_examples = []
    for ex in examples:
        processed_example = {}
        i = 0
        for attr in attributes:
            processed_example[attr] = ex[i]
            i += 1
        processed_examples.append(processed_example)

    return processed_examples

attributes = readFile("AtributosJuego.txt")
examples = readFile("Juego.txt")

# Nos ayuda a identificar qué atributo define si el ejemplo pertenece a la clase.
classAttribute = attributes[-1]

processedData = processExamples(attributes, examples)

log_file = open(DEFAULT_PATH + "logs.txt", "w")
print("Ejecutando ID3...")
output = ID3(attributes, processedData, None, None, log_file)
print("ID3 finalizado!")
log_file.write("Resultado final (Explicacion en la memoria):\n")
log_file.write(str(output))
log_file.close()


