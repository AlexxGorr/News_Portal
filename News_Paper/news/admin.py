from django.contrib import admin
from .models import *

admin.site.register(Authors)
admin.site.register(Categories)
admin.site.register(Posts)
admin.site.register(Post_Category)
admin.site.register(Comments)

