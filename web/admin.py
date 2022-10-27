from django.contrib import admin
from web.models import Feedback
from news.models import News
from user.models import User

# Register your models here.
admin.site.register(Feedback)
admin.site.register(News)
admin.site.register(User)
