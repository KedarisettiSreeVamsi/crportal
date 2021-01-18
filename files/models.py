from django.db import models
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField

class Subject(models.Model):
    name = models.CharField(max_length=255)
    file = FilerFileField(null=True, blank=True,
                                related_name="pdf_file")