import os
from django.core.exceptions import ValidationError



def validate_word_file_extension_on_upload(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.doc', '.docx','.docm','dotx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Only word files are allowed.')


def validate_pdf_file_extension_on_upload(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Only pdf files are allowed.')


def validate_image_extension_on_upload(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png','bmp','jpeg','jpeg 2000','jfif','tiff','gif','webP']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Only image files are allowed.')        