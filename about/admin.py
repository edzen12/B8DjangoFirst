from django.contrib import admin
from about.models import About, Staff, SocialLink, ImagesStaff


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1


class ImagesStaffInline(admin.TabularInline):
    model = ImagesStaff
    extra = 3


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'position']
    inlines = [SocialLinkInline, ImagesStaffInline]
    prepopulated_fields = {'slug':['fullname']}


admin.site.register(About)  