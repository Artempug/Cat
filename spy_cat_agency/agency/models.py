from django.db import models

class SpyCat(models.Model):
    name = models.CharField(max_length=100)  #Name of the spy cat
    years_of_experience = models.PositiveIntegerField()  #Years of experience
    breed = models.CharField(max_length=100)  #Breed of the cat
    salary = models.DecimalField(max_digits=10, decimal_places=2)  #Salary of the cat

    def __str__(self):
        return self.name

class Mission(models.Model):
    spy_cat = models.OneToOneField(SpyCat, on_delete=models.SET_NULL, null=True, blank=True)  #Assigned spy cat
    is_complete = models.BooleanField(default=False)  #Mission completion status

    def __str__(self):
        return f"Mission {self.id} for {self.spy_cat}"

class Target(models.Model):
    mission = models.ForeignKey(Mission, related_name='targets', on_delete=models.CASCADE)  #Associated mission
    name = models.CharField(max_length=100)  #Targets name
    country = models.CharField(max_length=100)  #Country of the target
    notes = models.TextField(blank=True)  #Notes collected
    is_complete = models.BooleanField(default=False)  #Target completion status

    def __str__(self):
        return self.name
