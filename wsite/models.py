from django.db import models


class About(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.title


class Banner(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.title


