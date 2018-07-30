import math

class Solution:
    def isPrime(self, n):
        # Corner cases
        if (n <= 1):
            return False
        if (n <= 3):
            return True

        # This is checked so that we can skip 
        # middle five numbers in below loop
        if (n % 2 == 0 or n % 3 == 0) :
            return False

        i = 5
        while(i * i <= n):
            if (n % i == 0 or n % (i + 2) == 0):
                return False
            i = i + 6

        return True

            
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        total = 0
        
        for number in range(L, R+1):
            count = 0
            while (number) > 0:
                if number & 1 == 1:
                    count += 1
                number = number >> 1
            
            if self.isPrime(count):
                total += 1
                
        return total