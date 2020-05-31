import data_utils as utils
import algorithms as algs

sample_files = ["TestIris01.txt", "TestIris02.txt", "TestIris03.txt"]

data = utils.get_data_from_file("Iris2Clases.txt")

print("======================== PRACTICA 3 ========================")
for sample_file in sample_files:
    sample = utils.get_sample_from_file(sample_file)
    print("\n========= {} =========".format(sample_file))
    print("Vamos a analizar la muestra {}".format(sample_file))
    print("\nBAYES: ")
    prediction = algs.bayes(data, sample)
    # More algorithms...
