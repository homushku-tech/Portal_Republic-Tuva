from rest_framework.serializers import ModelSerializer
from main.models import News

class OrderSerializer(ModelSerializer):

    class Meta:
        model = News
        fields = ['name', 'text', 'date']