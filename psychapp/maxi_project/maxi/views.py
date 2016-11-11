from django.shortcuts import render
from django.http import HttpResponse
#from maxi.forms import IntroForm, EndForm, ConsentForm, TestForm1, TestForm2, TestForm3, TestForm4, TestForm5, TestForm6, TestForm7, TestForm8, TestForm9, TestForm10, TestForm11, \
#TestForm12, TestForm13, TestForm14, TestForm15, TestForm16, TestForm17, TestForm18, TestForm19, TestForm20, TestForm21, TestForm22, TestForm23, TestForm24, TestForm25, TestForm26, \
#TestForm27, TestForm28, TestForm29, TestForm30, TestForm31
from maxi.forms import IntroForm, EndForm, ConsentForm, QuestionForm
from maxi.models import Subject, Question
from time import gmtime, strftime
from random import shuffle

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

def index(request):
	#start_time = strftime("%M:%S", gmtime())
	context_dict = {}
	if request.method == 'POST':
		form = ConsentForm(request.POST)
		#end_time = strftime("%M:%S", gmtime())
		if form.is_valid():
			subject = form.save(commit=False)		#Made false
			subject.syllogism_order = create_random_order()
			subject.save()
			id = subject.id
			context_dict['id']=id
			#context_dict['start'] = start_time
			#context_dict['end'] = end_time
			if subject == True: 
				return index(request)
			else:
				return render(request, 'maxi/index.html', context_dict)
		else:
			print(form.errors)
	else:
		form = ConsentForm()

	context_dict = {'form': form}
	return render(request, 'maxi/index.html', context_dict)

def preexperiment(request, id):
	context_dict = {}
	#obtain user from database
	instance = Subject.objects.get(id = id)

	if request.method == 'POST':
		form = IntroForm(request.POST, instance=instance)	#changed from 'or None'
		if form.is_valid():
			# print("Is preexperiment form valid?")
			form.save()									#removed commit=True
			# print("Now preexperimental data should be saved")
			#return render(request, id)			
		else:
			print(form.errors)
	else:
		form = IntroForm()
		
	context_dict['form'] = form 
	context_dict['id']=id
	return render(request, 'maxi/preexperiment.html', context_dict)

def tutorial(request, id):
	context_dict = {}
	context_dict['id']=id
	return render(request, 'maxi/tutorial.html', context_dict)

def experiment(request, id, question_nr):
        context_dict = {}
        #obtain user from database
        instance = Subject.objects.get(id = id)
        syl_order = instance.syllogism_order
        syl_list = syl_order.split("-", syl_order.count("-"))
        current_q = syl_list[int(question_nr) - 1]
	
        syllogism_list = create_syllogism_list(syl_order)

        if request.method == 'POST':
                form = QuestionForm(request.POST)
                if form.is_valid():
                        answer = form.save(commit=False)
                        answer.nr_code= str(current_q)          #str of max_len 2
                        answer.order_nr= str(question_nr)
                        answer.endtime= strftime("%M:%S", gmtime())
                        answer.subject = instance
                        answer.save()

                        #Save this question to the instance one-to-many field
                else:
                        print(form.errors)
        else:
                form = QuestionForm()

        context_dict['question_nr'] = int(question_nr)
        context_dict['next_nr'] = int(question_nr) + 1
        context_dict['form'] = form 
        context_dict['id']= id
        context_dict['premise1'] = syllogism_list[int(current_q)][0]
        context_dict['premise2'] = syllogism_list[int(current_q)][1]
	
        return render(request, 'maxi/experiment.html', context_dict)


##	if question_nr == 1:
##		if request.method == 'POST':			
##			instance.endtime1 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime1
##			form = TestForm1(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm1()
##			instance.starttime1 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime1	
##	elif question_nr == 2:
##		if request.method == 'POST':			
##			instance.endtime2 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime2
##			form = TestForm2(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm2()
##			instance.starttime2 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime2	
##	elif question_nr == 3:
##		if request.method == 'POST':			
##			instance.endtime3 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime3
##			form = TestForm3(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm3()
##			instance.starttime3 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime3
##	elif question_nr == 4:
##		if request.method == 'POST':			
##			instance.endtime4 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime4
##			form = TestForm4(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm4()
##			instance.starttime4 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime4	
##	elif question_nr == 5:
##		if request.method == 'POST':			
##			instance.endtime5 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime5
##			form = TestForm5(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm5()
##			instance.starttime5 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime5	
##			
##	elif question_nr == 6:
##		if request.method == 'POST':			
##			instance.endtime6 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime6
##			form = TestForm6(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm6()
##			instance.starttime6 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime6
##	elif question_nr == 7:
##		if request.method == 'POST':			
##			instance.endtime7 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime7
##			form = TestForm7(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm7()
##			instance.starttime7 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime7		
##	elif question_nr == 8:
##		if request.method == 'POST':			
##			instance.endtime8 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime8
##			form = TestForm8(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm8()
##			instance.starttime8 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime8
##	elif question_nr == 9:
##		if request.method == 'POST':			
##			instance.endtime9 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime9
##			form = TestForm9(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm9()
##			instance.starttime9 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime9		
##	elif question_nr == 10:
##		if request.method == 'POST':			
##			instance.endtime10 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime10
##			form = TestForm10(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm10()
##			instance.starttime10 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime10
##	elif question_nr == 11:
##		if request.method == 'POST':			
##			instance.endtime11 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime11
##			form = TestForm11(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm11()
##			instance.starttime11 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime11
##	elif question_nr == 12:
##		if request.method == 'POST':			
##			instance.endtime12 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime12
##			form = TestForm12(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm12()
##			instance.starttime12 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime12
##	elif question_nr == 13:
##		if request.method == 'POST':			
##			instance.endtime13 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime13
##			form = TestForm13(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm13()
##			instance.starttime13 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime13
##	elif question_nr == 14:
##		if request.method == 'POST':			
##			instance.endtime14 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime14
##			form = TestForm14(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm14()
##			instance.starttime14 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime14
##	elif question_nr == 15:
##		if request.method == 'POST':			
##			instance.endtime15 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime15
##			form = TestForm15(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm15()
##			instance.starttime15 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime15
##	elif question_nr == 16:
##		if request.method == 'POST':			
##			instance.endtime16 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime16
##			form = TestForm16(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm16()
##			instance.starttime16 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime16
##	elif question_nr == 17:
##		if request.method == 'POST':			
##			instance.endtime17 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime17
##			form = TestForm17(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm17()
##			instance.starttime17 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime17
##	elif question_nr == 18:
##		if request.method == 'POST':			
##			instance.endtime18 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime18
##			form = TestForm18(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm18()
##			instance.starttime18 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime18
##	elif question_nr == 19:
##		if request.method == 'POST':			
##			instance.endtime19 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime19
##			form = TestForm19(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm19()
##			instance.starttime19 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime19
##	elif question_nr == 20:
##		if request.method == 'POST':			
##			instance.endtime20 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime20
##			form = TestForm20(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm20()
##			instance.starttime20 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime20
##	elif question_nr == 21:
##		if request.method == 'POST':			
##			instance.endtime21 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime21
##			form = TestForm21(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm21()
##			instance.starttime21 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime21		
##	elif question_nr == 22:
##		if request.method == 'POST':			
##			instance.endtime22 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime22
##			form = TestForm22(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm22()
##			instance.starttime22 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime22
##	elif question_nr == 23:
##		if request.method == 'POST':			
##			instance.endtime23 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime23
##			form = TestForm23(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm23()
##			instance.starttime23 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime23		
##	elif question_nr == 24:
##		if request.method == 'POST':			
##			instance.endtime24 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime24
##			form = TestForm24(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm24()
##			instance.starttime24 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime24
##	elif question_nr == 25:
##		if request.method == 'POST':			
##			instance.endtime25 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime25
##			form = TestForm25(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm25()
##			instance.starttime25 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime25
##	elif question_nr == 26:
##		if request.method == 'POST':			
##			instance.endtime26 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime26
##			form = TestForm26(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm26()
##			instance.starttime26 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime26
##	elif question_nr == 27:
##		if request.method == 'POST':			
##			instance.endtime27 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime27
##			form = TestForm27(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm27()
##			instance.starttime27 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime27
##	elif question_nr == 28:
##		if request.method == 'POST':			
##			instance.endtime28 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime28
##			form = TestForm28(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm28()
##			instance.starttime28 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime28
##	elif question_nr == 29:
##		if request.method == 'POST':			
##			instance.endtime29 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime29
##			form = TestForm29(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm29()
##			instance.starttime29 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime29
##	elif question_nr == 30:
##		if request.method == 'POST':			
##			instance.endtime30 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime30
##			form = TestForm30(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm30()
##			instance.starttime30 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime30
##	else:
##		if request.method == 'POST':			
##			instance.endtime31 = strftime("%M:%S", gmtime())
##			instance.save()
##			context_dict['end'] = instance.endtime31
##			form = TestForm31(request.POST, instance=instance)		#changed from 'or None'
##			if form.is_valid():
##				form.save(commit=True)											#commit=True
##				# print("Now experimental data should be saved") # print("Now enddate should be saved")
##				#return experiment1(request, id)			
##			else:
##				print(form.errors)
##		else:
##			form = TestForm31()
##			instance.starttime31 = strftime("%M:%S", gmtime())
##			instance.save()
##			# print("Now startdate should be saved")
##			#how about if I save start-time here
##			context_dict['start'] = instance.starttime31

	
def postexperiment(request, id):

	#obtain user from database
	instance = Subject.objects.get(id = id)
	context_dict = {}
	if request.method == 'POST':
		form = EndForm(request.POST, instance=instance)	#changed from 'or None'
		if form.is_valid():
			#print("Is postexperiment form valid?")
			form.save()											#commit=True
			#print("Now postexperimental data should be saved")		
		else:
			print(form.errors)
	else:
		form = EndForm()
		
	context_dict['form'] = form 
	context_dict['id']=id
	return render(request, 'maxi/postexperiment.html', context_dict)
	
def debriefing(request):
	context_dict = {'dummy': "dummy"}
	return render(request, 'maxi/debriefing.html', context_dict)

# Create your views here.
