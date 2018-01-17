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

names_in_order = ['Abigail Guadarrama', 'Aditi Ramakrishnan', 'Alexandra Yoon-Hendricks', 'Alicia Lin', 'Anderson Lanham', 'Arushi Desai', 'Avni Prasad', 'Ayushi Gupta', 'Chaitanya Angadala', 'Clarissa Smathers', 'Cody Limber', 'Colin Hines', 'Drew Raguse', 'Ellen Luo', 'Evan Lisman', 'Gloria Chen', "Grace O'Toole", 'Haley Keglovits', 'Hersh Bhargava', 'Indu Pereira', 'Jason Chan', 'Jeffrey Wirjo', 'Jessica Liu', 'Jonathan Mendelson', 'Kate Swanson', 'Katrina Reynolds', 'Kiran Girish', 'Lilyanna Fu', 'Luke Zhang', 'Matthew Hilado', 'Maureen Sides', 'May Huang', 'Megha Torpunuri', 'Michael Chien', 'Michelle Brier', 'Mihir Gokhale', 'Nandika Donthi', 'Rahul Balakrishnan', 'Rivka Batlan', 'Sean Meng', 'Shaina Zuber', 'Simon Behar', 'Soham Kudtarkar', 'Sydney Yoon', 'Tanya Mahadwar', 'Tyler VanderLey', 'Uma Krishnan']

for name in names_in_order:
	if name in counts.keys():
		print(name + " " + str(counts[name]))
	else:
		print(name + " ")
