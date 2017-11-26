import json
import dicttoxml
from django.db import models
from polymorphic.models import PolymorphicModel
from django.core import serializers
from ..statistic_time.models import StatisticTime

class DataFormatStatistic(PolymorphicModel):

    class Meta:
        abstract = True

    def convert_data(self, stats):
        raise NotImplementedError ("You can't convert using this class")


class DataJson(DataFormatStatistic):

    def convert_data(self, stats):
        data = json.dumps(stats)
        return data

class DataXml(DataFormatStatistic):

    def convert_data(self, stats):
        data = dicttoxml.dicttoxml(stats)
        return data
