from django.db import models




class Klass(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name





class Teacher(models.Model):
    full_name = models.CharField(max_length=50, unique=True)
    about_teacher = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    classes = models.ManyToManyField(Klass, related_name='teachers')

    def __str__(self) -> str:
        return self.full_name




class Student(models.Model):
    toliq_name = models.CharField(max_length=50, unique=True)
    phone_num = models.DecimalField(max_digits=13, decimal_places=0, unique=True)
    telegram_link = models.CharField(max_length=41, unique=True)
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE, related_name='students')

    def __str__(self) -> str:
        return self.toliq_name