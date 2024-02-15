import datetime
import re

from django.db import models


# Create your models here.

class Asarlar(models.Model):
    b_cat = models.ForeignKey("B_category", null=True, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    asar_all_text = models.TextField()
    created_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        sentence_endings = r"[ \n]"
        matnlist = re.split(sentence_endings, self.asar_all_text)
        for i in matnlist:
            try:
                Bayt_parse.objects.create(word=i, b_category=self.b_cat)
            except Exception as e:
                print(str(e))
                pass
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.b_cat.name}-{str(datetime.datetime.now())}"


class A_category(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.name


class B_category(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    a_category = models.ForeignKey(A_category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Bayt_parse(models.Model):
    word = models.CharField(max_length=100)
    mano = models.CharField(max_length=255, null=True, blank=True)
    b_category = models.ForeignKey(B_category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word


class Nasriy_bayon(models.Model):
    text = models.CharField(max_length=100)
    b_category = models.ForeignKey(B_category, on_delete=models.CASCADE)
    bayt = models.ForeignKey(Bayt_parse, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class N_kirib_kelgan(models.Model):
    til_turi_name = models.CharField(max_length=100)

    def __str__(self):
        return self.til_turi_name


class N_lugat(models.Model):
    word = models.CharField(max_length=100)
    kirib_kelgan = models.ForeignKey(N_kirib_kelgan, on_delete=models.CASCADE)
    izohlar = models.TextField()

    def __str__(self):
        return self.word


