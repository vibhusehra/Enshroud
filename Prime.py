import numpy as np
import math
class Prime:

	@staticmethod
	def generatePrimePair():
		try:
			primeArray = np.load('primes.npy')
		except FileNotFoundError as e:
			primeArray = Prime.createPrimes()
			print(e)

		x, y = np.random.choice(primeArray, 2)
		while(x == y):
			y = np.random.choice(primeArray, 1)

		return (x, y)
			


	@staticmethod
	def checkPrime(num):
		try:
			primeArray = np.load('primes.npy')
		except FileNotFoundError as e:
			primeArray = Prime.createPrimes()
			print(e)

		return (num in primeArray)


	@staticmethod
	def createPrimes(start = 0, end = 200):
		end += 1
		primeArray = np.ones((end,), dtype=bool)
		primeArray[0] = primeArray[1] = False
		for i in range(2, int(math.sqrt(end)) + 1):
			# print(i)
			if(primeArray[i]):
				# print("prime: " + str(i))
				for j in range(i*i, end, i):
					primeArray[j] = False
					
		primeArray = np.array([i for i,elem in enumerate(primeArray) if elem == True])
		np.save("primes.npy", primeArray)
		print(primeArray)
		print(type(primeArray))

		return primeArray
# Prime.createPrimes(0, 100)
# print(list(map(int,Prime.createPrimes(0,10) == True)))
# print([i for i,elem in enumerate(Prime.createPrimes(0, 100)) if elem == True])
# print(Prime.createPrimes(0,20))
# print(Prime.generatePrimePair())
# print(Prime.checkPrime(23))
# Prime.createPrimes()
# Prime.createPrimes()
