import data_utils as utils
import algorithms as algs

data = utils.get_data_from_file("Iris2Clases.txt")
sample = utils.get_sample_from_file("TestIris03.txt")

prediction = algs.bayes(data, sample)

print("La predicción para la muestra es {}".format(prediction))
