from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from ..observer.models import ObserverStatistic
import datetime

class StatisticTime(models.Model):

    class Meta:
        abstract = True

    def get_statistic(self):
        pass

    def add_statisc_time(self):
        pass

    def remove_statistic_time(self):
        pass

class StatisticYearly(StatisticTime):
    year_number = models.IntegerField(unique=True) 
    MONTH_TOTAL = models.IntegerField
    yearly_value = models.FloatField(default=0.0)

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
    monthly_value = models.FloatField(default=0.0)
    year = models.ForeignKey(StatisticYearly, blank=True, null=True,default=None)
    month = models.IntegerField() 

    def start(self,search_year):
        if self.year is None:
            try:
                self.year = StatisticYearly.objects.get(year_number=search_year)
            except ObjectDoesNotExist:
                self.year = StatisticYearly(year_number = search_year)
                self.year.save()

    def add_statistic_time(self, daily_stat):
        daily_stat.stats_month = self
        self.update(daily_stat.daily_value)

    def remove_statistic_time(self, daily_stat):
        daily_stat.stats_month = None
        self.statistic_month -= daily_stat.daily_value

    def get_statistic(self):
        return self.monthly_dontations

    def return_days(self):
       StatisticDaily.objects.filter(month==self) 

class StatisticDaily(StatisticTime, ObserverStatistic):
    daily_donations = models.FloatField(default = 0.0)
    donation_date = models.DateField(auto_now=True)
    month = models.ForeignKey(StatisticMonthly, blank=True, null=True, default = None)

    def start(self):
        if self.month is None:
            try:
                self.month = StatisticMonthly.objects.get(month=self.donation_date.month,
                                                              year=StatisticYearly.objects.get(year_number=self.donation_date.year))
            except ObjectDoesNotExist:
                self.month = StatisticMonthly(month=self.donation_date.month)
                self.month.start(self.donation_date.year)
                self.month.save()
    
    def update(self, donation_value):
        self.daily_donations += donation_value

    def add_statistic_time(self):
        raise ValueError("You can't add a class to this object")

    def remove_statistic_time(self):
        raise ValueError("There is no objects in this instance")

    def get_statistic(self):
        return self.daily_donations
