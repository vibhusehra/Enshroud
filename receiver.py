import math
import os
class receiver():
    def __init__(self):
        
        self.d = None
        self.n = None
    def gcd(self, a,b): 
        if b==0: 
            return a 
        
        return self.gcd(b,a%b)

    def receiver_create_key(self , p1 = 89 , p2 = 97):
        f = open('message.txt' , 'r+')

        if f.read() == 'SEND':
            f.close()

            pass
        else:
            print('usko kuch nahi bhejna tujhe')
            return

        p = p1
        q = p2
        
        self.n = int(p * q)
        t = (p-1) * (q-1)
        for e_prime in range(2 , t):
            if self.gcd(e_prime , t) == 1:
                break
        for i in range(1,10):
            x = 1 + i*t 
            if x % e_prime == 0:
                self.d = int(x/e_prime) 
                break
        f.close()

        f = open('message.txt' , 'w+')

        f.write(( str(self.n) + ',' + str(e_prime)))
        f.close()
    def message_read(self , msg): 
        
        for m in msg:
            print( chr(pow(m , self.d) % self.n) , end = '')