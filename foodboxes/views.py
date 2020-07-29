from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view

from .recipients import recipients
from .foodboxes import foodboxes


@api_view(http_method_names=['GET'])
def foodboxes_list(request):
    result = []
    """ Допольнителный словарь с полями для выборок """
    field_dict = {"price": None,
                  "weight_grams": None}

    """ Распаковка словаря request.query_params содержащий поля и значение из запроса. К примеру, запрос ?price=2000 - ['price': 2000] """
    dict_a = list(request.query_params.keys())

    if dict_a:
        for fbox in foodboxes:
            if fbox[dict_a[0]] >= int(request.query_params.get(dict_a[0])):
                result.append(fbox)

    else:
        result = foodboxes

    """ Вывод результата в строгом формате """

    response = []
    # print(result)
    for res in result:
        print(res)
        response.append(
            {"title": res["name"],
             "description": res["about"],
             "price": res["price"],
             "weight": res["weight_grams"]
             })

    return Response(response)


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
