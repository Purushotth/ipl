# -*- coding: utf-8 -*-

"""
Personify Account Section/Borrower Portal Models
"""
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models
from django.utils import timezone
from django.utils.timezone import localtime, make_aware

# -*- Account Section Database Models -*-


class IPLUserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False):
        """
        Override Django's default User model.
        """
        if not email:
            raise ValueError('Users must have an email address!')

        user = self.model(
                email=self.normalize_email(email.lower()),
                created_dtm=localtime(timezone.now()),
                is_staff=is_staff
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, contact ID (from Salesforce) and password.
        """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class IPLUser(AbstractBaseUser):
    """
    Our own custom User model.
    """
    email = models.EmailField('Email Address', null=False, max_length=254, unique=True)
    created_dtm = models.DateTimeField('Created', default=localtime(timezone.now()))
    is_staff = models.BooleanField('Is Staff?', default=False)
    is_superuser = models.BooleanField('Is Superuser?', default=False)

    objects = IPLUserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    class Meta:
        db_table = 'users'
        get_latest_by = 'created_dtm'

