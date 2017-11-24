from django.db import models
from ..observer.models import ObserverStatistic
import datetime

class StatisticTime(ObserverStatistic):

    class Meta:
        abstract = True

    def calculate_statistic(self):
        pass

    def get_statistic(self):
        pass

    def add_statisc_time(self):
        pass

    def remove_statistic_time(self):
        pass    

class StatisticDaily(StatisticTime):
    statistic_day = models.FloatField()
    donation_date = models.DateField(auto_now=True)

    def get_statistic(self):
        return self.statistic_day

    def update(self, donation_value):
        self.statistic_day += donation_value

    def calculate_statistic(self):
        pass

    def add_statisc_time(self):
        raise ValueError("You can't add a class to this object")

    def remove_statistic_time(self):
        raise ValueError("There is no objects in this instance")
