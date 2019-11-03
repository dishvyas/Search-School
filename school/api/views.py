from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from school.models import SchoolPost
from school.api.serializers import SchoolPostSerializer



class ApiSchoolListView(ListAPIView):
    queryset = SchoolPost.objects.all()
    serializer_class = SchoolPostSerializer
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ('schoolname','address','area','pincode','landmark')
    ordering_fields = ('schoolname','pincode','medium_of_inst')

@api_view(['GET', ])
def json_data(request):
    table = []
    with open('Bangalore_schools.json', 'r') as f:
        for line in f:
            try:
                j = line.split('|')[-1]
                table.append(json.loads(j))
            except ValueError:
                continue
    for row in table:
        print(row)