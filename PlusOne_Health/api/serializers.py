from rest_framework import serializers

from .models import *




class UserProfileSerializer(serializers.ModelSerializer):

    
    class Meta:
        depth=0
        model=UserProfile
        fields=['bio','image']
        # extra_kwargs={
        #     'user':{'write_only':True}
            

        # }
        