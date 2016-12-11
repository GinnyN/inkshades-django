from django.contrib import admin
from front import models
from django_summernote.admin import SummernoteModelAdmin

class ModelAdmin(SummernoteModelAdmin): 
    pass

admin.site.register(models.Author, ModelAdmin)
admin.site.register(models.Setting, ModelAdmin)
admin.site.register(models.Publicity, ModelAdmin)
admin.site.register(models.Afiliate, ModelAdmin)
admin.site.register(models.Post, ModelAdmin)
admin.site.register(models.TagObra, ModelAdmin)
admin.site.register(models.Obra, ModelAdmin)
admin.site.register(models.Chapter, ModelAdmin)
admin.site.register(models.Productos, ModelAdmin)
admin.site.register(models.LinkObra, ModelAdmin)
admin.site.register(models.LinkAuthor, ModelAdmin)
admin.site.register(models.Image, ModelAdmin)
admin.site.register(models.PtoVenta, ModelAdmin)