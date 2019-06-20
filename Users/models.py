from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(models.Model):
    name = models.CharField(_('name'), max_length=255)
    lastName = models.CharField(_('lastName'), max_length=255)

    cpf = models.CharField(_('cpf'), max_length=15, null=True, blank=True)
    email = models.EmailField(_('email'), max_length=255, unique=True)
    password = models.CharField(_('password'), max_length=255)
    birthdate = models.DateField(_('birthdate'), null=True, blank=True)
    phone = models.CharField(_('phone'), max_length=20, null=True, blank=True)

    type = models.CharField(_('type'), max_length=20, null=True, blank=True)
    class Meta:
        ordering = ['name']
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        db_table = "users"

    def __str__(self):
        return '# ' + str(self.id) + ' ' + self.name + ' ' + self.lastName  + ' ' + self.type