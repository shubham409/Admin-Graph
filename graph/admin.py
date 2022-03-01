from django.contrib import admin

# Register your models here.
from .models import EmailSubscriber

@admin.register(EmailSubscriber)
class EmailSubscriberAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "created_at")
    ordering = ("-created_at",) 
    change_list_template ='graph/change_list.html'
    