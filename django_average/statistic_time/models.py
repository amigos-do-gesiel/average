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

    def get_statistic(self):
        return self.yearly_value

    def update_yearly_value(self, donation_value):
        self.yearly_value += donation_value
        super(StatisticYearly, self).save()

    def covert_data(self, data_format_statistic):
        data_format_statistic.convert_data(self.get_days)

    def get_days(self):
        days = []
        year = StatisticMonthly.objects.filter(year=self.id)
        for month in year:
            days_month = month.get_days()
            for day in days_month:
                days.append(day)
        return days


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
            # suspect code : super(StatisticMonthly, self).save()
            self.save()

    def get_statistic(self):
        return self.monthly_dontations

    def update_monthly_value(self, donation_value):
        self.monthly_value += donation_value
        self.year.update_yearly_value(donation_value)
        super(StatisticMonthly, self).save()

    def get_days(self):
        return StatisticDaily.objects.filter(month=self.id)


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
        # suspect code : super(StatisticDaily, self).save()
        self.save()

    def update(self, donation_value):
        self.daily_donations += donation_value
        self.month.update_monthly_value(donation_value)
        super(StatisticDaily, self).save()


    def add_statistic_time(self):
        raise ValueError("You can't add a class to this object")

    def remove_statistic_time(self):
        raise ValueError("There is no objects in this instance")

    def get_statistic(self):
        return self.daily_donations
