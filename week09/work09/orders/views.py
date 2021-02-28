from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Orders
from .serializers import OrdersSerializer


class CreateOrdersView(generics.CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = (IsAuthenticated,)


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

    @action(detail=True, methods=['GET'])
    def cancel(self, request, *args, **kwargs):
        order = self.get_object()
        if order.is_cancel is False:
            order.is_cancel = True
            order.save()
            return Response({'status': '订单取消成功'})
        else:
            return Response({'status': '订单已取消, 请不要重复提交'},
                            status=status.HTTP_400_BAD_REQUEST)
