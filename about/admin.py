from django.contrib import admin
from about.models import About, Staff, SocialLink


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'position']
    inlines = [SocialLinkInline,]
    prepopulated_fields = {'slug':['fullname']}


admin.site.register(About)  