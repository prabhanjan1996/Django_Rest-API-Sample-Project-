from django.http import JsonResponse
from django.shortcuts import render

# Third party imports
from rest_framework.response import Response
from rest_framework.views import APIView


# def test_view(request):
#     data = {
#         'name': 'John',
#         'age': '24'
#     }
#     return JsonResponse(data)

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name': 'John',
            'age': '24'
        }
        return Response(data)
