import math
import os
class sender1():
    def __init__(self):
        pass
    def ask_to_send(self):
        with open('message.txt' , 'w') as f:
            f.write('SEND')
            f.close()
    def send_msg(self , message = 'hello rishabh'):
        f = open('message.txt' , 'r+')
        key = f.read().split(',')
        n = int(key[0])
        e = int(key[1])
        f.close()

        
        msg = []
        f = open('message.txt' , 'w+')
        for ch in message:
            msg.append(ord(ch))
            f.write(str(pow(msg[-1] , e) % n) + '\n')
        f.close()