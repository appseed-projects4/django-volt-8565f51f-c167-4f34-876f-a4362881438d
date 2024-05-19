# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Account(models.Model):

    #__Account_FIELDS__
    guildid = models.CharField(max_length=255, null=True, blank=True)
    userid = models.CharField(max_length=255, null=True, blank=True)
    channelid = models.CharField(max_length=255, null=True, blank=True)
    tittle = models.CharField(max_length=255, null=True, blank=True)
    laststatus = models.CharField(max_length=255, null=True, blank=True)
    ssocookie = models.CharField(max_length=255, null=True, blank=True)
    created = models.CharField(max_length=255, null=True, blank=True)
    isexpiredcookie = models.CharField(max_length=255, null=True, blank=True)

    #__Account_FIELDS__END

    class Meta:
        verbose_name        = _("Account")
        verbose_name_plural = _("Account")


class Ban(models.Model):

    #__Ban_FIELDS__
    account = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Ban_FIELDS__END

    class Meta:
        verbose_name        = _("Ban")
        verbose_name_plural = _("Ban")



#__MODELS__END
