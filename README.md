# english_translate_tgbot
# coding=utf-8
import requests

URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
KEY = 'trnsl.1.1.20180110T175529Z.b62d653c98f60e76.385b36b37a0e3c68c35c71079baf4e51e399980d'
KEY = 'trnsl.1.1.20123456789180110T175529Z.b62d653c98f60e76.385b36b37a0e3c68c35c71079baf4e51e399980d'


def get_traslate(text, lang):
    try:
        r = requests.post(URL, data={'key': KEY, 'text': text, 'lang': lang})
    except requests.exceptions.ConnectionError:
        print ('no internet access')
    else:
        if r.status_code == 200:
            return r.json()
        else:
            print ('some error... with error code', r.status_code)

input_text = raw_input('Write your text: ')
# input_text = 'i love dogs'
# with open('kamilas_lib.py') as f:
#    input_text = f.read() * 1000

output = get_traslate(input_text, 'ru')
if output:
    print output['text'][0]
