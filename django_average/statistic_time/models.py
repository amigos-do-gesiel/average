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

class StatisticMonthly(StatisticTime):
    # monthly_dontations = models.ForeignKey(StatisticDaily)
    DAY_TOTAL = models.IntegerField() #number of days this month has
    statistic_month = models.FloatField()
    #stats_year = models.ForeignKey(StatisticYearly)

    def update(self, daily_value):
        self.statistic_month += daily_value

    def calculate_statistic(self):
        pass

    def add_statistic_time(self, daily_stat):
        daily_stat.stats_month = self
        self.update(daily_stat.daily_value)

    def remove_statistic_time(self, daily_stat):
        daily_stat.stats_month = None
        self.statistic_month -= daily_stat.daily_value

    def get_statistic(self):
        return self.monthly_dontations

class StatisticDaily(StatisticTime):
    daily_donations = models.FloatField()
    donation_date = models.DateField(auto_now=True)
    stats_month = models.ForeignKey(StatisticMonthly)

    def update(self, donation_value):
        self.daily_donations += donation_value

    def calculate_statistic(self):
        pass

    def add_statistic_time(self):
        raise ValueError("You can't add a class to this object")

    def remove_statistic_time(self):
        raise ValueError("There is no objects in this instance")

    def get_statistic(self):
        return self.daily_donations
