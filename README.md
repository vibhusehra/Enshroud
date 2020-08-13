# About
Audio Steganography is a technique used to transmit hidden information by modifying an audio signal in an imperceptible manner. It is the science of hiding some secret text or audio information in a host message. The host message before steganography and stego message after steganography have the same characteristics. We are using Audio steganography along with RSA algo to provide 2 level security.

# Enshroud
- The files for the project are as follows 
   - A sender(Encryption) module(RSA)
   - A receiver(Decrytion) Module(RSA)
   - A encoder module(steganography)
   - A decoder module(steganography)
   - prime number used to check and generate the prime numbers
   - sample-song folder contains a song
   - embedded_song.wav is the song where the message has been stored in the LSB of each byte of the song
   The modules are used in a manner as described in this image
  ![WorkFlow](https://www.eetindia.co.in/wp-content/uploads/sites/4/2020/04/Data_over_sound_fig1_end_to_end_1800x1025.jpg)
  
  We are doing all the work here from sending the message to adding the message for the reciever.
  - The message is stored in the LSB of each  frame_byte of the song
  - First the sender prompts the receiver via message.txt that it wants to send a message
  - The reciever module makes 2 set of keys (One private and One public) shares the public key to the sender(via message.txt) and keeps the private key to itself
  - The sender encrypts the data with the key and puts on the audio wav file.
  - Encoder module calculates all the frame bytes of the audio file and chahnges the last bit of each byte to store the encrypted data.
  - On the receiver side the decoder decodes the encrypted data from the audio. It then calls the receiver module.
  - The data is then decrypted by the receiver module using its private key.
  
 Note that we are not sending the public key via steganography just the encrypted message is sent.
 2 level concealing of the message has been done
  
 Sender Module(Prompt)--->Receiver Module(generates key)--->Sender(encrpyts data)--->Encode(puts the encrypted data in Audio using LSB technique)--->Decode(retrieves the data from audio)--->Receiver(decrypts the data using private key)
 
 
 # steps to use the module
 - clone this repository to sender and the receiver
 - run the gui python script with python 3.8
 - on the receiver tab generate the keys. keep the private key to yourself and share the public key with the sender(enter the small prime numbers for a better expereice)
 - if you are the sender then on the sender Tab type your message, enter the public keys and select the audio file.
 - share the audio file with the receiver.
 
 # tech stacks used
 - [Tkinter](https://docs.python.org/3/library/tkinter.html) was used to make the GUI.
 - Python wave library was used for the steganography.
 - About [RSA algo](https://simple.wikipedia.org/wiki/RSA_algorithm)

# future works/ improvements
- the length of the message is limited by the song. New methods to be discovered so that more info can be transmitted through the same song
- better crypoptography algos than RSA can be used
- The whole system can be made available on cloud for better expereice to the users

vibhusehra@gmail.com || doshirishabh26@gmail.com
