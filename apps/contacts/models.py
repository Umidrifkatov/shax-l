from django.db import models
from django.utils.translation import gettext_lazy as _

class ContactRequest(models.Model):
    STATUS_CHOICES = [
        ('new', _('Новый')),
        ('in_progress', _('В работе')),
        ('completed', _('Завершен')),
    ]

    name = models.CharField(_('Имя'), max_length=100)
    company = models.CharField(_('Компания'), max_length=100, blank=True)
    phone = models.CharField(_('Телефон'), max_length=30)
    email = models.EmailField(_('Email'))
    service_type = models.CharField(_('Тип услуги'), max_length=50)
    cargo_description = models.TextField(_('Описание груза'))
    origin = models.CharField(_('Откуда'), max_length=200)
    destination = models.CharField(_('Куда'), max_length=200)
    weight = models.CharField(_('Вес'), max_length=50, blank=True)
    volume = models.CharField(_('Объем'), max_length=50, blank=True)
    message = models.TextField(_('Сообщение'), blank=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Заявка')
        verbose_name_plural = _('Заявки')

    def __str__(self):
        return f"{self.name} - {self.service_type} ({self.created_at.strftime('%d.%m.%Y')})"
