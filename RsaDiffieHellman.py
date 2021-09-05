import math
import random

class RsaDiffieHellman(object):
  def isPrime(self, number ) -> bool :
    for i in range(2, math.isqrt(number)+1):
      if number % i == 0 :
        return False
    return  True
    
  def getPrime(self, size )  -> int :
    while True:
      number = random.randrange(size, 2*size)
      if self.isPrime(number):
        return number
        
  def isGenerator(self, generator, prime) -> int :
    for i in range(1, prime - 1 ): # caso o numeo primo seja 3 ele irá até 2
      if ( generator**i ) % prime == 1: 
        return False
    return True
        
  def getGenerator(self, prime ) -> int :
    for generator in range( 2, prime ):
      if self.isGenerator(generator, prime):
        return generator
        
  def lcm(self, a, b ) -> int :
    return a*b//math.gcd(a,b) # gcd ( maior divisor comum)
    # usamos // para realizar divisão por inteiros para que não se torne um flutuante
    
  def getE(self, lambda_n )  -> int :
    for e in range(2, lambda_n):
      if math.gcd(e, lambda_n) == 1:
        return e
    return False
  
  def getD(self, e, lambda_n )  -> int :
    for d in range(2, lambda_n):
      if d*e % lambda_n == 1:
        return d
    return False
  
  def factor(self, n):
    for p in range(2, n):
      if n % p == 0:
        return p, n//p
        
