from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def test_response(request):
    return HttpResponse(200)
