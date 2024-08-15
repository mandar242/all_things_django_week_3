# we need serializers because response object cannot handle complex data types such as django model instances
# so we need to serialize them before rendering it out

from rest_framework import serializers
from base.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
