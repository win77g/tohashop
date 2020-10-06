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

class Height_penalAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Height_penal._meta.fields]
      class Meta:
           model = Height_penal

admin.site.register(Height_penal, Height_penalAdmin)

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

class Width_penalAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Width_penal._meta.fields]
      class Meta:
           model = Width_penal

admin.site.register(Width_penal, Width_penalAdmin)

# ----------------------------Gallery----------------------------------------------------------
#добавление фоток внизу прдукт админки
class SkafImageInline(admin.TabularInline):
    model = SkafImage
    extra = 1
    list_display = ['image_img',]
    readonly_fields = ['image_img',]
# ---------------------------- end Gallery----------------------------------------------------------
class SkafModelAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
   #    list_display = [field.name for field in Product._meta.fields]
   inlines = [SkafImageInline,]
   list_display = ('name','brend','podcateg','image_img','price_g450_st','price_g450_od','price_g600_st','price_g600_od','price_shelf_1','price_shelf_2','is_active','top')
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
    model = SkafModel
    def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('name',)
        }
# Register your models here.
admin.site.register(SkafModel,SkafModelAdmin)
