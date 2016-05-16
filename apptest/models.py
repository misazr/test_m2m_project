from django.db import models

import select2.fields
import select2.models


class Author(models.Model):

    name = models.CharField(max_length=255)


    def __unicode__(self):
        return self.name

class Entry(models.Model):

    authors = select2.fields.ManyToManyField(Author,
                                             through='EntryAuthors',
                                             sort_field='position')


class EntryAuthors(select2.models.SortableThroughModel):

    author = models.ForeignKey(Author)
    entry = models.ForeignKey(Entry)
    position = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['position']