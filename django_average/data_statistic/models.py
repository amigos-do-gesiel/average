import json
import xml
from django.db import models

from ..statistic_time.models import StatisticTime 

class DataFormatStatistic(models.Model):

    statistic_time = models.ForeignKey(StatisticTime)

    class Meta:
        abstract = True

    def convert_data_statistic(self):
        raise NotImplementedError("This funtion is not implemented")

    def create_object_data(self):
        raise NotImplementedError("This funtion is not implemented")

    def aplication_recomendations(self):
        raise NotImplementedError("This funtion is not implemented")

    def convert_data(self):
        self.convert_data_statistic()
        self.create_object_data()
        self.aplication_recomendations()


class DataJson(DataFormatStatistic):
    jsonField = models.TextField()
    
    class Meta:
        abstract = True

    def convert_data_statistic(self):
        pass
    
    def create_object_data(self):
        pass

    def aplication_recomendations(self):
        pass

class DataXml(DataFormatStatistic):

    class Meta:
        abstract = True

    def convert_data_statistic(self):
        pass

    def create_object_data(self):
        pass

    def aplication_recomendations(self):
        pass
