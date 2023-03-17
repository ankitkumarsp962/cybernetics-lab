from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import millify


@api_view(["GET"])
def prettify_number(request, *args, **kwargs):
    '''
    '''
    query = request.GET.get('q', 0)
    try :
        query = float(query)
        ctx = {'query':millify(query) or query}
        return Response(ctx)
    except ValueError:
        return Response({'error':'please provide an integer in query'})
