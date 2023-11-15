from django.contrib import admin, messages
from .models import Author
# Register your models here.


def validate_author(obj):
    if len(obj.name) < 5:
        return False, "Author name should contain atleast 5 char"

    return True, ""


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','name','address', 'dob', 'country')
    list_filter = ('status','country')
    readonly_fields = ("country",)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        if request.user.has_perm('blog.add_author'):
            return True
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return True


    def save_model(self, request, obj, form, change):
        is_valid, err_msg = validate_author(obj)

        if is_valid:
            return super().save_model(request, obj, form, change)

        messages.set_level(request, messages.ERROR)
        messages.error(request, err_msg)


admin.site.register(Author, AuthorAdmin)






