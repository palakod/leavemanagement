class Calendar(models.Model):

    date = models.DateField()
    occasion = models.CharField(max_length = 20)