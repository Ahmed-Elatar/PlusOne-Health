from django.contrib import admin
from .models import *
from .forms import *


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)
    pass


class PostAdmin(admin.ModelAdmin):
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(auth=request.user)
    
    # readonly_fields=('auth',)
    pass

admin.site.register(Post,PostAdmin)

admin.site.register(PostComment)



admin.site.register(UserProfile,UserProfileAdmin)


