from django.contrib import admin

# Зарегистрируйте свои модели в админ панели здесь
from django.contrib import admin
from .models import Author, Entry, AuthorProfile, Tag

admin.site.register(Author)
admin.site.register(AuthorProfile)