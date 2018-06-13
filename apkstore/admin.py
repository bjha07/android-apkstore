from django.contrib import admin

from .models import APKDetails,APKSubDetails,Category,SubCategory,Comments,Additional_info

admin.site.register(APKDetails)
admin.site.register(APKSubDetails)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Comments)
admin.site.register(Additional_info)

