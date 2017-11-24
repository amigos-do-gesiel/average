from django.db import models
from ..observer.models import ObserverStatistic
import datetime

class StatisticTime(ObserverStatistic):

    class Meta:
        abstract = True

    def get_statistic(self):
        pass

    def add_statisc_time(self):
        pass

    def remove_statistic_time(self):
        pass

class StatisticYearly(StatisticTime):
    MONTH_TOTAL = models.IntegerField
    yearly_value = models.FloatField()

    def update(self, daily_value):
        self.statistic_year += daily_value

    def add_statistic_time(self, monthly_stat):
        monthly_stat.stats_year = self
        self.update(monthly_stat.monthly_value)

    def remove_statistic_time(self, monthly_stat):
        monthly_stat.stats_year = None
        self.statistic_year -= monthly_stat.monthly_value

    def get_statistic(self):
        return self.yearly_value

class StatisticMonthly(StatisticTime):
    # monthly_dontations = models.ForeignKey(StatisticDaily)
    DAY_TOTAL = models.IntegerField() #number of days this month has
    monthly_value = models.FloatField()
    stats_year = models.ForeignKey(StatisticYearly, blank=True, null=True)

    def update(self, daily_value):
        self.statistic_month += daily_value

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
    stats_month = models.ForeignKey(StatisticMonthly, blank=True, null=True)

    def update(self, donation_value):
        self.daily_donations += donation_value


    def add_statistic_time(self):
        raise ValueError("You can't add a class to this object")

    def remove_statistic_time(self):
        raise ValueError("There is no objects in this instance")

    def get_statistic(self):
        return self.daily_donations
