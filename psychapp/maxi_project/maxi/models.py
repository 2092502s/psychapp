from django.db import models


# Create your models here.
class Subject(models.Model):
	consent = models.BooleanField(default=False)
	name = models.IntegerField(null=True)
	#subject_nr = models.PositiveSmallIntegerField(unique=True)
	syllogism_order = models.CharField(max_length=500, null=False)
	#questions = models.ForeignKey(Question)
	#id = models.AutoField(primary_key=True)
	start_time = models.CharField(max_length=8, null=True)
	

	GENDERS = (('F', 'Female'),('M','Male'),('N', 'Not disclosed'))
	preq1 = models.CharField(max_length=1, choices=GENDERS, blank=True, null=True)
	preq2 = models.IntegerField(blank=True, null=True)
	DISCIPLINES = (('A', 'Arts & Humanities'), ('B','Computing & Engineering'), ('C','Social Sciences'),('D','Natural Sciences'),('E','Not at University'))
	preq3 = models.CharField(max_length=1, choices=DISCIPLINES, blank=True, null=True)
	FAMILIARITY = (('A','No familiarity at all'),('B','Vaguely familiar'),('C','Very familiar'))
	preq4 = models.CharField(max_length=1, choices=FAMILIARITY, blank=True, null=True)


	USE_OF_DIAGRAMS = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'))
	post1 = models.CharField(max_length=1, choices=USE_OF_DIAGRAMS, blank=True, null=True)
	FAMILIARITY2 = (('1','Not familiar'),('2','Vaguely familiar'),('3','Very familiar'))
	post2 = models.CharField(max_length=1, choices=FAMILIARITY2, blank=True, null=True)

	def __unicode__(self):
		return str(self.name)
		
	def __str__(self):
		return str(self.name)

class Question(models.Model):
        ANSWER_OPTIONS = (('A','All C are A'),('B','No C are A'),('C','Some C are A'),('D','Some C are not A'),('E','No valid conclusion'))
        nr_code = models.CharField(max_length=2, null=False)
        order_nr = models.CharField(max_length=2, null=False)
        answer = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
        #starttime = models.CharField(max_length=8, null=True)
        endtime = models.CharField(max_length=8, null=True)
        subject = models.ForeignKey(Subject)

        def __unicode__(self):
                return "Subject" + str(self.subject.name) + "Q" + nr_code
        def __str__(self):
                #return self.nr_code
                return "Subject" + str(self.subject.name) + "Q" + nr_code

##	ex1 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime1 = models.CharField(max_length=8, null=True)	
##	endtime1 = models.CharField(max_length=8, null=True)	
##
##	ex2 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime2 = models.CharField(max_length=8, null=True)
##	endtime2 = models.CharField(max_length=8, null=True)
##
##	ex3 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime3 = models.CharField(max_length=8, null=True)
##	endtime3 = models.CharField(max_length=8, null=True)
##
##	ex4 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime4 = models.CharField(max_length=8, null=True)
##	endtime4 = models.CharField(max_length=8, null=True)
##
##	ex5 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime5 = models.CharField(max_length=8, null=True)
##	endtime5 = models.CharField(max_length=8, null=True)
##
##	ex6 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime6 = models.CharField(max_length=8, null=True)	
##	endtime6 = models.CharField(max_length=8, null=True)	
##
##	ex7 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime7 = models.CharField(max_length=8, null=True)
##	endtime7 = models.CharField(max_length=8, null=True)
##
##	ex8 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime8 = models.CharField(max_length=8, null=True)
##	endtime8 = models.CharField(max_length=8, null=True)
##
##	ex9 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime9 = models.CharField(max_length=8, null=True)
##	endtime9 = models.CharField(max_length=8, null=True)
##
##	ex10 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime10 = models.CharField(max_length=8, null=True)
##	endtime10 = models.CharField(max_length=8, null=True)
##	
##	ex11 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime11 = models.CharField(max_length=8, null=True)	
##	endtime11 = models.CharField(max_length=8, null=True)	
##
##	ex12 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime12 = models.CharField(max_length=8, null=True)
##	endtime12 = models.CharField(max_length=8, null=True)
##
##	ex13 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime13 = models.CharField(max_length=8, null=True)
##	endtime13 = models.CharField(max_length=8, null=True)
##
##	ex14 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime14 = models.CharField(max_length=8, null=True)
##	endtime14 = models.CharField(max_length=8, null=True)
##
##	ex15 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime15 = models.CharField(max_length=8, null=True)
##	endtime15 = models.CharField(max_length=8, null=True)
##
##	ex16 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime16 = models.CharField(max_length=8, null=True)	
##	endtime16 = models.CharField(max_length=8, null=True)	
##
##	ex17 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime17 = models.CharField(max_length=8, null=True)
##	endtime17 = models.CharField(max_length=8, null=True)
##
##	ex18 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime18 = models.CharField(max_length=8, null=True)
##	endtime18 = models.CharField(max_length=8, null=True)
##
##	ex19 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime19 = models.CharField(max_length=8, null=True)
##	endtime19 = models.CharField(max_length=8, null=True)
##
##	ex20 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime20 = models.CharField(max_length=8, null=True)
##	endtime20 = models.CharField(max_length=8, null=True)
##	
##	ex21 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime21 = models.CharField(max_length=8, null=True)	
##	endtime21 = models.CharField(max_length=8, null=True)	
##
##	ex22 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime22 = models.CharField(max_length=8, null=True)
##	endtime22 = models.CharField(max_length=8, null=True)
##
##	ex23 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime23 = models.CharField(max_length=8, null=True)
##	endtime23 = models.CharField(max_length=8, null=True)
##
##	ex24 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime24 = models.CharField(max_length=8, null=True)
##	endtime24 = models.CharField(max_length=8, null=True)
##
##	ex25 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime25 = models.CharField(max_length=8, null=True)
##	endtime25 = models.CharField(max_length=8, null=True)
##	
##	ex26 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime26 = models.CharField(max_length=8, null=True)	
##	endtime26 = models.CharField(max_length=8, null=True)	
##
##	ex27 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime27 = models.CharField(max_length=8, null=True)
##	endtime27 = models.CharField(max_length=8, null=True)
##
##	ex28 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime28 = models.CharField(max_length=8, null=True)
##	endtime28 = models.CharField(max_length=8, null=True)
##
##	ex29 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime29 = models.CharField(max_length=8, null=True)
##	endtime29 = models.CharField(max_length=8, null=True)
##
##	ex30 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime30 = models.CharField(max_length=8, null=True)
##	endtime30 = models.CharField(max_length=8, null=True)
##	
##	ex31 = models.CharField(max_length=1, choices=ANSWER_OPTIONS, null=True, blank=True)
##	starttime31 = models.CharField(max_length=8, null=True)	
##	endtime31 = models.CharField(max_length=8, null=True)	


