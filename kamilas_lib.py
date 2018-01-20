# coding=utf-8
import requests

URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
KEY = 'trnsl.1.1.20180110T175529Z.b62d653c98f60e76.385b36b37a0e3c68c35c71079baf4e51e399980d'
#KEY = 'trnsl.1.1.20123456789180110T175529Z.b62d653c98f60e76.385b36b37a0e3c68c35c71079baf4e51e399980d'


# def get_traslate(text, lang):
#     try:
#         r = requests.post(URL, data={'key': KEY, 'text': text, 'lang': lang})
#     except requests.exceptions.ConnectionError:
#         print ('no internet access')
#     else:
#         if r.status_code == 200:
#             return r.json()
#         else:
#             print ('some error... with error code', r.status_code)



# def case_of_error(error_code):
#     return error_dict.get(request.status_code, 'no key')
ERROR_DICT = {
    401: "some error...with error code",
    403: "some error...with error code",
    404: "Exceeded the daily limit on the amount of translated text",
    413: "Exceeded the maximum text size",
    422: "syntactic or semantic error",
    501: "The specified translation direction is not supported"
}


def case_of_error(error_code):
    return ERROR_DICT.get(error_code, 'another mistake')


def get_traslate(text, lang):
    request = requests.post(URL, data={'key': KEY, 'text': text, 'lang': lang})
    #print request.status_code
    if request.status_code == 200:
        return request.json()
    else:
        print case_of_error(request.status_code)


if __name__ == '__main__':
    input_text = raw_input('Write your text: ')
    output = get_traslate(input_text, 'ru')
    if output:
        print output['text'][0]