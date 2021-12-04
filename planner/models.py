from django.db import models



class Plans(models.Model):
    workout_choices=(
        ('aerobics','aerobics'),
        ('Group classes','Group classes'),
        ('personal trainer','personal trainer'),
        
    )
   

    workout=models.CharField(max_length=200,choices=workout_choices)
    description=models.CharField(max_length=200)
    days=models.CharField(max_length=200,null=True)
    time=models.CharField(max_length=200)
    complete=models.BooleanField(default=False)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.workout)
    

class book(models.Model):
    
    days=(
        ('Mon','Mon'),
        ('Tue','Tue'),
        ('Wed','Wed'),
        ('Thur','Thur'),
        ('Fri','Fri')
    
    ) 
    workout_choices=(
        ('aerobics','aerobics'),
        ('Group class','Group class'),
        ('personal trainer','personal trainer'),
        ('solo training','solo training')
    )
    day=models.CharField(max_length=200,choices=days)
    name=models.CharField(max_length=200)
    workout=models.CharField(max_length=200,choices=workout_choices)
    time=models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.name)+(self.time)
    class Meta:
        ordering=['time']



