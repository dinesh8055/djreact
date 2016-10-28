from rest_framework import serializers
from savedjobs.models import SavedJob
from rest_framework.validators import UniqueValidator

class SavedJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedJob
        fields = ('title', 'city', 'state', 'company', 'salary', 'salaryPer', 'description')
    # id = serializers.IntegerField(required=False, validators=[UniqueValidator(queryset=SavedJob.objects.all())])
    # title = serializers.CharField(required=False, allow_blank=True, max_length=200)
    # city = serializers.CharField(required=False, allow_blank=True, max_length=50)
    # state = serializers.CharField(required=False, allow_blank=True, max_length=50)
    # company = serializers.CharField(required=False, allow_blank=True, max_length=200)
    # salary = serializers.CharField(required=False, allow_blank=True, max_length=50)
    # salaryPer = serializers.CharField(required=False, allow_blank=True, max_length=50)
    # description = serializers.CharField(required=False, allow_blank=True, max_length=200)
    # postedDaysAgo = serializers.IntegerField(required=False, allow_null=True)
    # expireInDays = serializers.IntegerField(required=False, allow_null=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return SavedJob.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        # instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.company = validated_data.get('company', instance.company)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.salaryPer = validated_data.get('salaryPer', instance.salaryPer)
        instance.description = validated_data.get('description', instance.description)
        # instance.postedDaysAgo = validated_data.get('postedDaysAgo', instance.postedDaysAgo)
        # instance.expireInDays = validated_data.get('expireInDays', instance.expireInDays)

        instance.save()
        return instance
