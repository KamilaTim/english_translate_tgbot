from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
import requests

URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
KEY = 'trnsl.1.1.20180110T175529Z.b62d653c98f60e76.385b36b37a0e3c68c35c71079baf4e51e399980d'

def post_list(request):
    ERROR_DICT = {
        401: "some error...with error code",
        403: "some error...with error code",
        404: "Exceeded the daily limit on the amount of translated text",
        413: "Exceeded the maximum text size",
        422: "syntactic or semantic error",
        501: "The specified translation direction is not supported"
    }

    translated_text = ''

    def case_of_error(error_code):
        return ERROR_DICT.get(error_code, 'another mistake')

    def get_traslate(text, lang):
        request = requests.post(URL, data={'key': KEY, 'text': text, 'lang': lang})
        if request.status_code == 200:
            return request.json()
        else:
            print(case_of_error(request.status_code))

    input_text = request.GET["inputtext"]
    try:
        output = get_traslate(input_text, 'ru')
    except:
        output = None
        translated_text = "- Connection error -"

    if output:
        translated_text = output['text'][0]

    cxt = {'translated_text': translated_text}
    return render(request, 'blog/post_list.html', context=cxt)


