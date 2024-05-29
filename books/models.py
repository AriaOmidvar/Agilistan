from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    edition = models.CharField(max_length=50, null=True, blank=True)
    authors = models.CharField(max_length=200)  # Assuming a comma-separated list of authors

    def __str__(self):
        return self.title