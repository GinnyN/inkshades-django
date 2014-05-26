from django import template
from front import models

register = template.Library()

def rightColumn():
	settings = models.Setting.objects.get(pk=1)
	publicity = models.Publicity.objects.all().order_by('?')[:1].get()
	affiliates = models.Afiliate.objects.all()
	return {'settings': settings,'publicity': publicity,'afiliates':affiliates}

register.inclusion_tag('right_column.html')(rightColumn)