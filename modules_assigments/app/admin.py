from django.contrib import admin
from .models import Collection , Book , Profile , Publisher , Author
# Register your models here.
admin.site.register(Collection)
admin.site.register(Book)
admin.site.register(Profile)

admin.site.register(Publisher)
admin.site.register(Author)
