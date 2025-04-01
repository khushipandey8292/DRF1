from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # name=serializers.CharField(read_only=True)
    # def start_with_k(value):
    #     if value[0].lower()!='k':
    #         raise serializers.ValidationError('name should be start with k')
    #name=serializers.CharField(validators=[start_with_k])
    class Meta:
        model=Student
        fields=['name','roll','city']
        # read_only_fields=['name','city']
        # extra_kwargs={'name':{'read_only':True}}
        
# Field lavel validation

    # def validate_roll(self,value):
    #     if value>=200:
    #         raise serializers.ValidationError('Seat full')
    #     return value
    
# object level validation  
 
    # def validate(self,data):
    #     nm=data.get('name')
    #     ct=data.get('city')
    #     if nm.lower()=='ravi' and ct.lower()!='dhanbad':
    #         raise serializers.ValidationError('city must be Dhanbad')
    #     return data