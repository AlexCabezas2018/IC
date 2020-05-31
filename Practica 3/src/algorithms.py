import numpy as np
import math

def bayes(data, sample_to_guess):
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
            sample_minus_mean = [np.array(sample) - mean]
            n_term = np.matmul(sample_minus_mean, np.transpose(sample_minus_mean))
            total += n_term
            
        return total / len(samples)
    
    def get_min_distance(data):
        min_value = math.inf
        prediction = ""

        for val in data:
            if data[val][0][0] < min_value:
                prediction = val
                min_value = data[val][0][0]

        return prediction

    print("Analizando la muestra con el algoritmo de bayes")
    bayes_data = {}
    for className in data:
        mean = calculate_mean(className)
        covariance = calculate_covariance(className, mean)

        sample_minus_mean = [np.array(sample_to_guess) - mean]
        second_term = np.transpose(sample_minus_mean)

        bayes_data[className] = np.matmul(sample_minus_mean, second_term)
    
    print("Distancias de la muestra: ")
    for val in bayes_data:
        print("\t- Clase: {}, distancia: {}".format(val, bayes_data[val][0][0]))

    prediction = get_min_distance(bayes_data)
    print("La predicción (distancia mínima) para la muestra es {}".format(prediction))

    return prediction


    
        
