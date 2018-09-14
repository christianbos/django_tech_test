# DJANGO CORE IMPORTS
from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'single-user'),
        (2, 'station-manager'),
        (3, 'lines-manager'),
        (4, 'administrator'),
    )
    user_type = models.PositiveSmallIntegerField(default=1, choices=USER_TYPE_CHOICES)

    class Meta:
        verbose_name = 'Usuarios'
        permissions = (
            ("is_line_manager", "Line Manager can add-edit"),
            ("is_station_manager", "Station Manager can add-edit"),
            ("is_urbvan_administrator", "Urbvan Administrator can add-edit-delete"),
        )
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            super(User, self).save(*args, **kwargs)
            self.set_permissions(self.user_type)
        else:
            super(User, self).save(*args, **kwargs)


    def set_permissions(self, user_type):
        if self.user_type==2:
            permission = Permission.objects.get(codename='is_station_manager')
            self.user_permissions.add(permission)
        elif self.user_type==3:
            permission = Permission.objects.get(codename='is_line_manager')
            self.user_permissions.add(permission)
        elif self.user_type==4:
            permission = Permission.objects.get(codename='is_urbvan_administrator')
            self.user_permissions.add(permission)
        else:
            pass