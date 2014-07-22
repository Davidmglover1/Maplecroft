from adaptor.model import CsvModel
# from django.db import models
from adaptor.fields import CharField, FloatField

class MyCsvModel(CsvModel):
	country = CharField()
	code = CharField()
	lng = FloatField()
	lat = FloatField()
	
	class Meta:
		delimiter = ','
		has_header = True