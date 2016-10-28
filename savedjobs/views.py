from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from savedjobs.models import SavedJob
from savedjobs.serializers import SavedJobSerializer


# Create your views here.
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def savedjob_list(request):
    """
    List all code savedjobs, or create a new savedjob.
    """
    if request.method == 'GET':
        savedjobs = SavedJob.objects.all()
        serializer = SavedJobSerializer(savedjobs, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SavedJobSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def savedjob_detail(request, pk):
    """
    Retrieve, update or delete a code savedjob.
    """
    try:
        savedjob = SavedJob.objects.get(pk=pk)
    except SavedJob.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SavedJobSerializer(savedjob)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SavedJobSerializer(savedjob, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        savedjob.delete()
        return HttpResponse(status=204)
