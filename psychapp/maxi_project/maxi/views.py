from django.shortcuts import render
from django.http import HttpResponse
#from maxi.forms import IntroForm, EndForm, ConsentForm, TestForm1, TestForm2, TestForm3, TestForm4, TestForm5, TestForm6, TestForm7, TestForm8, TestForm9, TestForm10, TestForm11, \
#TestForm12, TestForm13, TestForm14, TestForm15, TestForm16, TestForm17, TestForm18, TestForm19, TestForm20, TestForm21, TestForm22, TestForm23, TestForm24, TestForm25, TestForm26, \
#TestForm27, TestForm28, TestForm29, TestForm30, TestForm31
from maxi.forms import IntroForm, EndForm, ConsentForm, QuestionForm, StartForm
from maxi.models import Subject, Question
from time import gmtime, strftime
from random import shuffle
import csv

##################################################################################################
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

##################################################################################################
def create_syllogism_list(syl_string):					#Takes a string of index-integers as argument.

	#Obtain the string and split into a list of integers.
	syl_list = syl_string.split("-", syl_string.count("-"))
	#Turn characters into integers
	for x in syl_list:
		x = int(x)
	#Initialise syllogism-list
	syllogisms = []		#"A" and "A" are merely placeholders.
		
	#Now, collect the premises according to these indexes
	for i in range(0,31):
		idx = int(syl_list[i])				#This obtained index is used to refer to elements in the original order.
		syllogisms.append([])
		for j in (0,1):
			if j == 0:
				if quantifiers[idx][j] == "all":
					syllogisms[i].append("All " + terms[idx][0] + " are " + terms[idx][1])
				elif quantifiers[idx][j] == "no":
					syllogisms[i].append("No " + terms[idx][0] + " are " + terms[idx][1])
				elif quantifiers[idx][j] == "some-not":
					syllogisms[i].append("Some " + terms[idx][0] + " are not " + terms[idx][1])
				else:
					syllogisms[i].append("Some " + terms[idx][0] + " are " + terms[idx][1])
			else:
				if quantifiers[i][j] == "all":
					syllogisms[i].append("All " + terms[idx][2] + " are " + terms[idx][3])
				elif quantifiers[idx][j] == "no":
					syllogisms[i].append("No " + terms[idx][2] + " are " + terms[idx][3])
				elif quantifiers[idx][j] == "some-not":
					syllogisms[i].append("Some " + terms[idx][2] + " are not " + terms[idx][3])
				else:
					syllogisms[i].append("Some " + terms[idx][2] + " are " + terms[idx][3])				
	return syllogisms


def create_random_order():

	syl_list = list(range(0,31))
	shuffle(syl_list)
	syl_string = '-'.join(str(x) for x in syl_list)
	print(syl_string)
	return syl_string


def create_code_list():
	syl_list = list(range(0,31))
	syl_order = syl_list
	shuffle(syl_order)
	syllogism_codes = syl_order[:]
	for i in range(31):
		idx = syl_order[i]
		syllogism_codes[i] = codes[idx]

	syl_string = '-'.join(syllogism_codes)
	return syl_string

#################################################################################################
# CSV-generation
#format:
# SUBJECT_NR # QUESTION_CODE # DURATION
def generate_csv():
	with open('demographic_data.csv','w', newline="") as csvfile:
		writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		#writer.writerow(["ID","Gender","Age","Discipline","Diagam_Use","Familiarity"])
		all_subjects = Subject.objects.all()
		for subject in all_subjects:
			name = subject.name
			gender = subject.preq1
			age = str(subject.preq2)			#Note: it's a string
			discipline = subject.preq3
			diagram_use = subject.post1 		#Note: it's a string
			familiarity = subject.post2
			
			#######WRITE INTO FILE
			writer.writerow([name, gender, age, discipline, diagram_use, familiarity])

	with open('experimental_data.csv','w', newline="") as csvfile:
		writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		#writer.writerow(["ID","Code","Order","Answer","Endtime","Correct"])		
		all_subjects = Subject.objects.all()
		for subject in all_subjects:
			name = subject.name
			#PRINT SUBJECT
			subject_qs = Question.objects.filter(subject=subject)
			for question in subject_qs:
				#subject = question.subject
				nr_code = question.nr_code
				order_nr = question.order_nr
				answer  = question.answer
				endtime = question.endtime
				if answer == answers[int(nr_code)]:
					correct = 1
				else:
					correct = 0
				writer.writerow([name, nr_code, order_nr, answer, endtime, correct])
	return
#########################################################################################

def index(request):
	#start_time = strftime("%M:%S", gmtime())
	context_dict = {}
	submitted = False
	if request.method == 'POST':
		form = ConsentForm(request.POST)
		#end_time = strftime("%M:%S", gmtime())
		if form.is_valid():
			subject = form.save(commit=False)		#Made false
			subject.syllogism_order = create_random_order()
			subject.save()
			id = subject.id
			context_dict['id']=id
			subject.name = id
			subject.save()		
			context_dict['submitted']=True
			return render(request, 'maxi/index.html', context_dict)
		else:
			print(form.errors)
	else:
		form = ConsentForm()


	context_dict = {'form': form, 'submitted':submitted}
	return render(request, 'maxi/index.html', context_dict)

def preexperiment(request, id):
	context_dict = {}
	context_dict['id']=id
	#obtain user from database
	instance = Subject.objects.get(id = id)
	submitted=False

	if request.method == 'POST':
		form = IntroForm(request.POST, instance=instance)	#changed from 'or None'
		if form.is_valid():
			# print("Is preexperiment form valid?")
			form.save()									#removed commit=True
			# print("Now preexperimental data should be saved")
			#return render(request, id)
			submitted=True
			context_dict['submitted']=True
			return render(request, 'maxi/preexperiment.html', context_dict)		
		else:
			print(form.errors)
	else:
		form = IntroForm()

		
	context_dict['form'] = form 

	context_dict['submitted']=submitted
	return render(request, 'maxi/preexperiment.html', context_dict)

def tutorial(request, id):
	context_dict = {}
	context_dict['id']=id
	instance = Subject.objects.get(id=id)
	submitted = False
	if request.method == 'POST':
		form = StartForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			start = cd.get('start')
			#if start == True:
			instance.start_time = strftime("%M:%S", gmtime())
			instance.save()
			submitted=True
			context_dict['submitted']=submitted
			return render(request, 'maxi/tutorial.html', context_dict)	
		else:
			print(form.errors)
	else:
		form = StartForm()
	context_dict['form']=form
	context_dict['submitted']=submitted
	return render(request, 'maxi/tutorial.html', context_dict)

def experiment(request, id, question_nr):
        context_dict = {}
        submitted = False
        #obtain user from database
        instance = Subject.objects.get(id = id)
        syl_order = instance.syllogism_order
        syl_list = syl_order.split("-", syl_order.count("-"))
        current_q = syl_list[int(question_nr) - 1]
	
        syllogism_list = create_syllogism_list(syl_order)

        context_dict['id']= id
        context_dict['submitted']=submitted
        context_dict['premise1'] = syllogism_list[int(current_q)][0]
        context_dict['premise2'] = syllogism_list[int(current_q)][1]
        context_dict['question_nr'] = int(question_nr)
        context_dict['next_nr'] = int(question_nr) + 1
        if request.method == 'POST':
                form = QuestionForm(request.POST)
                if form.is_valid():
                        answer = form.save(commit=False)
                        answer.nr_code= str(current_q)          #str of max_len 2
                        answer.order_nr= str(question_nr)
                        answer.endtime= strftime("%M:%S", gmtime())
                        answer.subject = instance
                        answer.save()
                        submitted=True
                        context_dict['submitted']=submitted
                        return render(request, 'maxi/experiment.html', context_dict)
                        #if int(question_nr) <= 30:
                        #        return experiment(request,id,int(question_nr) + 1)
                        #else:
                        #        return postexperiment(request,id)

                        #Save this question to the instance one-to-many field
                else:
                        print(form.errors)
        else:
                form = QuestionForm()

        context_dict['form'] = form 
        context_dict['submitted']=submitted

        return render(request, 'maxi/experiment.html', context_dict)
	
def postexperiment(request, id):
	#obtain user from database
	instance = Subject.objects.get(id = id)
	context_dict = {}
	context_dict['id']=id
	submitted = False
	if request.method == 'POST':
		form = EndForm(request.POST, instance=instance)	#changed from 'or None'
		if form.is_valid():
			#print("Is postexperiment form valid?")
			form.save()											#commit=True
			#print("Now postexperimental data should be saved")	
			submitted=True
			context_dict['submitted']=submitted
			return render(request, 'maxi/postexperiment.html', context_dict)	
		else:
			print(form.errors)
	else:
		form = EndForm()
		
	context_dict['form'] = form 

	return render(request, 'maxi/postexperiment.html', context_dict)
	
def debriefing(request):
	context_dict = {'dummy': "dummy"}
	generate_csv()
	return render(request, 'maxi/debriefing.html', context_dict)

# Create your views here.
