from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from xml_converter.resources import handle_xml_file


class ConverterViewSet(ViewSet):
    # Note this is not a restful API
    # We still use DRF to assess how well you know the framework
    parser_classes = [MultiPartParser]

    @action(methods=["POST"], detail=False, url_path="convert")
    def convert(self, request, **kwargs):
        # import pdb;  pdb.set_trace()
        if request.FILES['file']:
            xml_converted = handle_xml_file(request.FILES['file'])
            return JsonResponse(xml_converted)
        else:
            return JsonResponse({'Message': 'File not found'})
