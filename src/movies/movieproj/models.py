from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.name
    #def was_published_recently(self):
    #    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
		
class List(models.Model):
    User = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    #votes = models.IntegerField()
    def __unicode__(self):
        return self.name