from django import forms
from maxi.models import Subject, Question, Participant

class ConsentForm(forms.ModelForm):
	consent = forms.BooleanField(label="I confirm that I have understood this information, that participation is voluntary, and that I can withdraw at any time.")
	class Meta:
		model=Subject
		fields = ('consent',)

class ParticipantForm(forms.ModelForm):
	name = forms.CharField(max_length=100, )
	email = forms.EmailField()
	personal_nr = forms.IntegerField(label="Birth date YYYYMMDD")

	class Meta:
		model= Participant
		fields = ('name','email','personal_nr',)

class TutorialForm(forms.ModelForm):

	CONFIDENCE_LEVELS = (('1','Not confident at all'),('2','Not very confident'),('3','Unsure'),('4','Quite confident'),('5','Completely confident'))
	confidence = forms.ChoiceField(label="How confident did this tutorial make you feel in solving syllogisms?", choices=CONFIDENCE_LEVELS, widget=forms.RadioSelect)
	class Meta:
		model=Subject
		fields = ('confidence',)

class StartForm(forms.Form):
	start = forms.BooleanField(help_text="Tick to confirm you are ready to start the experiment")

ANSWER_OPTIONS = (('Aac','All A are C'),('Iac','Some A are C'),('Eac','No A are C'),('Oac','Some A are not C'),('Aca','All C are A'),('Ica','Some C are A'),('Eca','No C are A'),('Oca','Some C are not A'),('NVC','No valid conclusion'))

class QuestionForm(forms.ModelForm):
        answer = forms.ChoiceField(help_text="Select one valid conclusion (if several ones are valid, choose any of those)", choices=ANSWER_OPTIONS, widget=forms.RadioSelect)
        class Meta:
                model = Question
                fields = ('answer',)

		
class EndForm(forms.ModelForm):

	GENDERS = (('F', 'Female'),('M','Male'),('N', 'Not disclosed'))
	preq1 = forms.ChoiceField(choices=GENDERS, help_text="Are you male or female?",widget=forms.RadioSelect)
	preq2 = forms.IntegerField(help_text="What is your age?")
	DISCIPLINES = (('A', 'Arts & Humanities'), ('B','Computing & Engineering'), ('C','Social Sciences'),('D','Natural Sciences'),('E','Not at University'))
	preq3 = forms.ChoiceField(choices=DISCIPLINES, help_text="If at university, which discipline do you study?", widget=forms.RadioSelect)
	PROPOSITIONAL_LOGIC = (('1','None'),('2','Some'),('3','A lot'))
	post0 = forms.ChoiceField(choices=PROPOSITIONAL_LOGIC, help_text="How much experience do you have with syllogisms and propositional logic from before?", widget=forms.RadioSelect)
	USE_OF_DIAGRAMS = (('1','Never'),('2','Rarely'),('3','About half of the time'),('4','Very often'),('5','Every time'))	
	post1 = forms.ChoiceField(choices=USE_OF_DIAGRAMS, help_text="To what extent did you make use of diagrams in your solutions?", widget=forms.RadioSelect)
	FAMILIARITY2 = (('1','Not familiar'),('2','Vaguely familiar'),('3','Very familiar'))
	post2 = forms.ChoiceField(choices=FAMILIARITY2, help_text="How familiar were you with the diagram used?", widget=forms.RadioSelect)
	NOISE = (('1','Very Noisy'),('2','Noisy'), ('3','Normal'),('4','Calm'),('5','Very Calm'))
	post3 = forms.ChoiceField(choices=NOISE, help_text="How easy was it to concentrate in the place that you did the experiment?", widget=forms.RadioSelect)
	
	class Meta:
		model = Subject
		fields = ('preq1', 'preq2','preq3','post0','post1', 'post2','post3',)
