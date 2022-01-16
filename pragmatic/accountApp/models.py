from django.db import models

# Create your models here.

# $ python manage.py makemigrations
# 모델스 파이에다 쓰는 내용을 DB와 연동시킬 파이썬 파일로 만들어주는 작업

class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)
