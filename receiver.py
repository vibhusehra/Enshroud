import math
import os
class receiver():
    # def __init__(self):
        
    #     self.d = None
    #     self.n = None

    @staticmethod
    def gcd(a,b): 
        if b==0: 
            return a 
        
        return receiver.gcd(b,a%b)

    @staticmethod
    def receiver_create_key(p1 = 89 , p2 = 97):
        # f = open('message.txt' , 'r+')

        # if f.read() == 'SEND':
        #     f.close()

        #     pass
        # else:
        #     print('usko kuch nahi bhejna tujhe')
        #     return

        p = p1
        q = p2
        
        # Part of the public key
        n = int(p * q)
        # self.n = int(p * q)
        '''
            t -> integer
              -> called theta(n)
        '''
        t = (p-1) * (q-1)

        '''
            now we find e, i.e the second public key
            e -> integer => [1<e<t]
              -> gcd(e,t) = 1
        '''
        for e_prime in range(2 , t):
            # if self.gcd(e_prime , t) == 1:
            if receiver.gcd(e_prime , t) == 1:
                break

        '''
            Now we create the private key
              -> ed % t = 1
        '''
        d = None
        i = 1
        while True:
            x = 1 + i*t 
            if x % e_prime == 0:
                # self.d = int(x/e_prime) 
                d = int(x/e_prime) 
                break
            i += 1
            # else:
            #     d = int(x/e_prime)

        # return (self.n, e_prime, self.d)
        return (n, e_prime, d)
        # f.close()

        # f = open('message.txt' , 'w+')

        # f.write(( str(self.n) + ',' + str(e_prime)))
        # f.close()

    @staticmethod
    def message_read(msg, d, n): 
        msg = msg.strip().split(' ')
        print(msg)
        decoded = ""
        for m in msg:
            # print(m)
            decoded += chr(pow(int(m) , d) % n)
        return decoded