from django_elasticsearch_dsl import DocType, Index
from .models import Users,Projects,FileUpload



usersIndex=Index('users')
projectsIndex=Index('projects')
fileUploadIndex=Index('fileupload')

usersIndex.settings(
    number_of_shards=1,
    number_of_replicas=0
)

projectsIndex.settings(
    number_of_shards=1,
    number_of_replicas=0
)
fileUploadIndex.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@usersIndex.doc_type
class UsersDocument(DocType):
        class Meta:
            model=Users

            fields=[
            'id',
            'userPicture',
            'name',
            'position',
            'expertise',
            'pLanguages',
            'operatingSystems',
            'programming',
            'databases',
            'certification',
            'languages',
            'educationInstitution',
            'educationPeriod',
            'educationMajor',
            ]



@projectsIndex.doc_type
class ProjectsDocument(DocType):
        class Meta:
            model=Projects
            fields = [
                'id',
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
            ]


@fileUploadIndex.doc_type
class fileUploadDocument(DocType):
        class Meta:
            model=FileUpload
            fields=[
            'id',
            'ownerName',
            'word_doc_path',
            'pdf_doc_path',
            'content_word',
            'content_pdf',
            'isParsed'
        ]
