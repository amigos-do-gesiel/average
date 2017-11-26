import json
import xml
from django.db import models
from polymorphic.model import PolymorphicModel
from django.core import serializers
from ..statistic_time.models import StatisticTime

class DataFormatStatistic(PolymorphicModel):

    statistic_time = models.ForeignKey(StatisticTime)

    class Meta:
        abstract = True

    def convert_data(self, stats):
        raise NotImplementedError ("You can't convert using this class")


class DataJson(DataFormatStatistic):

    def convert_data(self, stats):
        data = serializers.serialize("json", stats)
        return data

class DataXml(DataFormatStatistic):

    def convert_data(self, stats):
        data = serializers.serialize("xml", stats)
        return data
