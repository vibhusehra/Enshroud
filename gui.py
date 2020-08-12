from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from prime_number.Prime import Prime
from tkinter import messagebox
from RSA.receiver import receiver
from steganography.decode_song import decode
from RSA.sender import Sender
from steganography.encode_song import encode

fname = None
decodeButton = None
sender_fname = None
encodeButton = None



def encodeMessage(textBox, n, e):
    '''
    sends the message to the encode_song module
    '''
    message = textBox.get("1.0", END)
    encrypted = Sender.send_msg(message, n, e)
    print(encrypted)
    encode(sender_fname, encrypted)
    messagebox.showinfo("Success", "Encodede Successfully")


def addSendTab():
    '''
    adding the send tab in tkinter
    provides a text box for message
    and 2 entry box for the public key
    '''
    tab1.columnconfigure(1, weight=1)
    tab1.columnconfigure(0, weight=1)
    tab1.columnconfigure(2, weight=1)

    label1 = Label(tab1, text="Key 1")
    label1.grid(row=0, column=0, pady=10)
    key1Entry = Entry(tab1, width=20, borderwidth=3)
    key1Entry.grid(row=1, column=0, padx=20)

    label2 = Label(tab1, text="Key 2")
    label2.grid(row=0, column=2, pady=10)
    key2Entry = Entry(tab1, width=20, borderwidth=3)
    key2Entry.grid(row=1, column=2, padx=20)

    textBox = Text(tab1, height=5, width=20)

    encodeButton = Button(tab1, text="Encode", state=DISABLED, command= lambda: encodeMessage(textBox, int(key1Entry.get()), int(key2Entry.get())))

    uploadAudioButton = Button(tab1, text="Browse Audio", command=lambda: load_file(encodeButton, key1Entry, key2Entry))
    uploadAudioButton.grid(row=2, column=1, sticky="ew", pady=10)
    label_temp = Label(tab1 , text = "sample text")
    label_temp.grid(row = 2 , column = 2 , pady = 10)


    # textBox = Entry(tab1, borderwidth=3)
    massageLabel = Label(tab1, text="Secret Message")
    massageLabel.grid(row=3, column=0)

    textBox.grid(row=4, column=0, columnspan=3, sticky="ew", padx=(50,50))

    encodeButton.grid(row=5, column=1, sticky="ew", pady=10)

    # encode code


def load_file(button, key1, key2):
    '''
    for loading the file in the send tab
    opens the dialog box for the file names and asks for a wav file
    if not provided a wav file shows an error
    '''
    global sender_fname
    sender_fname = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])
    if sender_fname:
        try:
            # print("""here it comes: """)
            print(sender_fname)
            # if label1['text'].isdigit():
                # print('yes')
            print(key1.get(), key2.get())
            if key1.get().isdigit() and key2.get().isdigit():
                # print('yes')
                button['state'] = 'normal'
            else:
                displayError('Please enter an Integer')

        except:                     
            showerror("Open Source File", "Failed to read file\n'%s'" % sender_fname)
    return

def load_file_receiver(button):
    '''
    opens up the filedialog box to browse the audio file where the message is hidden
    '''
    global fname
    fname = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])
    if fname:
        try:
            # print("""here it comes: """)
            print(fname)
            if type(pk1) == int:
                button['state'] = 'normal'

        except:                     
            showerror("Open Source File", "Failed to read file\n'%s'" % fname)
        return



def generatePrimes(prime1Entry, prime2Entry):
    '''
    generates the prime number for the user if User does not want to calculate prime numbers
    '''
    (x, y) = Prime.generatePrimePair()
    # print(x,y)
    prime1Entry.delete(0, END)
    prime2Entry.delete(0 , 'end')
    prime1Entry.insert(0, str(x))
    prime2Entry.insert(0, str(y))

def displayError(text):
    '''
    shows the error when an exception is raised
    '''
    messagebox.showerror(message=text)

def checkEntries(prime1Entry, prime2Entry):
    '''
    checks the entries if both entries in the entry box are prime or not
    otherwise shows the error on the message box
    '''
    p1 = (prime1Entry.get()).strip()
    p2 = (prime2Entry.get()).strip()
    # print(p1.isdigit())
    # print(p1, p2) 
    # print(not p1.isdigit())
    if p1.isdigit() == False or p2.isdigit() == False:
        displayError("Please enter a valid Integer!!")
        return


    p1 = int(p1)
    p2 = int(p2)

    if p1 == p2:
        displayError("Same Numbers not allowed")
        prime1Entry.delete(0 , 'end')
        prime2Entry.delete(0 , 'end')
        return


    if Prime.checkPrime(p1) and Prime.checkPrime(p2):
        # create keys
        print('Both Primes')
        global pk1, pk2, pr1
        pk1, pk2, pr1 = receiver.receiver_create_key(p1, p2)
        changeKeyText(pk1, pk2, pr1)

        if fname is not None:
            decodeButton['state'] = 'normal'
        print(pk1, pk2, pr1)

    else:
        ls = []
        if(Prime.checkPrime(p1) == False): 
            ls.append(p1)
            prime1Entry.delete(0 , 'end')
        if(Prime.checkPrime(p2) == False): 
            ls.append(p2)
            prime2Entry.delete(0 , 'end')
        message = "Please enter valid prime numbers:\n"
        for elem in ls:
            message += "{} is not a prime\n".format(elem)
        displayError(message)

def decodeMessage():
    '''
    calls the decode module from the receiver tab and shows the message in a message box
    both decodes the message and decrypts the message
    '''
    encoded = decode(fname)
    print(pr1, pk1)
    decoded = receiver.message_read(encoded, pr1, pk1)
    messagebox.showinfo("Decoded Message", "secet message:{}".format(decoded))


def changeKeyText(pk1, pk2, pr1):
    '''
    if prime numbers are valid this method
    replaces the lables to accomodate prime number within them
    '''
    global key1Label, key2Label, key3Label
    key1Label['text'] = 'Public Key 1: ' + str(pk1)
    key2Label['text'] = 'Public Key 2: ' + str(pk2)
    key3Label['text'] = 'Private Key: ' + str(pr1)

def addReceiveTab():
    '''
    receiver tab code
    pops up a message box when audio is decoded
    '''
    
    tab2.columnconfigure(1, weight=1)
    tab2.columnconfigure(0, weight=1)
    tab2.columnconfigure(2, weight=1)
    label1 = Label(tab2, text="Prime 1")
    label1.grid(row=0, column=0, pady=10)
    prime1Entry = Entry(tab2, width=20, borderwidth=3)
    prime1Entry.grid(row=1, column=0, padx=20)

    label2 = Label(tab2, text="Prime 2")
    label2.grid(row=0, column=2, pady=10)
    prime2Entry = Entry(tab2, width=20, borderwidth=3)
    prime2Entry.grid(row=1, column=2, padx=20)

    generatePrimeButton = Button(tab2, text="Generate Prime Pair", command=lambda: generatePrimes(prime1Entry, prime2Entry))
    generatePrimeButton.grid(row=2, column=1, sticky="ew")
    
    generateKeyButton = Button(tab2, text="Generate Keys", command=lambda: checkEntries(prime1Entry, prime2Entry))
    generateKeyButton.grid(row=3, column=1, pady=5, sticky="ew")

    print(pk1, pk2, pr1)

    key1Label.grid(row=4,column=0)

    key2Label.grid(row=4,column=1)

    key3Label.grid(row=4,column=2)

    global decodeButton
    decodeButton = Button(tab2, text="Decode", state=DISABLED, command=decodeMessage)

    uploadAudioButton = Button(tab2, text="Browse Audio", command=lambda: load_file_receiver(decodeButton))
    uploadAudioButton.grid(row=5, column=1, sticky="ew", pady=10)

    #maybe add file loacation label or a audio player

    decodeButton.grid(row=7, column=1, sticky="ew", pady=10)




if __name__ == '__main__':
    root = Tk()
    root.title("Enshroud")
    root.geometry("500x300")
    # e = Entry(root, width=35, borderwidth=5)
    # e.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

    tabControl = ttk.Notebook(root)

    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)

    pk1 = "-"
    pk2 = "-"
    pr1 = "-"

    key1Label = Label(tab2, text="public Key 1: " + pk1)
    key2Label = Label(tab2, text="public Key 2: " + pk2)
    key3Label = Label(tab2, text="private Key: " + pr1)

    tabControl.add(tab1, text="Send")
    tabControl.add(tab2, text="Receive")

    # tabControl.grid(row)


    addSendTab()
    addReceiveTab()

    tabControl.pack(expand=1,fill='both')
    root.mainloop()