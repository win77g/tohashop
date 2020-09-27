from django.contrib import admin
from .models import *
# Register your models here.

class BrendAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Brend._meta.fields]
      class Meta:
           model = Brend
      def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('name',)
        }
admin.site.register(Brend, BrendAdmin)

# class CategoryAdmin (admin.ModelAdmin):
#    #  вывод всех полей в админку
#       list_display = [field.name for field in Category._meta.fields]
#       class Meta:
#            model = Category

# admin.site.register(Category, CategoryAdmin)

class PodcategAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Podcateg._meta.fields]
      class Meta:
           model = Podcateg
      def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('name',)
        }
admin.site.register(Podcateg, PodcategAdmin)

class HeightAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Height._meta.fields]
      class Meta:
           model = Height

admin.site.register(Height, HeightAdmin)

class DepthAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Depth._meta.fields]
      class Meta:
           model = Depth

admin.site.register(Depth, DepthAdmin)

class WidthAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Width._meta.fields]
      class Meta:
           model = Width

admin.site.register(Width, WidthAdmin)

class SeriaAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Seria._meta.fields]
      class Meta:
           model = Seria
      def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('name',)
        }
admin.site.register(Seria, SeriaAdmin)

# ----------------------------Gallery----------------------------------------------------------
#добавление фоток внизу прдукт админки
class KuhniImageInline(admin.TabularInline):
    model = KuhniImage
    extra = 1
    list_display = ['image_img',]
    readonly_fields = ['image_img',]
# ---------------------------- end Gallery----------------------------------------------------------
class KuhniModelAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
   #    list_display = [field.name for field in Product._meta.fields]
   inlines = [KuhniImageInline,]
   list_display = ('name','brend','category','podcateg','image_img', 'price','photoMenu','is_active','new_product','top','slider')
   readonly_fields = ['image_img',]
   # verbose_name_plural = 'Main'
   search_fields = ["price","name","brend__name"]
   list_filter = ['podcateg','brend','is_active','new_product','top']
   # suit_form_tabs = (
   #      ('main', 'Main'),
   #      ('params', 'Params'),
   #      ('filters','Filters'),)
   # fieldsets = [('Main',{
   #                   'classes': ('suit-tab', 'suit-tab-main',),
   #                   'fields':[
   #         'name','brend','categ','attributes','description','description_short','image_img', 'price','is_active','new_product','top','slider'
   #                   ]
   #                       }
   #               )]
   list_per_page = 15

   # ------------


   # meta

   # inlines = (MetaTagInline,)

   # def formfield_for_manytomany(self, db_field, request=None, **kwargs):
   #      if db_field.name == 'membership':
   #          qs = kwargs.get('queryset', db_field.remote_field.model.objects)
   #          # Avoid a major performance hit resolving membership names which
   #          # triggers a content_type load:
   #          kwargs['queryset'] = qs.select_related('content_type')
   #      return super().formfield_for_manytomany(db_field, request=request, **kwargs)
   # fields = ['category', 'title', 'slug', 'metakey', 'metadesc', 'text_redactor', 'text_redactor_full', 'tag', 'timestamp', 'autor', 'image', 'image_img', 'body', 'likes', 'dislikes']

class Meta:
    model = KuhniModel
    def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('name',)
        }
# Register your models here.
admin.site.register(KuhniModel,KuhniModelAdmin)
