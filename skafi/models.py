from django.db import models
from django.db.models.signals import  pre_save
# преврашает в slug
from django.utils.text import slugify
# переводит кирилицу в латынь
from transliterate import translit
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
    name = models.CharField(max_length=120,blank=True, null=True, default=None,unique=True,verbose_name='Высота шкафа')
    # вывод одного поля
    def __str__(self):
        return " %s" % self.name
    class Meta:
        verbose_name = 'Высота шкафа'
        verbose_name_plural = 'Высота шкафа'
class Height_penal(models.Model):
    name = models.CharField(max_length=120,blank=True, null=True, default=None,unique=True,verbose_name='Высота пенала')
    # вывод одного поля
    def __str__(self):
        return " %s" % self.name
    class Meta:
        verbose_name = 'Высота пенала'
        verbose_name_plural = 'Высота пенала'        
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
    name = models.CharField(max_length=120,blank=True, null=True, default=None,unique=True,verbose_name='Ширина шкафа')
    # вывод одного поля
    def __str__(self):
        return " %s" % self.name
    class Meta:
        verbose_name = 'Ширина шкафа'
        verbose_name_plural = 'Ширина шкафа'
# ширина
class Width_penal(models.Model):
    name = models.CharField(max_length=120,blank=True, null=True, default=None,unique=True,verbose_name='Ширина_пенала')
    # вывод одного поля
    def __str__(self):
        return " %s" % self.name
    class Meta:
        verbose_name = 'Ширина пенала'
        verbose_name_plural = 'Ширина пенала'        
# ширина
class Podcateg(models.Model):
    name = models.CharField(verbose_name='Название',max_length=120,blank=True, null=True ,unique=True)
    slug = models.SlugField(verbose_name='Транслит', null = True, unique=True,)
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
class SkafModel(models.Model):
    name = models.CharField(verbose_name='Название',max_length=120,blank=True, null=True ,unique=True)
    podcateg = models.ForeignKey(Podcateg, blank=True, null=True,related_name = 'cat',on_delete=models.CASCADE,verbose_name='Подкатегория',to_field='slug')
    brend = models.ForeignKey(Brend,blank=True, null=True, default=None,on_delete=models.CASCADE,verbose_name='Бренд',to_field='name')
    image_1 = models.ImageField(upload_to=image_folder, blank=True, null=True, default=None,verbose_name='Фотка1')
    image_2 = models.ImageField(upload_to=image_folder, blank=True, null=True, default=None,verbose_name='Фотка2')
    slug = models.SlugField(blank=True, null=True, default=None,verbose_name='Транслит(Не трогать)')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name='Цена шкафа')
    price_shelf_1 = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name='Цена пенала 0,450мм')
    price_shelf_2 = models.DecimalField(max_digits=10, decimal_places=2, default=0,verbose_name='Цена пенала 0,600мм')
    height = models.ForeignKey(Height,blank=True, null=True, default=None,on_delete=models.CASCADE,verbose_name='Высота шкафа',to_field='name')
    height_penal = models.ForeignKey(Height_penal,blank=True, null=True, default=None,on_delete=models.CASCADE,verbose_name='Высота пенала',to_field='name')
    depth = models.ForeignKey(Depth,blank=True, null=True, default=None,on_delete=models.CASCADE,verbose_name='Глубина шкафа',to_field='name')
    width = models.ForeignKey(Width,blank=True, null=True, default=None,on_delete=models.CASCADE,verbose_name='Ширина шкафа',to_field='name')
    width_penal = models.ForeignKey(Width_penal,blank=True, null=True, default=None,on_delete=models.CASCADE,verbose_name='Ширина пенала',to_field='name')
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
pre_save.connect(pre_save_product_slug, sender=SkafModel)
# -----------------------------end product-------------------------------------------------------------
#  --------------------------Gallery-------------------------------------------------------
# создание названия фотки
def image_gallary_folder(instance,filename):
    filename = instance.slug +'.'+filename.split('.')[1]
    return "{0}/{1}".format(instance.slug,filename)
# фотки продукта
class SkafImage(models.Model):
    product = models.ForeignKey(SkafModel,blank=True, null=True, default=None,on_delete=models.CASCADE)
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
pre_save.connect(pre_save_imagegallery_slug, sender=SkafImage)
# ---------------------------------------end gallery----------------------------------
