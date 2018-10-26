from django.contrib import admin
from .models import Profile,Leagues,Message,Fixtures,Teams
# Register your models here.

# class ArticleAdmin(admin.ModelAdmin):
#     filter_horizontal =('teamA','teamB')


admin.site.register(Profile)
admin.site.register(Message)
admin.site.register(Leagues,)
admin.site.register(Fixtures)
admin.site.register(Teams)