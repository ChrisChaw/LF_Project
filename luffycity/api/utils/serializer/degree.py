from rest_framework import serializers
from api import models


class A(serializers.Serializer):
    value = serializers.IntegerField(source='value')


class DegreeCourseSerializer(serializers.Serializer):
    """
        只有在下面写出要显示的字段才能正确的显示，不写下面的字段只是写fields不会显示
    """
    id = serializers.IntegerField()
    name = serializers.CharField()
    teachers = serializers.CharField(source="teachers.all")
    # scholarship = serializers.CharField(source='scholarship_set.all')
    scholarship = serializers.SerializerMethodField()
    model = serializers.SerializerMethodField()
    degreecourse_price_policy = serializers.SerializerMethodField()

    def get_scholarship(self, obj):
        li = []
        for item in obj.scholarship_set.all():
            li.append(item.value)
        return li

    def get_model(self,obj):
        li = []
        for item in obj.course_set.all():
            li.append(item.name)
        return li

    def get_degreecourse_price_policy(self, obj):
        li = []
        for item in obj.degreecourse_price_policy.all():
            dict = {
                "id":item.id,
                'period':item.get_valid_period_display(),
                "_period":item.valid_period,
                "price":item.price
            }
            li.append(dict)
        return li