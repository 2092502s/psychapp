from django.shortcuts import render
from django.http import HttpResponse

from maxi.forms import TutorialForm, EndForm, QuestionForm, StartForm, ParticipantForm, ConsentForm
from maxi.models import Subject, Question, Participant
from time import gmtime, strftime
from datetime import tzinfo, timedelta, datetime
from random import shuffle, randint
import csv


##################################################################################################
##quantifiers = 	[["all","all"],
##				["all","all"],
##				["all","all"],
##				["all","some"],
##				["all","some"],
##				["all","some"],
##				["all","some"],
##				["some","all"],
##				["some","all"],
##				["some","all"],
##				["some","all"],
##				["all","no"],
##				["all","no"],
##				["all","no"],
##				["all","no"],
##				["no","all"],
##				["no","all"],
##				["no","all"],
##				["no","all"],
##				["all","some-not"],
##				["all","some-not"],
##				["all","some-not"],
##				["all","some-not"],
##				["some-not","all"],
##				["some-not","all"],
##				["some-not","all"],
##				["some-not","all"],
##				["no","some"],
##				["no","some"],
##				["no","some"],
##				["no","some"]]


quantifiers = [["all", "all"],				#1
                ["some", "all"],			#2
                ["some", "some"],			#3
                ["some-not", "all"],		#4
                ["some-not", "all"],		#5
                ["some-not", "some"],		#6
                ["some-not","some"],		#7
                ["some-not", "no"],			#8
                ["some-not","some-not"],	#9
                ["some-not","some-not"],	#10
                ["some-not","some-not"],	#11
                ["all", "all"],				#12
                ["all", "all"],				#13
                ["all","some"],				#14
                ["no", "all"],				#15
                ["all","no"],				#16
                ["no","some"],				#17
                ["some-not","all"],			#18
                ["some-not","all"]] 		#19
               

terms = [["A","B","C","B"],		#1
        ["B","A","C","B"],		#2
         ["A","B","C","B"],		#3
         ["B","A","C","B"],		#4
         ["A","B","B","C"],		#5
         ["B","A","C","B"],		#6
         ["A","B","C","B"],		#7
         ["A","B","C","B"],		#8
         ["A","B","C","B"],		#9
         ["A","B","B","C"],		#10
         ["B","A","B","C"],		#11
         ["A","B","B","C"],		#12
         ["B","A","B","C"],		#13
         ["B","A","C","B"],		#14
         ["B","A","C","B"], 	#15
         ["B","A","C","B"],		#16
         ["A","B","B","C"],		#17
         ["B","A","B","C"],		
         ["A","B","C","B"]]		
         
answers = [["NVC"], ["NVC"], ["NVC"], ["NVC"], ["NVC"], ["NVC"], ["NVC"], ["NVC"], ["NVC"], ["NVC"], ["NVC"],
           ["Aac","Iac"],["Iac","Ica"],["Iac","Ica"],["Eac","Eca"],["Oac"],["Oac","Oca"],["Oca"],["Oac"]]
           
codes = ["NP1", "NP2", "NP3", "NN1", "NN2", "NN3", "NN4", "NN5", "NN6", "NN7", "NN8", "VP1",
         "VP2", "VP3", "VN1", "VN2", "VN3", "VN4", "VN5"]        

##terms = [["A","B","C","B"],
##		["B","A","B","C"],
##		["A","B","B","C"],
##		["B","A","C","B"],
##		["A","B","C","B"],
##		["B","A","B","C"],
##		["A","B","B","C"],
##		["B","A","C","B"],
##		["A","B","C","B"],
##		["B","A","B","C"],
##		["A","B","B","C"],
##		["B","A","C","B"],
##		["A","B","C","B"],
##		["B","A","B","C"],
##		["A","B","B","C"],
##		["B","A","C","B"],
##		["A","B","C","B"],
##		["B","A","B","C"],
##		["A","B","B","C"],
##		["B","A","C","B"],
##		["A","B","C","B"],
##		["B","A","B","C"],
##		["A","B","B","C"],
##		["B","A","C","B"],
##		["A","B","C","B"],
##		["B","A","B","C"],
##		["A","B","B","C"],
##		["B","A","C","B"],
##		["A","B","C","B"],
##		["B","A","B","C"],
##		["A","B","B","C"]]
##
##answers = ["N","N","N","I","N","I","N","N","N","I","I","N","E","N","E","E","E",
##           "N","N","N","O","N","N","N","N","O","N","O","O","O","O"]

##codes = ["AA2","AA3","AA4","AI1","AI2","AI3","AI4","IA1","IA2","IA3","IA4","AE1","AE2","AE3",
##         "AE4","EA1","EA2","EA3","EA4","AO1","AO2","AO3","AO4","OA1","OA2","OA3","OA4","EI1",
##         "EI2","EI3","EI4"]



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
	for i in range(0,19):
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
				if quantifiers[idx][j] == "all":
					syllogisms[i].append("All " + terms[idx][2] + " are " + terms[idx][3])
				elif quantifiers[idx][j] == "no":
					syllogisms[i].append("No " + terms[idx][2] + " are " + terms[idx][3])
				elif quantifiers[idx][j] == "some-not":
					syllogisms[i].append("Some " + terms[idx][2] + " are not " + terms[idx][3])
				else:
					syllogisms[i].append("Some " + terms[idx][2] + " are " + terms[idx][3])				
	return syllogisms


def create_random_order():

	syl_list = list(range(0,19))		#simply create a list of 19 indices, shuffle and concatenate by '-'
	shuffle(syl_list)
	syl_string = '-'.join(str(x) for x in syl_list)
	print(syl_string)
	return syl_string					#will be saved in question-order field in Subject, effectively list of indices

### NOTE: THIS METHOD IS DEPRECATED, NOT ACTUALLY USED.
def create_code_list(): 			
	syl_list = list(range(0,19))	#Create a list of integers 0 to 18 (each nr serves as index in list of question-codes)
	syl_order = syl_list
	shuffle(syl_order)				#Shuffle the list - this contains the order
	syllogism_codes = syl_order[:]
	for i in range(19):
		idx = syl_order[i]			#As you loop, take the index
		syllogism_codes[i] = codes[idx] 	#Collect the question-code corresponding to the index

	syl_string = '-'.join(syllogism_codes) 		#Create a string with '-' as separator
	return syl_string

#################################################################################################
# CSV-generation
#format:
# SUBJECT_NR # QUESTION_CODE # DURATION
def generate_csv():
	#with open('static/docs/demographic_data.csv','w', newline="") as csvfile:
	with open('psychapp/psychapp/maxi_project/demographic_data.csv','w') as csvfile:
		writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(['ID','Gender','Age','Discipline', 'Confidence', 'Tutorial_Exp','Logic_Experience','Diagam_Use','Familiarity','Location','Condition'])
		all_subjects = Subject.objects.all()
		for subject in all_subjects:
			name = subject.name
			gender = subject.preq1
			age = str(subject.preq2)			#Note: it's a string
			confidence = subject.confidence
			condition = subject.condition
			discipline = subject.preq3
			logic = subject.post0
			diagram_use = subject.post1 		#Note: it's a string
			familiarity = subject.post2
			location = subject.post3
			
			tutorial_start = subject.tutorial_start
			tutorial_end = subject.start_time
			dt = tutorial_end - tutorial_start
			tut_duration = dt.total_seconds()
			
			#######WRITE INTO FILE
			writer.writerow([name, gender, age, discipline, confidence, tut_duration, logic, diagram_use, familiarity, location, condition])

	#with open('static/docs/experimental_data.csv','w', newline="") as csvfile:
	with open('psychapp/psychapp/maxi_project/experimental_data.csv','w') as csvfile:
		writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(['ID','Condition','Code','Order','Answer','Duration','Correct'])		
		all_subjects = Subject.objects.all()
		for subject in all_subjects:
			name = subject.name
			condition = subject.condition
			#PRINT SUBJECT
			subject_qs = Question.objects.filter(subject=subject)
			for question in subject_qs:
				#subject = question.subject
				nr_code = question.nr_code
				order_nr = question.order_nr
				answer  = question.answer
				if order_nr != "1":					#Unless it is the first question
					#print(order_nr)
					previous_nr = int(order_nr)-1	#Obtain the previous question-nr
					previous_ones = subject_qs.filter(order_nr=str(previous_nr))
					#print("Size is " + str(len(previous_ones)))
					previous = previous_ones[0]
					dt = question.endtime - previous.endtime
				else:
					dt = question.endtime - subject.start_time
				duration = dt.total_seconds()
				#time = dt.time
				#duration = str(time.minute * 60 + time.second)
				if answer in answers[int(nr_code)]:
					correct = 1
				else:
					correct = 0
				writer.writerow([name, condition, nr_code, order_nr, answer, duration, correct])
	return
#########################################################################################

def data(request):
	context_dict = {}
	return render(request, 'maxi/data.html', context_dict)	

def index(request):
	#start_time = strftime("%M:%S", gmtime())
	context_dict = {}
	submitted = False
	if request.method == 'POST':
		form1 = ParticipantForm(request.POST)
		form2 = ConsentForm(request.POST)
		#end_time = strftime("%M:%S", gmtime())
		if form1.is_valid() and form2.is_valid():
			participant = form1.save(commit=True)
			subject = form2.save(commit=False)					#Made false
			subject.syllogism_order = create_random_order()
			subject.save()
			id = subject.id
			context_dict['id']=id
			subject.name = id
			subject.tutorial_start = datetime.now()
			#subject.condition = str(randint(0,1)) 	#Randomly choose condition
			if id % 2 == 0:
				subject.condition = 0
			else:
				subject.condition = 1
			subject.save()		
			context_dict['submitted']=True
			return render(request, 'maxi/index.html', context_dict)
		else:
			print(form1.errors)
			print(form2.errors)
	else:
		form1 = ParticipantForm()
		form2 = ConsentForm()


	context_dict = {'form1': form1, 'form2':form2, 'submitted':submitted}
	return render(request, 'maxi/index.html', context_dict)

#def preexperiment(request, id):
#	context_dict = {}
#	context_dict['id']=id
#	#obtain user from database
#	instance = Subject.objects.get(id = id)
#	submitted=False
#
#	if request.method == 'POST':
#		form = IntroForm(request.POST, instance=instance)	#changed from 'or None'
#		if form.is_valid():
#			# print("Is preexperiment form valid?")
#			form.save()									#removed commit=True
#			# print("Now preexperimental data should be saved")
#			#return render(request, id)
#			submitted=True
#			context_dict['submitted']=True
#			return render(request, 'maxi/preexperiment.html', context_dict)		
#		else:
#			print(form.errors)
#	else:
#		form = IntroForm()
#
#		
#	context_dict['form'] = form 
#
#	context_dict['submitted']=submitted
#	return render(request, 'maxi/preexperiment.html', context_dict)

def tutorial(request, id):
	context_dict = {}
	context_dict['id']=id
	instance = Subject.objects.get(id=id)
	context_dict['condition'] = instance.condition
	submitted = False
	if request.method == 'POST':
		form1 = TutorialForm(request.POST, instance=instance)
		form2 = StartForm(request.POST)
		if form1.is_valid() and form2.is_valid():
			
			form1.save(commit=True)
			cd = form2.cleaned_data
			start = cd.get('start')
			#if start == True:
			#instance.start_time = strftime("%M:%S", gmtime())	
			instance.start_time = datetime.now()
			instance.save()
			submitted = True
			context_dict['submitted']=submitted
			return render(request, 'maxi/tutorial.html', context_dict)	
		else:
			print(form1.errors)
			print(form2.errors)
	else:
		form1 = TutorialForm()
		form2 = StartForm()
	context_dict['form1']=form1
	context_dict['form2']=form2
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
        context_dict['condition'] = instance.condition
        context_dict['submitted']=submitted
        context_dict['premise1'] = syllogism_list[int(current_q)][0]
        context_dict['image1']="images/" + syllogism_list[int(current_q)][0].replace(' ','') + ".png"
        context_dict['premise2'] = syllogism_list[int(current_q)][1]
        context_dict['image2'] = "images/" + syllogism_list[int(current_q)][1].replace(' ','') + ".png"
        context_dict['question_nr'] = int(question_nr)
        context_dict['next_nr'] = int(question_nr) + 1
        context_dict['syllogism_list'] = str(syllogism_list)
        context_dict['syl_list'] = str(syl_list)
        context_dict['current_q'] = current_q
		
        if request.method == 'POST':
                form = QuestionForm(request.POST)
                if form.is_valid():
                        answer = form.save(commit=False)
                        answer.nr_code= str(current_q)          #str of max_len 2
                        answer.order_nr= str(question_nr)
                        #answer.endtime= strftime("%M:%S", gmtime())
                        answer.endtime = datetime.now()
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
