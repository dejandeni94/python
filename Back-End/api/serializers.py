
from rest_framework import serializers
from . import models


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'userPicture',
            'name',
            'position',
            'expertise',
            'pLanguages',
            'operatingSystems',
            'programming',
            'databases',
            'certification',
            'languages'
            'educationInstitution',
            'educationPeriod',
            'educationMajor',
        )

        model = models.Users
        read_only_fields = ('id',)

class ProjectsSerializer(serializers.ModelSerializer):
        class Meta:
            fields = (
                'id',
                'userID',
                'developerName',
                'projectLogo',
                'projectDurationPeriod',
                'projectEmployeer',
                'projectName',
                'developerRole',
                'projectDescription',
                'developerResponsibilities',
                'usedTechnologies',
                'additionalProjectInfo'
            )
            model = models.Projects
            read_only_fields = ('id',)
        users = serializers.PrimaryKeyRelatedField(
        many=True, queryset=models.Users.objects.all())



class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'owner',
            'ownerName',
            'word_doc_path',
            'pdf_doc_path',
            'content_word',
            'content_pdf',
            'isParsed'
        )
        model = models.FileUpload
        read_only_fields = ('id',)
        user = serializers.PrimaryKeyRelatedField(
        many=True, queryset=models.Users.objects.all())

