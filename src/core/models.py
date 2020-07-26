from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Journal(models.Model):
    title = models.CharField(max_length=250)

    author = models.ForeignKey(
        'Author', related_name='journal_by', on_delete=models.CASCADE)

    categories = models.ForeignKey(
        'Categories', related_name='journal_tagged_by', on_delete=models.CASCADE)

    publish_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    reviewed = models.BooleanField(default=False)
