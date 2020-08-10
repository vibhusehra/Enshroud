import math
import os
class Sender():
    # def __init__(self):
    #     pass
    # def ask_to_send(self):
    #     with open('message.txt' , 'w') as f:
    #         f.write('SEND')
    #         f.close()

    @staticmethod
    def send_msg(message, n, e):
        # f = open('message.txt' , 'r+')
        # key = f.read().split(',')
        # n = int(key[0])
        # e = int(key[1])
        # f.close()

        
        msg = []
        # f = open('message.txt' , 'w+')
        x = ""
        for ch in message:
            msg.append(ord(ch))
            # f.write(str(pow(msg[-1] , e) % n) + '\n')
            x += str(pow(msg[-1] , e) % n) + " "
        return x
        # f.close()