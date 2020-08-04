from tkinter import *
from tkinter import ttk
from tkinter import filedialog

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
		except:                     # <- naked except is a bad idea
			showerror("Open Source File", "Failed to read file\n'%s'" % fname)
		return
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

	generatePrimeButton = Button(tab2, text="Generate Prime Pair")
	generatePrimeButton.grid(row=2, column=1, sticky="ew")

	generateKeyButton = Button(tab2, text="Generate Keys")
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
