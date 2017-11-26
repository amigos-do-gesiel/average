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

    def covert_data(self, data_format_statistic):
        pass

class StatisticYearly(StatisticTime):
    year_number = models.IntegerField(unique=True)
    MONTH_TOTAL = models.IntegerField
    yearly_value = models.FloatField(default=0.0)
    yearly_average = models.FloatField(default=0.0)

    def get_statistic(self):
        return self.yearly_value

    def update_yearly_value(self, donation_value):
        self.yearly_value += donation_value
        self.update_yearly_average()
        self.save()

    def convert_data(self, data_format_statistic):
        year_data = self.get_days()
        return data_format_statistic.convert_data(year_data)

    def get_days(self):
        days = {}
        year = StatisticMonthly.objects.filter(year=self.id)
        for month in year:
            days_month = month.get_days()
            for day in days_month:
                days[str(day)] = days_month[day]
        return days

    def get_months(self):
        months = StatisticMonthly.objects.filter(year=self)
        months_list = {}
        for month in months:
            months_list[str(month.month) + '/' + str(month.year.year_number)] = self.yearly_value
        return months_list

    def update_yearly_average(self):
        months = len(self.get_months())
        self.yearly_average = self.yearly_value/months

class StatisticMonthly(StatisticTime):
    # monthly_dontations = models.ForeignKey(StatisticDaily)
    monthly_value = models.FloatField(default=0.0)
    year = models.ForeignKey(StatisticYearly, blank=True, null=True,default=None)
    month = models.IntegerField()
    month_average = models.FloatField(default=0.0)

    def start(self,search_year):
        if self.year is None:
            try:
                new_year = StatisticYearly.objects.get(year_number=search_year)
                self.year = new_year
            except ObjectDoesNotExist:
                new_year = StatisticYearly(year_number=search_year)
                new_year.save()
                self.year = new_year
            self.save()

    def get_statistic(self):
        return self.monthly_dontations

    def update_monthly_value(self, donation_value):
        self.monthly_value += donation_value
        self.year.update_yearly_value(donation_value)
        self.update_month_average()
        self.save()

    def get_days(self):
        days = StatisticDaily.objects.filter(month=self.id)
        days_list = {}
        for day in days:
            days_list[str(day.donation_date.day) + '/' + str(day.donation_date.month) + '/' + str(day.donation_date.year)] = day.daily_donations
        return days_list

    def get_month_avarege(self):
        days = len(self.get_days())
        return self.monthly_value/days

    def convert_data(self, data_format_statistic):
        data = self.get_days()
        #data.append(self)
        #data.append(self.get_days())
        return data_format_statistic.convert_data(data)

    def update_month_average(self):
        days = len(self.get_days())
        self.month_average = self.monthly_value/days

class StatisticDaily(StatisticTime, ObserverStatistic):
    daily_donations = models.FloatField(default = 0.0)
    donation_date = models.DateField(auto_now=True)
    month = models.ForeignKey(StatisticMonthly, blank=True, null=True, default = None)

    def start(self):
        if self.month is None:
            try:
                new_month = StatisticMonthly.objects.get(month=self.donation_date.month,
                                                              year=StatisticYearly.objects.get(year_number=self.donation_date.year))
                self.month = new_month
            except ObjectDoesNotExist:
                new_month = StatisticMonthly(month=self.donation_date.month)
                new_month.save()
                self.month = new_month
                self.month.start(self.donation_date.year)
            # self.month.save()
        # suspect code : super(StatisticDaily, self).save()
        self.save()

    def update(self, donation_value):
        self.daily_donations += donation_value
        self.month.update_monthly_value(donation_value)
        self.save()


    def add_statistic_time(self):
        raise ValueError("You can't add a class to this object")

    def remove_statistic_time(self):
        raise ValueError("There is no objects in this instance")

    def get_statistic(self):
        return self.daily_donations

    def convert_data(self, data_format_statistic):
        pass