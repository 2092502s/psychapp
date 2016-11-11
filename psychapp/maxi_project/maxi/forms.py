from django import forms
from maxi.models import Subject, Question

class ConsentForm(forms.ModelForm):
	#name = forms.CharField(max_length=500, help_text="Your Name")
	consent = forms.BooleanField(help_text="I consent to participate")
	class Meta:
		model = Subject
		fields = ('consent',)

class StartForm(forms.Form):
	start = forms.BooleanField(help_text="Tick to confirm you are ready to start the experiment")

class IntroForm(forms.ModelForm):

	GENDERS = (('F', 'Female'),('M','Male'),('N', 'Not disclosed'))
	preq1 = forms.ChoiceField(choices=GENDERS, help_text="Are you male or female?",widget=forms.RadioSelect)
	preq2 = forms.IntegerField(help_text="What is your age?")
	DISCIPLINES = (('A', 'Arts & Humanities'), ('B','Computing & Engineering'), ('C','Social Sciences'),('D','Natural Sciences'),('E','Not at University'))
	preq3 = forms.ChoiceField(choices=DISCIPLINES, help_text="If at university, which discipline do you study?", widget=forms.RadioSelect)
	#FAMILIARITY = (('A','No familiarity at all'),('B','Vaguely familiar'),('C','Very familiar'))
	#preq4 = forms.ChoiceField(choices=FAMILIARITY, help_text="How familiar are you with syllogisms?", widget=forms.CheckboxSelectMultiple)

	class Meta:
		model = Subject
		fields = ('preq1', 'preq2','preq3',)

ANSWER_OPTIONS = (('A','All C are A'),('B','No C are A'),('C','Some C are A'),('D','Some C are not A'),('E','No valid conclusion'))

class QuestionForm(forms.ModelForm):
        answer = forms.ChoiceField(help_text="Select the valid conclusion", choices=ANSWER_OPTIONS, widget=forms.RadioSelect)
        class Meta:
                model = Question
                fields = ('answer',)

##class TestForm1(forms.ModelForm):
##	ex1 = forms.ChoiceField(help_text= "Select the correct answer", choices=ANSWER_OPTIONS)
##	class Meta:
##		model = Subject
##		fields = ('ex1',)
##
##class TestForm2(forms.ModelForm):
##	ex2 = forms.ChoiceField(help_text="Select the correct answer", choices=ANSWER_OPTIONS)	
##	class Meta:
##		model = Subject
##		fields = ('ex2',)
##
##class TestForm3(forms.ModelForm):	
##	ex3 = forms.ChoiceField(help_text="Select the correct answer", choices=ANSWER_OPTIONS)
##	class Meta:
##		model = Subject
##		fields = ('ex3',)
##
##class TestForm4(forms.ModelForm):
##	ex4 = forms.ChoiceField(help_text="Select the correct answer", choices=ANSWER_OPTIONS)	
##	class Meta:
##		model = Subject
##		fields = ('ex4',)
##		
##class TestForm5(forms.ModelForm):
##	ex5 = forms.ChoiceField(help_text="Is the conclusion valid?", choices=ANSWER_OPTIONS)
##	class Meta:
##		model = Subject
##		fields = ('ex5',)
##
##class TestForm6(forms.ModelForm):
##	ex6 = forms.ChoiceField(help_text= "Select the correct answer", choices=ANSWER_OPTIONS)
##	class Meta:
##		model = Subject
##		fields = ('ex6',)
##
##class TestForm7(forms.ModelForm):
##	ex7 = forms.ChoiceField(help_text="Select the correct answer", choices=ANSWER_OPTIONS)	
##	class Meta:
##		model = Subject
##		fields = ('ex7',)
##
##class TestForm8(forms.ModelForm):	
##	ex8 = forms.ChoiceField(help_text="Select the correct answer", choices=ANSWER_OPTIONS)
##	class Meta:
##		model = Subject
##		fields = ('ex8',)
##
##class TestForm9(forms.ModelForm):
##	ex9 = forms.ChoiceField(help_text="Select the correct answer", choices=ANSWER_OPTIONS)	
##	class Meta:
##		model = Subject
##		fields = ('ex9',)
##		
##class TestForm10(forms.ModelForm):
##	ex10 = forms.ChoiceField(help_text="Is the conclusion valid?", choices=ANSWER_OPTIONS)
##	class Meta:
##		model = Subject
##		fields = ('ex10',)
##		
##class TestForm11(forms.ModelForm):
##	ex11 = forms.ChoiceField(help_text= "Select the correct answer", choices=ANSWER_OPTIONS)
##	class Meta:
##		model = Subject
##		fields = ('ex11',)
##
##class TestForm12(forms.ModelForm):
##	ex12 = forms.ChoiceField(help_text="Select the correct answer", choices=ANSWER_OPTIONS)	
##	class Meta:
##		model = Subject
##		fields = ('ex12',)
##
##class TestForm13(forms.ModelForm):	
##	ex13 = forms.ChoiceField(help_text="Select the correct answer", choices=ANSWER_OPTIONS)
##	class Meta:
##		model = Subject
##		fields = ('ex13',)
##
##class TestForm14(forms.ModelForm):
##	ex14 = forms.ChoiceField(help_text="Select the correct answer", choices=ANSWER_OPTIONS)	
##	class Meta:
##		model = Subject
##		fields = ('ex14',)
##		
##class TestForm15(forms.ModelForm):
##	ex15 = forms.ChoiceField(help_text="Is the conclusion valid?", choices=ANSWER_OPTIONS)
##	class Meta:
##		model = Subject
##		fields = ('ex15',)
##		
##class TestForm16(forms.ModelForm):
##	ex16 = forms.ChoiceField(help_text= "Select the correct answer", choices=ANSWER_OPTIONS)
##	class Meta:
##		model = Subject
##		fields = ('ex16',)
##
##class TestForm17(forms.ModelForm):
##	ex17 = forms.ChoiceField(help_text="Select the correct answer", choices=ANSWER_OPTIONS)	
##	class Meta:
##		model = Subject
##		fields = ('ex17',)
##
##class TestForm18(forms.ModelForm):	
##	ex18 = forms.ChoiceField(help_text="Select the correct answer", choices=ANSWER_OPTIONS)
##	class Meta:
##		model = Subject
##		fields = ('ex18',)
##
##class TestForm19(forms.ModelForm):
##	ex19 = forms.ChoiceField(help_text="Select the correct answer", choices=ANSWER_OPTIONS)	
##	class Meta:
##		model = Subject
##		fields = ('ex19',)
##		
##class TestForm20(forms.ModelForm):
##	ex20 = forms.ChoiceField(help_text="Is the conclusion valid?", choices=ANSWER_OPTIONS)
##	class Meta:
##		model = Subject
##		fields = ('ex20',)
##
##class TestForm21(forms.ModelForm):
##	ex21 = forms.ChoiceField(help_text= "Select the correct answer", choices=ANSWER_OPTIONS)
##	class Meta:
##		model = Subject
##		fields = ('ex21',)
##
##class TestForm22(forms.ModelForm):
##	ex22 = forms.ChoiceField(help_text="Select the correct answer", choices=ANSWER_OPTIONS)	
##	class Meta:
##		model = Subject
##		fields = ('ex22',)
##
##class TestForm23(forms.ModelForm):	
##	ex23 = forms.ChoiceField(help_text="Select the correct answer", choices=ANSWER_OPTIONS)
##	class Meta:
##		model = Subject
##		fields = ('ex23',)
##
##class TestForm24(forms.ModelForm):
##	ex24 = forms.ChoiceField(help_text="Select the correct answer", choices=ANSWER_OPTIONS)	
##	class Meta:
##		model = Subject
##		fields = ('ex24',)
##		
##class TestForm25(forms.ModelForm):
##	ex25 = forms.ChoiceField(help_text="Is the conclusion valid?", choices=ANSWER_OPTIONS)
##	class Meta:
##		model = Subject
##		fields = ('ex25',)
##		
##class TestForm26(forms.ModelForm):
##	ex26 = forms.ChoiceField(help_text= "Select the correct answer", choices=ANSWER_OPTIONS)
##	class Meta:
##		model = Subject
##		fields = ('ex26',)
##
##class TestForm27(forms.ModelForm):
##	ex27 = forms.ChoiceField(help_text="Select the correct answer", choices=ANSWER_OPTIONS)	
##	class Meta:
##		model = Subject
##		fields = ('ex27',)
##
##class TestForm28(forms.ModelForm):	
##	ex28 = forms.ChoiceField(help_text="Select the correct answer", choices=ANSWER_OPTIONS)
##	class Meta:
##		model = Subject
##		fields = ('ex28',)
##
##class TestForm29(forms.ModelForm):
##	ex29 = forms.ChoiceField(help_text="Select the correct answer", choices=ANSWER_OPTIONS)	
##	class Meta:
##		model = Subject
##		fields = ('ex29',)
##		
##class TestForm30(forms.ModelForm):
##	ex30 = forms.ChoiceField(help_text="Is the conclusion valid?", choices=ANSWER_OPTIONS)
##	class Meta:
##		model = Subject
##		fields = ('ex30',)
##		
##class TestForm31(forms.ModelForm):
##	ex31 = forms.ChoiceField(help_text="Is the conclusion valid?", choices=ANSWER_OPTIONS)
##	class Meta:
##		model = Subject
##		fields = ('ex31',)
		
class EndForm(forms.ModelForm):
	USE_OF_DIAGRAMS = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'))	
	post1 = forms.ChoiceField(choices=USE_OF_DIAGRAMS, help_text="To what extent did you make use of diagrams in your solutions?", widget=forms.RadioSelect)
	FAMILIARITY2 = (('1','Not familiar'),('2','Vaguely familiar'),('3','Very familiar'))
	post2 = forms.ChoiceField(choices=FAMILIARITY2, help_text="How familiar were you with the diagram used?", widget=forms.RadioSelect)

	
	class Meta:
		model = Subject
		fields = ('post1', 'post2',)
