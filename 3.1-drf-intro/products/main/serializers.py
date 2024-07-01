from rest_framework import serializers

from main.models import Review, Product


class ReviewSerializer(serializers.ModelSerializer):
    # реализуйте все поля
    class Meta:
        model = Review
        fields = '__all__'


class ProductListSerializer(serializers.Serializer):
    # реализуйте поля title и price
    title = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)


class ProductReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'mark']

        
class ProductDetailsSerializer(serializers.ModelSerializer):
    # реализуйте поля title, description, price и reviews
    reviews = ProductReviewsSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'reviews']

