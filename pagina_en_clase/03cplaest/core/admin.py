from django.contrib import admin

# Register your models here.
from .models import GrantGoal

@admin.register(GrantGoal)
class GrantGoalAdmin(admin.ModelAdmin):
    list_display = [
        "gg_title",
        "timestamp",
        "days_duration",
        "final_date",
        "user"
    ]