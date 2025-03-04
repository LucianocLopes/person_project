from django.contrib import admin

from persons import models

@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    '''Admin View for models.Person'''

    list_display = (       
                    'full_name', 
                    'cpf_number',
                    'email',
                    'date_of_birth',
                    'gender',
                    'created_at', 
                    'created_by', 
                    'modified_at',
                    'modified_by',
                )
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)
    exclude = ('created_by', 'modified_by')

    def save_model(self,request,obj,form,change):
        obj.created_by = request.user
        obj.modified_by = request.user
        obj.save()