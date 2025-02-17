from django.contrib import admin



admin.site.site_header = "Mango Administration"
admin.site.site_title = "Mango Admin Portal"
# admin.site.index_title = "Mango-Admin"

# Register your models here.

from website.models import BlogDetails, branches,gallery,Promo,careermodel

class BranchAdmin(admin.ModelAdmin):
  
  list_display = ("branch_name", "branch_address", "branch_image",)

class GalleryAdmin(admin.ModelAdmin):
  
  list_display = ("event_name","event_image",)

class PromoAdmin(admin.ModelAdmin):
  
  list_display = ("promo_name","start_date","end_date","promo_image")

class CareerAdmin(admin.ModelAdmin):
  
  list_display = ("first_name","Last_name","phone_no","email","current_location")

class BlogAdmin(admin.ModelAdmin):
  
  list_display = ("blog_event_name","blog_description","blog_event_image","posted_date")
  

  
admin.site.register(BlogDetails,BlogAdmin)
admin.site.register(branches, BranchAdmin)
admin.site.register(careermodel, CareerAdmin)
admin.site.register(gallery,GalleryAdmin)
admin.site.register(Promo,PromoAdmin)


