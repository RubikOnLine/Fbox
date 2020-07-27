from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view

from .recipients import recipients
from .foodboxes import foodboxes


@api_view(http_method_names=['GET'])
def foodboxes_list(request):
    result = []

    if request.query_params.get("price"):
        for fbox in foodboxes:
            if int(fbox["price"]) >= int(request.query_params.get("price")):
                result.append(fbox)

    if request.query_params.get("weight_grams"):
        for fbox in foodboxes:
            if int(fbox["weight_grams"]) >= int(request.query_params.get("weight_grams")):
                result.append(fbox)

    else:
        for fbox in foodboxes:
            result.append(
                {"title": fbox["name"],
                 "description": fbox["about"],
                 "price": fbox["price"],
                 "weight": fbox["weight_grams"]
                 })

    return Response(result)


@api_view(http_method_names=['GET'])
def foodbox(request, pk):

        if not pk:
            return Response(status=status.HTTP_404_NOT_FOUND)

        for fbox in foodboxes:
            if fbox['inner_id'] == pk:
                return Response(fbox)



@api_view(http_method_names=['GET'])
def recipients_list(request):
    result = []

    if request.query_params:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    for recip in recipients:
        result.append(
            {"surname": recip["info"]["name"],
             "name": recip["info"]["name"],
             "patronymic": recip["info"]["patronymic"],
             "phoneNumber": recip["contacts"]["phoneNumber"],
             })

    return Response(result)


@api_view(http_method_names=['GET'])
def recipient(request, pk):

    if not pk:
        return Response(status=status.HTTP_404_NOT_FOUND)

    for recip in recipients:
        if recip['id'] == pk:
            return Response(recip)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
