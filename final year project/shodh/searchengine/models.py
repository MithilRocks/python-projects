from django.db import models

class url_list(models.Model):
	url_id=models.IntegerField()			#Specifies unique Id for that url. Should be incremented by 1 for a new url
	url_name=models.CharField(max_length=200)       #Name of the url
	url_title=models.CharField(max_length=200)
	url_text=models.TextField()
	def __unicode__(self):
		return self.url_name                    #Returns name of the url
   
class link(models.Model):
	         #Foreign key that adds 'url_list' model in this model so as to access the urls. 
                                                        #Is stored as the column name 'url_list_id' in the database.  
	from_id=models.IntegerField()                   #Id of parent url of which it is a child
        to_id=models.IntegerField()                     #Id of child url of this url
	

class word_list(models.Model):
	url_id=models.IntegerField()			
	url_name=models.CharField(max_length=200)          
                                                        #Is stored as the column name 'url_list_id' in the database.
	word=models.CharField(max_length=50)            #Specifies a word that occurs in the webpage corresponding to the url
	title=models.IntegerField()                     #1-if word is present in title field of webpage 0-otherwise
	header=models.IntegerField()                    #1-if word is present in header field of webpage 0-otherwise
	anchor=models.IntegerField()               #1-if word is present in anchor field of webpage 0-otherwise
	no_of_occur=models.IntegerField()           #if title, header and achor text fields are 0, no. of occurences of that word in 
                                                        #that webpage is stored here
	def __unicode__(self):
		return self.url_name           #Returns name of the url

class query_score(models.Model):
	query=models.CharField(max_length=100)
	score=models.IntegerField()
# Create your models here.
