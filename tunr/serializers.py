from rest_framework import serializers
from .models import City, Attraction, Review

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    attraction = serializers.HyperlinkedRelatedField(
        view_name='attraction_detail',
        read_only=True
    )

    attraction_id = serializers.PrimaryKeyRelatedField(
        queryset=Attraction.objects.all(),
        source='attraction'
    )

    class Meta:
       model = Review
       fields = ('id', 'attraction', 'attraction_id', 'user_name', 'rating', 'comment', 'date_posted')

class AttractionSerializer(serializers.HyperlinkedModelSerializer):
    city = serializers.HyperlinkedRelatedField(
        view_name='city_detail',
        read_only=True
    )

    city_id = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(),
        source='city'
    )

    reviews = ReviewSerializer(
        many=True,
        read_only=True
    )

    attraction_url = serializers.HyperlinkedIdentityField(
        view_name='attraction_detail'
    )

    class Meta:
       model = Attraction
       fields = ('id', 'attraction_url', 'city', 'city_id', 'name', 'hours', 'description', 'reviews')

class CitySerializer(serializers.HyperlinkedModelSerializer):
    attractions = AttractionSerializer(
        many=True,
        read_only=True
    )

    city_url = serializers.ModelSerializer.serializer_url_field(
        view_name='city_detail'
    )

    class Meta:
       model = City
       fields = ('id', 'city_url', 'name', 'population', 'description', 'attractions')
