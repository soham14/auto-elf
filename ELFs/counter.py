import csv
#from collections import counter

names = []

folder = input('What is the name of the file containing the ELF?\n>>> ')

with open(folder + '/ELF.csv', newline='') as csvfile:
	filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
	first1 = True
	for row in filereader:
		if first1:
			first1 = False
			continue
		first2 = True
		for entry in row:
			if first2:
				first2 = False
				continue
			if entry not in ['BLANK', 'FILL_IN', 'NONE_AVAILABLE', '']:
				names.append(entry)

counts = {x: names.count(x) / 2 for x in names}

names_in_order = ['Alan Turing', 'Grace Hopper', 'Ada Lovelace', 'Barbara Liskov', 'Alan Kay', 'Shafi Goldwasser', 'Anita Borg', 'Steve Wozniak', 'Sergey Brin', 'Tim Berners-Lee', 'Marissa Mayer', 'Sophie Wilson', 'Stephen Cook', 'Jean Sammet', 'Frances Allen', 'Radia Perlman', 'John Backus', 'Jeannette Wing', 'Rosalind Picard', 'Edgar Codd', 'John von Neumann', 'James Gosling', 'Brian Kernighan', 'Jennifer Widom', 'Edsger Dijkstra', 'Larry Page', 'Daphne Koller', 'Winifred Asprey', 'Annie Easley', 'Wang Xiaoyun', 'Alonzo Church', 'Robert Kahn', 'Adi Shamir', 'Jean Bartik', 'Yukihiro Matsumoto', 'Maria Klawe', 'Leslie Lamport', 'Dennis Ritchie', 'Karen Jones', 'Susan Landau', 'Vinod Khosla', 'Wendy Hall', 'Betty Holberton', 'Bjarne Stroustrup', 'Adele Goldberg', 'Bill Joy', 'Alan Perlis']

for name in names_in_order:
	if name in counts.keys():
		print(name + " " + str(counts[name]))
	else:
		print(name + " ")
