from django.db import models

class DataFormatStatistic(models.Model):

    class Meta:
        abstract = True

    def convert_data_statistic(self, data):
        raise NotImplementedError("This funtion is not implemented")

    def create_object_data(self, data):
        raise NotImplementedError("This funtion is not implemented")

    def aplication_recomendations(self, data):
        raise NotImplementedError("This funtion is not implemented")

    def convert_data(self, data):
        self.convert_data_statistic(data)
        self.create_object_data(data)
        self.aplication_recomendations(data)


class DataJson(DataFormatStatistic):

    class Meta:
        abstract = True

    def convert_data_statistic():
        pass

    def create_object_data():
        pass

    def aplication_recomendations():
        pass

class DataXml(DataFormatStatistic):

    class Meta:
        abstract = True

    def convert_data_statistic():
        pass

    def create_object_data():
        pass

    def aplication_recomendations():
        pass
