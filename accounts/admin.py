from django.contrib import admin
from .models import RandomNumberModel


class RandomNumberAdmin(admin.ModelAdmin):
    list_display = ['id', 'random_number', 'updated_at', 'user', 'timestamp']
    list_display_links = ['id', 'random_number', 'updated_at', 'user', 'timestamp']

    class Meta:
        model = RandomNumberModel


admin.site.register(RandomNumberModel, RandomNumberAdmin)

