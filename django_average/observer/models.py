from django.db import models

# Create your models here.

class ObserverStatistic(models.Model):
    class Meta:
        abstract = True

    def update(self, donation_value):
        pass

class ObservableStatisctic(models.Model):
    class Meta:
        abstract = True

    def add_observers():
        pass

    def remove_observers():
        pass
    
    def notify_observers():
        pass
