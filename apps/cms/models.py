from django.db import models

# Create your models here.

class PageSetting(models.Model):
    page_title = models.CharField(verbose_name="首页标题",max_length=32,default="STUCMS")
    ad_title = models.CharField(verbose_name="公众号标题",max_length=32,default="STUCMS")
    ad_image = models.CharField(verbose_name="公众号图片URL",max_length=999,default= "/static/images/stu.png")

