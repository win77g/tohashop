from django.db import models
from django.db.models.signals import  pre_save
# преврашает в slug
from django.utils.text import slugify
# переводит кирилицу в латынь
from transliterate import translit
from product.models import Category
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe

class Brend(models.Model):
    name = models.CharField(max_length=120,blank=True, null=True, default=None,unique=True,)
    slug = models.SlugField(blank=True, null=True, default=None ,verbose_name='Транслит')
    # вывод одного поля
    def __str__(self):
        return " %s" % self.name
    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренд'
# автоматическое сохранение поля слаг в бренд
def pre_save_brend_slug(sender,instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(instance.name, reversed=True))
        instance.slug = slug
pre_save.connect(pre_save_brend_slug, sender=Brend)
# высота
class Height(models.Model):
    name = models.CharField(max_length=120,blank=True, null=True, default=None,unique=True,verbose_name='Высота')
    # вывод одного поля
    def __str__(self):
        return " %s" % self.name
    class Meta:
        verbose_name = 'Высота'
        verbose_name_plural = 'Высота'
# глубина
class Depth(models.Model):
    name = models.CharField(max_length=120,blank=True, null=True, default=None,unique=True,verbose_name='Глубина')
    # вывод одного поля
    def __str__(self):
        return " %s" % self.name
    class Meta:
        verbose_name = 'Глубина'
        verbose_name_plural = 'Глубина'
# ширина
class Width(models.Model):
    name = models.CharField(max_length=120,blank=True, null=True, default=None,unique=True,verbose_name='Ширина')
    # вывод одного поля
    def __str__(self):
        return " %s" % self.name
    class Meta:
        verbose_name = 'Ширина'
        verbose_name_plural = 'Ширина'
# ширина
# class Category(models.Model):
#     name = models.CharField(verbose_name='Название',max_length=120,blank=True, null=True ,unique=True)
#     slug = models.SlugField(verbose_name='Транслит', null = True, unique=True,)
#     # вывод одного поля
#     def __str__(self):
#         return " %s" % self.name
#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категория'

class Podcateg(models.Model):
    name = models.CharField(verbose_name='Название',max_length=120,blank=True, null=True ,unique=True)
    slug = models.SlugField(verbose_name='Транслит', null = True, unique=True,)
    description = RichTextUploadingField(verbose_name='Описание',max_length=120,blank=True, null=True ,unique=True)
    meta_k = models.CharField(verbose_name='Ключевые слова',max_length=120,blank=True, null=True ,unique=True)
    meta_d = RichTextUploadingField(verbose_name='Мета описание',max_length=120,blank=True, null=True ,unique=True)

    # вывод одного поля
    def __str__(self):
        return " %s" % self.name
    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегория'
# ---------------------------------Product---------------------------------------------------
# создание названия фотки
def image_folder(instance,filename):
    filename = instance.slug +'.'+filename.split('.')[1]
    return "{0}/{1}".format(instance.slug,filename)


# модеь продукта
class SpalniModel(models.Model):
    name = models.CharField(verbose_name='Название',max_length=120,blank=True, null=True ,unique=True)
    keyword = models.CharField(verbose_name='Ключи',max_length=120,blank=True, null=True ,unique=True)
    category = models.ForeignKey(Category, blank=True, null=True,on_delete=models.CASCADE,verbose_name='Категория',to_field='slug')
    podcateg = models.ForeignKey(Podcateg, blank=True, null=True,on_delete=models.CASCADE,verbose_name='Подкатегория',to_field='slug')
    brend = models.ForeignKey(Brend,blank=True, null=True, default=None,on_delete=models.CASCADE,verbose_name='Бренд',to_field='name')
    image_1 = models.ImageField(upload_to=image_folder, blank=True, null=True, default=None,verbose_name='Фотка1')
    image_2 = models.ImageField(upload_to=image_folder, blank=True, null=True, default=None,verbose_name='Фотка2')
    slug = models.SlugField(blank=True, null=True, default=None,verbose_name='Транслит(Не трогать)')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name='Цена')
    height = models.ForeignKey(Height,blank=True, null=True, default=None,on_delete=models.CASCADE,verbose_name='Высота',to_field='name')
    depth = models.ForeignKey(Depth,blank=True, null=True, default=None,on_delete=models.CASCADE,verbose_name='Глубина',to_field='name')
    width = models.ForeignKey(Width,blank=True, null=True, default=None,on_delete=models.CASCADE,verbose_name='Ширина',to_field='name')
    description = RichTextUploadingField(verbose_name='Текст',blank=True, null=True, default=None)
    description_short = RichTextUploadingField(verbose_name='Текст(короткий)',blank=True, null=True, default=None)
    discount = models.IntegerField(default=0,verbose_name='Скидка')
    is_active = models.BooleanField(default=True,verbose_name='В наличии')
    new_product = models.BooleanField(default=False,verbose_name='Новинка')
    top = models.BooleanField(default=False,verbose_name='В топе(на гл.странице)')
    photoMenu = models.BooleanField(default=False,verbose_name='Фото в меню')
    slider = models.BooleanField(default=False,verbose_name='Слайдер(на гл.странице)')
    comments = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True,auto_now=False,verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now_add=False,auto_now=True,verbose_name='Дата последнего обновления')
    # вывод одного поля
    def __str__(self):
        return " %s" % self.name
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


    def image_img(self):
        if self.image_1:
            return mark_safe(u'<a href="{0}"target="_blank"><img src="{0}" width="100"/></a>'.format(self.image_1.url))
        else:
            return '(Нет изображения)'
    image_img.short_description = 'Картинка'
    image_img.allow_tags = True
# удаление фото

# автоматическое сохранение поля слаг в продуктах
def pre_save_product_slug(sender,instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(instance.name, reversed=True))
        instance.slug = slug
pre_save.connect(pre_save_product_slug, sender=SpalniModel)
# -----------------------------end product-------------------------------------------------------------
#  --------------------------Gallery-------------------------------------------------------
# создание названия фотки
def image_gallary_folder(instance,filename):
    filename = instance.slug +'.'+filename.split('.')[1]
    return "{0}/{1}".format(instance.slug,filename)
# фотки продукта
class SpalniImage(models.Model):
    product = models.ForeignKey(SpalniModel,blank=True, null=True, default=None,on_delete=models.CASCADE)
    image = models.ImageField(upload_to= image_gallary_folder,blank=True, null=True, default=None)
    slug = models.SlugField(blank=True, null=True, default=None , verbose_name='Транслит')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    def image_img(self):
        if self.image:
            return mark_safe(u'<a href="{0}"target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'
    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

# автоматическое сохранение поля слаг в gallery
def pre_save_imagegallery_slug(sender,instance, *args, **kwargs):
    # print(instance.filename)
    if not instance.slug:
        slug = slugify(translit(instance.product.name, reversed=True))
        instance.slug = slug
pre_save.connect(pre_save_imagegallery_slug, sender=SpalniImage)
# ---------------------------------------end gallery----------------------------------
# Create your models here.

