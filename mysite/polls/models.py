from django.db import models


# Create your models here.
class CreatorOneToOne(models.Model):
    creator_text = models.CharField(max_length=100)


class CreationOneToOne(models.Model):
    creator_text = models.CharField(max_length=100)
    creator = models.OneToOneField(CreatorOneToOne, on_delete=models.CASCADE)


class OTMCreator(models.Model):
    creator_text = models.CharField(max_length=100)


class MTOCreation(models.Model):
    otm_Creator = models.ForeignKey(OTMCreator, on_delete=models.CASCADE)
    creator_text = models.CharField(max_length=100)


class MTMCreator(models.Model):
    creator_text = models.CharField(max_length=100)


class MTMCreation(models.Model):
    mtm_creator = models.ManyToManyField(MTMCreator)
    creation_text = models.CharField(max_length=100)
