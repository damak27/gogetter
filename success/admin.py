from django.contrib import admin
from .models import Articles
from .models import Contact
from .models import Quotes

class admin_design(admin.ModelAdmin):
      list_display = ["author","article_title","Created_time",]
      class meta:
          model = Articles
admin.site.register(Articles,admin_design),

class contact_design(admin.ModelAdmin):
      list_display = [ "First_name","email_address",]
      class meta:
          model = Contact
admin.site.register(Contact,contact_design),

class  quotes_design(admin.ModelAdmin):
      list_display = [ "quote","quote_by"]
      class meta:
          model = Quotes
admin.site.register(Quotes, quotes_design),



# Register your models here.
