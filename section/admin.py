from django.contrib import admin

# Register your models here.

from section.models import (
    MainSection,
    AboutSection,
    Catalog,
    Product,

)

class MainSectionAdmin(admin.ModelAdmin):
    pass

class AboutSectionAdmin(admin.ModelAdmin):
    pass

class CatalogAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(MainSection, MainSectionAdmin)
admin.site.register(AboutSection, AboutSectionAdmin)
admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Product, ProductAdmin)
