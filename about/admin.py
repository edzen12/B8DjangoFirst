from django.contrib import admin
from about.models import About, Staff, SocialLink


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'position']
    inlines = [SocialLinkInline,]


admin.site.register(About)  