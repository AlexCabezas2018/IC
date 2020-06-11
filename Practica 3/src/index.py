import data_utils as utils
import algorithms as algs

DEFAULT_PATH = "files/"

sample_files = ["TestIris01.txt", "TestIris02.txt", "TestIris03.txt"]

data = utils.get_data_from_file("Iris2Clases.txt")

bayes_logs_file = open(DEFAULT_PATH + "bayes.log", "w")
kmeans_logs_file = open(DEFAULT_PATH + "kmeans.log", "w")

print("======================== PRACTICA 3 ========================")
for sample_file in sample_files:
    sample = utils.get_sample_from_file(sample_file)
    print("\n========= {} =========".format(sample_file))
    print("Vamos a analizar la muestra {}".format(sample_file))
    bayes_logs_file.write("BAYES (Para la muestra {}): \n".format(sample_file))
    print("\nBAYES: ")
    prediction = algs.bayes(data, sample, bayes_logs_file)
    bayes_logs_file.write("\n\n\n")
    kmeans_logs_file.write("KMEANS (Para la muestra {}): \n".format(sample_file))
    print("\nKMEANS: ")
    predictionKMeans = algs.k_means(data, sample, kmeans_logs_file)
    kmeans_logs_file.write("\n\n\n")
