from django.contrib import admin
from .models import Course, Offer


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'length')


admin.site.register(Offer, OfferAdmin)
admin.site.register(Course, CourseAdmin)
