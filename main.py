analyse = True

while analyse:
	valid_book = False
	print("""Which book would you like to analyse? 
	1. Alice in Wonderland
	2. Treasure Island
	3. Wizard of Oz
	4. Jekyll & Hyde
	5. Harry Potter and the Philosopher's Stone
	6. Lord of the Rings: Fellowship of the Ring""")
	book = input()
	while not valid_book:
		if book == "1":
			print("You are analysing Alice in Wonderland")
			book = open("alice.txt")
			valid_book = True
		elif book == "2":
			print("You are analysing Treasure Island")
			book = open("treasureIsland.txt")
			valid_book = True
		elif book == "3":
			print("You are analysing The Wizard of Oz")
			book = open("wizardofoz.txt")
			valid_book = True
		elif book == "4":
			print("You are analysing Jekyll and Hyde")
			book = open("jekyll.txt")
			valid_book = True
		elif book == "5":
			print("You are analysing Harry Potter and the Philosopher's Stone")
			book = open("harrypotter_1.txt")
			valid_book = True
		elif book == "6":
			print("You are analysing The Fellowship of the Ring")
			book = open("fellowship.txt")
			valid_book = True
		else:
			print("You need to enter 1,2,3,4 or 5.")
			book = input()
