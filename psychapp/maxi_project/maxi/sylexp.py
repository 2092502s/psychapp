from random import shuffle

quantifiers = 	[["all","all"],
				["all","all"],
				["all","all"],
				["all","some"],
				["all","some"],
				["all","some"],
				["all","some"],
				["some","all"],
				["some","all"],
				["some","all"],
				["some","all"],
				["all","no"],
				["all","no"],
				["all","no"],
				["all","no"],
				["no","all"],
				["no","all"],
				["no","all"],
				["no","all"],
				["all","some-not"],
				["all","some-not"],
				["all","some-not"],
				["all","some-not"],
				["some-not","all"],
				["some-not","all"],
				["some-not","all"],
				["some-not","all"],
				["no","some"],
				["no","some"],
				["no","some"],
				["no","some"]]

terms = [["A","B","C","B"],
		["B","A","B","C"],
		["A","B","B","C"],
		["B","A","C","B"],
		["A","B","C","B"],
		["B","A","B","C"],
		["A","B","B","C"],
		["B","A","C","B"],
		["A","B","C","B"],
		["B","A","B","C"],
		["A","B","B","C"],
		["B","A","C","B"],
		["A","B","C","B"],
		["B","A","B","C"],
		["A","B","B","C"],
		["B","A","C","B"],
		["A","B","C","B"],
		["B","A","B","C"],
		["A","B","B","C"],
		["B","A","C","B"],
		["A","B","C","B"],
		["B","A","B","C"],
		["A","B","B","C"],
		["B","A","C","B"],
		["A","B","C","B"],
		["B","A","B","C"],
		["A","B","B","C"],
		["B","A","C","B"],
		["A","B","C","B"],
		["B","A","B","C"],
		["A","B","B","C"]]

answers = ["N","N","N","I","N","I","N","N","N","I","I","N","E","N","E","E","E",
           "N","N","N","O","N","N","N","N","O","N","O","O","O","O"]

codes = ["AA2","AA3","AA4","AI1","AI2","AI3","AI4","IA1","IA2","IA3","IA4","AE1","AE2","AE3",
         "AE4","EA1","EA2","EA3","EA4","AO1","AO2","AO3","AO4","OA1","OA2","OA3","OA4","EI1",
         "EI2","EI3","EI4"]



def create_syllogism_list(syl_string):					#Takes a string of index-integers as argument.

	#Obtain the string and split into a list of integers.
	syl_list = syl_string.split("-", syl_string.count("-"))
	#Turn characters into integers
	for x in syl_list:
		x = int(x)
	#Initialise syllogism-list
	syllogisms = [["",""]]*31		#"A" and "A" are merely placeholders.
	#print(syllogisms)	
	#Now, collect the premises according to these indexes
	for i in range(0,31):
		idx = int(syl_list[i])				#This obtained index is used to refer to elements in the original order.
		#print(idx)
		for j in (0,1):
			if j == 0:
				if quantifiers[idx][j] == "all":
					syllogisms[i][0] += "All " + terms[idx][0] + " are " + terms[idx][1]
				elif quantifiers[idx][j] == "no":
					syllogisms[i][0] += "No " + terms[idx][0] + " are " + terms[idx][1]
				elif quantifiers[idx][j] == "some-not":
					syllogisms[i][0] += "Some " + terms[idx][0] + " are not " + terms[idx][1]
				else:
					syllogisms[i][0] += "Some " + terms[idx][0] + " are " + terms[idx][1]
			else:
				if quantifiers[i][j] == "all":
					syllogisms[i][1] += "All " + terms[idx][2] + " are " + terms[idx][3]
				elif quantifiers[idx][j] == "no":
					syllogisms[i][1] += "No " + terms[idx][2] + " are " + terms[idx][3]
				elif quantifiers[idx][j] == "some-not":
					syllogisms[i][1] += "Some " + terms[idx][2] + " are not " + terms[idx][3]
				else:
					syllogisms[i][1] += "Some " + terms[idx][2] + " are " + terms[idx][3]					
	return syllogisms


def create_random_order():

	syl_list = list(range(0,31))
	shuffle(syl_list)
	syl_string = '-'.join(str(x) for x in syl_list)
	#print(syl_string)
	return syl_string


random_order = create_random_order()
syllogisms = create_syllogism_list(random_order)
print(syllogisms)
