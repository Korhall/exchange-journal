from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Sector, Branch, EnterpriseSegment

# Register your models here.

@admin.register(Sector)
class SectorAdmin(ImportExportModelAdmin):
    list_display = ('fieldSectorName',)
    list_display_links = ('fieldSectorName',)
    
@admin.register(Branch)
class BranchAdmin(ImportExportModelAdmin):
    list_display = ('fieldBranchName',)
    list_display_links = ('fieldBranchName',)
    #resource_class = BranchResource
    
@admin.register(EnterpriseSegment)
class EnterpriseSegmentAdmin(admin.ModelAdmin):
    list_display = ('fieldSector','fieldBranch','fieldCompanyName',)
    list_display_links = ('fieldBranch',)
    

class BranchResource(resources.ModelResource):
    
    class Meta:
        model = Branch
        fields = ('fieldBranchName',)
        skip_unchanged = True
        report_skiped = False
        
class SectorResource(resources.ModelResource):
    
    class Meta:
        model = Sector
        fields = ('fieldSectorName',)
        skip_unchanged = True
        report_skiped = False