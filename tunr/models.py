from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    population = models.IntegerField()
    description = models.TextField()


    def __str__(self):
        return self.name


class Attraction(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='attractions')
    name = models.CharField(max_length=100)
    hours = models.CharField()
    description = models.TextField()


    def __str__(self):
        return self.name
   
class Review(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()
    date_posted = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.user_name} - {self.attraction.name}"