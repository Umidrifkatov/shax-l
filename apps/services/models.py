from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Service(models.Model):
    CATEGORY_CHOICES = [
        ('auto', _('Автоперевозки')),
        ('air', _('Авиаперевозки')),
        ('rail', _('Железнодорожные перевозки')),
        ('sea', _('Морские перевозки')),
        ('multimodal', _('Мультимодальные перевозки')),
        ('additional', _('Дополнительные услуги')),
    ]

    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=50, help_text="FontAwesome icon name (e.g., 'truck')")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    features = models.JSONField(default=list, blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']
        verbose_name = _('Услуга')
        verbose_name_plural = _('Услуги')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services:detail', kwargs={'slug': self.slug})
