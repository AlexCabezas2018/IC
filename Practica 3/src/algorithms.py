import numpy as np
import random
from KMeans import KMeans, Class as KMeansClass
import math

def bayes(data, sample_to_guess, bayes_file):
    def calculate_mean(className):
        samples = data[className]
        n = len(samples[0])
        mean = [0.0 for i in range(n)]
        
        for sample in samples:
            for i in range(len(sample)):
                mean[i] += sample[i] / len(samples)
        
        return np.array(mean)
        
    def calculate_covariance(className, mean):
        samples = data[className]
        total = 0
        for sample in samples:
            sample_minus_mean = np.array(sample) - mean
            n_term = np.matmul(sample_minus_mean, np.transpose(sample_minus_mean))
            total += n_term
            
        return total / len(samples)
    
    def get_min_distance(data):
        min_value = math.inf
        prediction = ""

        for val in data:
            if data[val] < min_value:
                prediction = val
                min_value = data[val]

        return prediction

    print("Analizando la muestra con el algoritmo de bayes")
    bayes_data = {}
    for className in data:
        mean = calculate_mean(className)
        covariance = calculate_covariance(className, mean)

        sample_minus_mean = np.array(sample_to_guess) - mean
        inverse_covariance = np.linalg.inv([[covariance]])[0][0]
        second_term = np.dot(inverse_covariance, np.transpose(sample_minus_mean))

        bayes_data[className] = np.matmul(sample_minus_mean, second_term)

        # d = (X - m) x C-1(X - m)t
    
    bayes_file.write("Distancias de la muestra:\n")
    print("Distancias de la muestra: ")
    for val in bayes_data:
        bayes_file.write("\t- Clase: {}, distancia: {}\n".format(val, bayes_data[val]))
        print("\t- Clase: {}, distancia: {}".format(val, bayes_data[val]))

    prediction = get_min_distance(bayes_data)
    bayes_file.write("La prediccion (distancia minima) para la muestra es {}\n".format(prediction))
    print("La predicción (distancia mínima) para la muestra es {}".format(prediction))

    return prediction

def k_means(data, sample_to_guess, log_file, tolerance=0.01, b=2):

    def getKMeansInitializeUMAtrix(xVectorsCount):

        random.seed()
        matrix = []
        for i in range(xVectorsCount):
            elem = random.uniform(0, 1)
            matrix.append(elem)
            matrix.append(1-elem)
        return np.reshape(matrix,(xVectorsCount,2))

    k = KMeans(4)
    c1 = KMeansClass(0,"Iris-setosa")
    c1.setVCenter([4.6,3.0,4.0,0.0])
    c2 = KMeansClass(1,"Iris-versicolor")
    c2.setVCenter([6.8,3.4,4.6,0.7])

    k.addClass(c1)
    k.addClass(c2)

    uMatrix = getKMeansInitializeUMAtrix(len(data['Iris-setosa']) + len(data['Iris-versicolor']))
    k.setUMatrix(uMatrix)

    for x in data['Iris-setosa']:
        k.addXVector(x)
    
    for x2 in data['Iris-versicolor']:
        k.addXVector(x2)
    
    k.doTraining(log_file=log_file, epsilonLimit=tolerance,b=b)

    prediction = k.clasifyEuclideanDistance(sample_to_guess, log_file)
    log_file.write("La prediccion para la muestra es {}".format(prediction))
    print("La predicción para la muestra es {}".format(prediction))

    return prediction

    
        
