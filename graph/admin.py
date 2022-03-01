from django.contrib import admin

# Register your models here.
from .models import EmailSubscriber
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.core.serializers.json import DjangoJSONEncoder
import json


@admin.register(EmailSubscriber)
class EmailSubscriberAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "created_at")
    ordering = ("-created_at",) 
    change_list_template ='graph/change_list.html'


    def changelist_view(self, request, extra_context=None):
            # Aggregate new subscribers per day
            chart_data = (
                EmailSubscriber.objects.annotate(date=TruncDay("created_at"))
                .values("date")
                .annotate(y=Count("id"))
                .order_by("-date")
            )

            # Serialize and attach the chart data to the template context
            as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
            extra_context = extra_context or {"chart_data": as_json}

            # Call the superclass changelist_view to render the page
            return super().changelist_view(request, extra_context=extra_context)