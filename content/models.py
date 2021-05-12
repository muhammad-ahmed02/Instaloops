from django.db import models
from django.contrib.auth.models import User


class Niche(models.Model):
    name = models.CharField(max_length=56)

    def __str__(self):
        return self.name


class Influencer(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    min_budget = models.PositiveIntegerField(default=0)
    max_budget = models.PositiveIntegerField()
    niche = models.ForeignKey(to=Niche, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to="Influencer/Pic/", blank=True, null=True)
    banner = models.ImageField(upload_to="Influencer/Banner/", blank=True, null=True)
    bio = models.CharField(max_length=64, blank=True, null=True)
    about = models.TextField()
    rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username

    def reviews(self):
        return Review.objects.filter(influencer__pk=self.pk)

    def review_count(self):
        return Review.objects.filter(influencer__pk=self.pk).count()


class Consumer(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to="Consumer/pic/", blank=True, null=True)


class Review(models.Model):
    consumer = models.ForeignKey(
        to=Consumer, on_delete=models.CASCADE, blank=True, null=True
    )
    influencer = models.ForeignKey(to=Influencer, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title


def getIncreasingBannerOrder():
    return Banner.objects.all().count()


class Banner(models.Model):
    image = models.ImageField(upload_to="Site/Banners/")
    link = models.URLField(blank=True, null=True)
    order_no = models.PositiveIntegerField(default=getIncreasingBannerOrder)


class Order(models.Model):
    influencer = models.ForeignKey(to=Influencer, on_delete=models.CASCADE)
    consumer = models.ForeignKey(to=Consumer, on_delete=models.CASCADE)
    accepted_amount = models.FloatField()
    date_created = models.DateTimeField(auto_created=True)
    is_accepted = models.BooleanField(default=False)
    has_responded = models.BooleanField(default=False)
