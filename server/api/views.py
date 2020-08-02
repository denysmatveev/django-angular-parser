from rest_framework.response import Response
from rest_framework.views import APIView

from .models import DataList
from .serializers import DataListSerializer

class DateListView(APIView):
    def get(self, request):
        data = DataList.objects.all()
        serializer = DataListSerializer(data, many=True)
        response = Response({'data': serializer.data})
        response["Access-Control-Allow-Origin"] = "http://127.0.0.1:4200"
        response["Access-Control-Allow-Methods"] = "GET"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        return response
