from django.db import models


# Create your models here.
class Participant(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=254, unique=True)
	personal_nr = models.IntegerField()

	def __unicode__(self):
		return self.name

class Subject(models.Model):
	consent = models.BooleanField(default=False)	
	name = models.IntegerField(null=True)
	#subject_nr = models.PositiveSmallIntegerField(unique=True)
	syllogism_order = models.CharField(max_length=500, null=False)
	#questions = models.ForeignKey(Question)
	#id = models.AutoField(primary_key=True)
	condition = models.CharField(max_length=1, null=True)
	
	tutorial_start = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
	start_time = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
	
	CONFIDENCE_LEVELS = (('1','Not confident at all'),('2','Not very confident'),('3','Unsure'),('4','Quite confident'),('5','Completely confident'))
	confidence = models.CharField(max_length=1, choices=CONFIDENCE_LEVELS, blank=True, null=True)


	GENDERS = (('F', 'Female'),('M','Male'),('N', 'Not disclosed'))
	preq1 = models.CharField(max_length=1, choices=GENDERS, blank=True, null=True)
	preq2 = models.IntegerField(blank=True, null=True)
	DISCIPLINES = (('A', 'Arts & Humanities'), ('B','Computing & Engineering'), ('C','Social Sciences'),('D','Natural Sciences'),('E','Not at University'))
	preq3 = models.CharField(max_length=1, choices=DISCIPLINES, blank=True, null=True)
	#FAMILIARITY = (('A','No familiarity at all'),('B','Vaguely familiar'),('C','Very familiar'))
	#preq4 = models.CharField(max_length=1, choices=FAMILIARITY, blank=True, null=True)

	#How much experience do you have with syllogisms and propositional logic from before?
	PROPOSITIONAL_LOGIC = (('1','None'),('2','Some'),('3','A lot'))
	post0 = models.CharField(max_length=1, choices=PROPOSITIONAL_LOGIC, blank=True, null=True)
	
	USE_OF_DIAGRAMS = (('1','Never'),('2','Rarely'),('3','About half of the time'),('4','Very often'),('5','Every time'))
	post1 = models.CharField(max_length=1, choices=USE_OF_DIAGRAMS, blank=True, null=True)
	FAMILIARITY2 = (('1','Not familiar'),('2','Vaguely familiar'),('3','Very familiar'))
	post2 = models.CharField(max_length=1, choices=FAMILIARITY2, blank=True, null=True)
	NOISE = (('1','Very Noisy'),('2','Noisy'), ('3','Normal'),('4','Calm'),('5','Very Calm'))
	post3 = models.CharField(max_length=1, choices=NOISE, blank=True, null=True)

	def __unicode__(self):
		return str(self.name)
		
	def __str__(self):
		return str(self.name)

class Question(models.Model):
        ANSWER_OPTIONS = (('Aac','All A are C'),('Iac','Some A are C'),('Eac','No A are C'),('Oac','Some A are not C'),('Aca','All C are A'),('Ica','Some C are A'),('Eca','No C are A'),('Oca','Some C are not A'),('NVC','No valid conclusion'))
        nr_code = models.CharField(max_length=2, null=False)
        order_nr = models.CharField(max_length=2, null=False)
        answer = models.CharField(max_length=3, choices=ANSWER_OPTIONS, null=True, blank=True)
        #starttime = models.CharField(max_length=8, null=True)
        endtime = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
        subject = models.ForeignKey(Subject)

        def __unicode__(self):
                return "Subject" + str(self.subject.name) + "Q" + self.nr_code
        def __str__(self):
                #return self.nr_code
                return "Subject" + str(self.subject.name) + "Q" + self.nr_code
