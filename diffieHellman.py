import math
import random

# Prime numbers: Os números primos são os números naturais que podem ser divididos por apenas dois fatores: o número um e ele mesmo
def isPrime( number ):
  for i in range(2, math.isqrt(number)+1):
    if number % i == 0 :
      return False
  return  True
  
def getPrime( size ):
  while True:
    number = random.randrange(size, 2*size)
    if isPrime(number):
      return number
      
def isGenerator( generator, prime):
  for i in range(1, prime - 1 ): # caso o numeo primo seja 3 ele irá até 2
    if ( generator**i ) % prime == 1: 
      return False
  return True
      
def getGenerator( prime ):
  for generator in range( 2, prime ):
    if isGenerator(generator, prime):
      return generator


prime = getPrime(10000)
generator = getGenerator(prime)
print("Numero primo: ", prime)
print("Gerador derivado: ", generator)

print("//===========//")
# Alice  gera a chave privada e publica  
privateA = random.randrange(0, prime) # numero privado gerado com mesmo numero primo
publicA = (generator ** privateA) % prime

print("Alice privada: ", privateA)
print("Alice publica: ", publicA)

# Bob gera a chave privada e publica  
privateB = random.randrange(0, prime) # numero privado gerado com mesmo numero primo
publicB = (generator ** privateB) % prime

# Bob sends this out in the public
print("Bob privada: ", privateB)
print("Bob publica: ", publicB)

print("//===========//")
# Volta para alice
secretA = ( publicB**privateA ) % prime
print("Alice segredo: ", secretA)

# Volta para o bob
secretB =( publicA**privateB ) % prime
print("Bob segredo: ", secretB)
