from rest_framework import serializers
from .models import Orders


class OrdersSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Orders
        fields = ('order_id', 'amount', 'is_cancel', 'create_time', 'update_time')
        read_only_fields = ['is_cancel']
