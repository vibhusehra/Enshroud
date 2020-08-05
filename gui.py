from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from Prime import Prime
from tkinter import messagebox

def addSendTab():
	tab1.columnconfigure(1, weight=1)
	tab1.columnconfigure(0, weight=1)
	tab1.columnconfigure(2, weight=1)	

	label1 = Label(tab1, text="Key 1")
	label1.grid(row=0, column=0, pady=10)
	key1Entry = Entry(tab1, width=20, borderwidth=3)
	key1Entry.grid(row=1, column=0, padx=20)

	label2 = Label(tab1, text="Key 2")
	label2.grid(row=0, column=2, pady=10)
	prime2Entry = Entry(tab1, width=20, borderwidth=3)
	prime2Entry.grid(row=1, column=2, padx=20)

	uploadAudioButton = Button(tab1, text="Browse Audio", command=load_file)
	uploadAudioButton.grid(row=2, column=1, sticky="ew", pady=10)


	# textBox = Entry(tab1, borderwidth=3)
	massageLabel = Label(tab1, text="Secret Message")
	massageLabel.grid(row=3, column=0)

	textBox = Text(tab1, height=5, width=20)
	textBox.grid(row=4, column=0, columnspan=3, sticky="ew", padx=(50,50))

	decodeButton = Button(tab1, text="Encode", state=DISABLED)
	decodeButton.grid(row=5, column=1, sticky="ew", pady=10)

def load_file():
	fname = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])
	if fname:
		try:
			# print("""here it comes: """)
			print(fname)
		except:                     
			showerror("Open Source File", "Failed to read file\n'%s'" % fname)
		return

def deleteText(entry):
	entry.delete(0, END)

def generatePrimes(prime1Entry, prime2Entry):
	(x, y) = Prime.generatePrimePair()
	# print(x,y)
	deleteText(prime1Entry)
	deleteText(prime2Entry)
	prime1Entry.insert(0, str(x))
	prime2Entry.insert(0, str(y))

def displayError(text):
	messagebox.showerror(message=text)

def checkEntries(prime1Entry, prime2Entry):
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
	if Prime.checkPrime(p1) and Prime.checkPrime(p2):
		# create keys
		print('Both Primes')
	else:
		ls = []
		if(Prime.checkPrime(p1) == False): 
			ls.append(p1)
			deleteText(prime1Entry)
		if(Prime.checkPrime(p2) == False): 
			ls.append(p2)
			deleteText(prime2Entry)
		message = "Please enter valid prime numbers:\n"
		for elem in ls:
			message += "{} is not a prime\n".format(elem)
		displayError(message)


def addReceiveTab():
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

	p1 = "123"
	p2 = "456"
	p3 = "678"
	key1Label = Label(tab2, text="public Key 1: " + p1)
	key1Label.grid(row=4,column=0)
	key2Label = Label(tab2, text="public Key 2: " + p2)
	key2Label.grid(row=4,column=1)
	key3Label = Label(tab2, text="private Key: " + p3)
	key3Label.grid(row=4,column=2)

	uploadAudioButton = Button(tab2, text="Browse Audio", command=load_file)
	uploadAudioButton.grid(row=5, column=1, sticky="ew", pady=10)

	#maybe add file loacation label or a audio player

	decodeButton = Button(tab2, text="Decode", state=DISABLED)
	decodeButton.grid(row=7, column=1, sticky="ew", pady=10)




root = Tk()
root.title("Enshroud")
root.geometry("500x300")
# e = Entry(root, width=35, borderwidth=5)
# e.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text="Send")
tabControl.add(tab2, text="Receive")

# tabControl.grid(row)


addSendTab()
addReceiveTab()

tabControl.pack(expand=1,fill='both')
root.mainloop()
