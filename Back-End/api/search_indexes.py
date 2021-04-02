from haystack import indexes
from .models import Projects
from .models import Users
from .models import FileUpload



class UsersIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    position = indexes.NgramField(model_attr='position')
    expertise = indexes.NgramField(model_attr='expertise')
    pLanguages = indexes.NgramField(model_attr='pLanguages')
    operatingSystems = indexes.NgramField(model_attr='operatingSystems')
    programming = indexes.NgramField(model_attr='programming')
    databases = indexes.CharField(model_attr='databases')
    certification = indexes.NgramField(model_attr='certification')
    languages = indexes.NgramField(model_attr='languages')
    educationInstitution = indexes.NgramField(
        model_attr='educationInstitution')
    educationPeriod = indexes.NgramField(model_attr='educationPeriod')
    educationMajor = indexes.NgramField(model_attr='educationMajor')
    content_auto = indexes.EdgeNgramField(model_attr='content')

    def get_model(self):
        return Users


class ProjectsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    userID = indexes.IntegerField(model_attr='userID')
    developerName = indexes.NgramField(model_attr='developerName')
    projectDurationPeriod = indexes.NgramField(model_attr='projectDurationPeriod')
    projectEmployeer = indexes.NgramField(model_attr='projectEmployeer')
    projectName = indexes.NgramField(model_attr='projectName')
    developerRole = indexes.NgramField(model_attr='developerRole')
    projectDescription = indexes.NgramField(model_attr='projectDescription')
    developerResponsibilities = indexes.NgramField(model_attr='developerResponsibilities')
    usedTechnologies = indexes.NgramField(model_attr='usedTechnologies')
    additionalProjectInfo=indexes.NgramField(model_attr='additionalProjectInfo')
    content_auto = indexes.EdgeNgramField(model_attr='content')

    def get_model(self):
        return Projects


class FileUploadIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    ownerName = indexes.IntegerField(model_attr='ownerName')
    word_doc_path = indexes.NgramField(model_attr='word_doc_path')
    pdf_doc_path = indexes.NgramField(model_attr='pdf_doc_path')
    content_word=indexes.NgramField(model_attr='content_word')
    content_pdf=indexes.NgramField(model_attr='content_pdf')
    isParsed=indexes.CharField()

    def get_model(self):
        return FileUpload
