from django.db import models

import select2.fields
import select2.models


class Author(models.Model):

    name = models.CharField(max_length=255)


    def __unicode__(self):
        return self.name