from django.db import models
from django.db.models import manager
from .validators import validate_word_file_extension_on_upload,validate_pdf_file_extension_on_upload,validate_image_extension_on_upload



# Create your models here.

class Users(models.Model):
    userPicture=models.ImageField(null=True,blank=True,validators=[validate_image_extension_on_upload])
    name = models.CharField(max_length=50, null=False)
    position = models.TextField(null=False)
    expertise = models.TextField(null=False)
    pLanguages=models.TextField(null=False)
    operatingSystems = models.TextField(null=False)
    programming = models.TextField(null=False)
    databases=models.TextField()
    certification=models.TextField()
    languages = models.TextField(null=False)
    educationInstitution = models.TextField(null=False)
    educationPeriod = models.CharField(max_length=50)
    educationMajor = models.TextField(null=False)
    objects = manager.Manager()
    # ides = models.TextField(null=False)
    # tools = models.TextField(null=False)
    

    def __str__(self):
        return "{}".format(self.name)


class Projects(models.Model):
    userID = models.ForeignKey(Users, on_delete=models.CASCADE)
    developerName = models.CharField(max_length=50)
    projectLogo=models.ImageField(null=True,blank=True,validators=[validate_image_extension_on_upload])
    projectDurationPeriod = models.CharField(max_length=100, null=False)
    projectEmployeer = models.CharField(
        max_length=100, null=False, default='Melon AD')
    projectName = models.CharField(max_length=50, null=False)
    developerRole = models.CharField(max_length=50, null=False)
    projectDescription = models.TextField(null=False)
    developerResponsibilities = models.TextField(null=False)
    usedTechnologies = models.TextField(null=False)
    additionalProjectInfo=models.TextField(null=True)
    objects = manager.Manager()

    def __str__(self):
        return "{}".format(self.projectName)



class FileUpload(models.Model):
    owner=models.ForeignKey(Users,on_delete=models.CASCADE)
    ownerName=models.CharField(max_length=100)
    word_doc_path=models.FileField(validators=[validate_word_file_extension_on_upload],upload_to="cv_word_doc")
    pdf_doc_path=models.FileField(validators=[validate_pdf_file_extension_on_upload],upload_to="cv_pdf_doc")
    content_word=models.TextField(blank=True)
    content_pdf=models.TextField(blank=True)
    isParsed=models.BooleanField(default=False)
    objects = manager.Manager()

    def __str__(self):
        return "{}".format(self.ownerName)