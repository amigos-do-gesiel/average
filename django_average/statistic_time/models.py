from django.db import models
from ..observer import Observer


class StatisticTime(Observer):

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
