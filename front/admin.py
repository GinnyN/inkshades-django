from django.contrib import admin
from front import models
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
	pass
admin.site.register(models.Author)
admin.site.register(models.Setting)
admin.site.register(models.Publicity)
admin.site.register(models.Afiliate)
admin.site.register(models.Post,PostAdmin)
admin.site.register(models.TagObra)
admin.site.register(models.Obra,PostAdmin)
admin.site.register(models.Chapter,PostAdmin)
admin.site.register(models.Productos,PostAdmin)
admin.site.register(models.LinkObra)
admin.site.register(models.LinkAuthor)
admin.site.register(models.Image)
admin.site.register(models.PtoVenta)