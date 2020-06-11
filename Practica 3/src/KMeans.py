import numpy

class KMeans():

	def __init__(self,N):

		self.xVectors = []
		self.classes = {}
		self.N = N
		self.uMatrix = []

	def addXVector(self,xVector):

		self.xVectors.append(xVector)

	def addClass(self,c):

		self.classes[c.getClassName()] = c

	def setClasses(self,classes):

		self.classes = classes

	def getClasses(self):

		return self.classes

	def setUMatrix(self,matrix):

		self.uMatrix = matrix

	def doTraining(self,epsilonLimit,b, log_file):

		xNumber = len(self.xVectors)
		cNumber = len(self.classes)
		bBreak = False
		i = 1
		while not bBreak:

			bBreak = True
			for key in self.classes:
				delta = self.calculateV(self.classes[key],b)
				bBreak = bBreak and (delta<epsilonLimit)
			log_file.write("\n>>>>>>>>>>>>>>>>>>Iteracion {}\n".format(i))
			for key in self.classes:
				log_file.write("\n>>> Vector v de la clase {}\n".format(self.classes[key].getClassName()))
				log_file.write(str(self.classes[key].getVCenter()))
			i+=1
			self.updateUMatrix(b)
			log_file.write("\n>>> Matriz U\n")
			numpy.set_printoptions(linewidth=numpy.nan)
			numpy.transpose(self.uMatrix)
			log_file.write(str(self.uMatrix))
			''' Resets the formatter '''
			numpy.set_printoptions()
		
	def calculateV(self,c,b):

		newV = numpy.zeros((self.N,1),dtype=float)
		newVDividend = numpy.zeros((1,self.N),dtype=float)
		newVDivisor = 0
		
		for i in range(len(self.xVectors)):
			'''dividend is a temp var equals P(uij/xj)'''
			dividend = self.uMatrix[i][c.getIndex()]
			newVDividend = numpy.add(newVDividend, numpy.dot(numpy.power(dividend,b),self.xVectors[i]))
			'''divisor is a temp var equals P(uij/xj) '''
			divisor = self.uMatrix[i][c.getIndex()]
			newVDivisor = numpy.add(newVDivisor, numpy.power(divisor,b))

		newV = numpy.divide(newVDividend,newVDivisor)
		''' numpy.linalg.norm without an exponent parameter equals euclidean distance '''
		delta = numpy.linalg.norm(numpy.subtract(newV,c.getVCenter()))
		c.setVCenter(newV)

		return delta

	def calculateP(self,v1,v2,b):

		'''We calculate the dividend 1/dij ^ 1/b-1 '''
		dij = self.calculateEuclideanDistance2(v1,v2)
		dividend = (1/numpy.power(dij, (1/(b-1))))

		'''We calculate the divisor'''
		divisor = 0
		for key in self.classes:

			drj = self.calculateEuclideanDistance2(v2,self.classes[key].getVCenter())
			divisor +=  (1/numpy.power(drj, (1/(b-1))))
		
		return dividend/divisor

	def calculateEuclideanDistance2(self,v1,v2):

		return numpy.power(numpy.linalg.norm(numpy.subtract(v2,v1)),2)

	def updateUMatrix(self,b):

		'''We update the values of the fuzzy U matrix for the next iteration'''

		for i in range(len(self.uMatrix)):
			for key in self.classes:
				self.uMatrix[i][self.classes[key].getIndex()] = self.calculateP(self.classes[key].getVCenter(),self.xVectors[i],b)

	def clasifyEuclideanDistance(self,vector, log_file):
		
		className= None
		mini = float('inf')

		log_file.write("\n>>> Clasificacion de distancia vector {}\n".format(vector))
		print("\n>>> Clasificacion de distancia vector ",vector ,"\n")
		for key in self.classes:
			distance = self.calculateEuclideanDistance2(self.classes[key].getVCenter(),vector)
			log_file.write("Distancia a la clase {}: {}\n".format(self.classes[key].getClassName(), distance))
			print("Distancia a la clase ",self.classes[key].getClassName(), ": ",distance)
			if(distance < mini):
				mini = distance
				className = key
		return className

	def clasifyProbability(self,vector,b):
		pVector=[]
		for key in self.classes:
			p = self.calculateP(self.classes[key].getVCenter(),vector,b)
			pVector.append(self.classes[key].getClassName() + " = "+str(p))

		return pVector
		
class Class():

	def __init__(self,xIndex,className):

		self.vCenter = []
		self.xIndex = xIndex
		self.className = className

	def getVCenter(self):

		return self.vCenter

	def setVCenter(self,vCenter):

		self.vCenter = vCenter

	def getClassName(self):

		return self.className

	def getIndex(self):

		return self.xIndex