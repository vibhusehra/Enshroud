# Secure-Transmit-Pro
- The files for the project are as follows 
   - A sender(Encryption) module
   - A receiver(Decrytion) Module
   - A encoder module
   - A decoder module
  The modules are used in a manner as described in this image
  ![WorkFlow](https://www.eetindia.co.in/wp-content/uploads/sites/4/2020/04/Data_over_sound_fig1_end_to_end_1800x1025.jpg)
  
  We are doing all the work here from sending the message to adding the message for the reciever.
  - A sample workflow has been described in the jupyter notebook file- Sample Workflow
  - First the sender prompts the receiver via message.txt that it wants to send a message
  - The reciever module makes 2 set of keys (One private and One public) shares the public key to the sender(via message.txt) and keeps the private key to itself
  - The sender encrypts the data with the key and puts on the audio wav file.
  - Encoder module calculates all the frame bytes of the audio file and chahnges the last bit of each byte to store the encrypted data.
  - On the receiver side the decoder decodes the encrypted data from the audio. It then calls the receiver module.
  - The data is then decrypted by the receiver module using its private key.
  
 Note that we are not sending the public key via steganography just the encrypted message is sent.
 2 level concealing of the message has been done
  
 Sender Module(Prompt)--->Receiver Module(generates key)--->Sender(encrpyts data)--->Encode(puts the encrypted data in Audio using LSB technique)--->Decode(retrieves the data from audio)--->Receiver(decrypts the data using private key)
 

vibhusehra@gmail.com || doshirishabh26@gmail.com
