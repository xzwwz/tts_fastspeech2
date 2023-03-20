import os
import re
from django.shortcuts import render
from .utils import rmWavs, merge_files


# Create your views here.

def index(request):
    value = {'text': ''}
    return render(request, "index.html", context=value)


def tts(request):
    # print(request.headers)
    # print(request.encoding)
    print(request.GET.get('input'))

    texts = request.GET.get('input')
    value = {'text': texts}
    texts = re.split('，|。|！|？', texts)
    wav_path = os.path.join('fastspeech2/output/result/BZNSYP')
    mp3_path = os.path.join('firstapp/static/tts/audio-file.mp3')

    rmWavs(wav_path)
    for text in texts:
        if text != '':
            print(text)
            order = 'python fastspeech2/synthesize.py --text \"' + text + '\" --restore_step 400000 --mode single -p fastspeech2/config/BZNSYP/preprocess.yaml -m fastspeech2/config/BZNSYP/model.yaml -t fastspeech2/config/BZNSYP/train.yaml --duration_control 1 --energy_control 0.8'
            os.system(order)
    merge_files(wav_path, texts, mp3_path)
    return render(request, 'index.html', context=value)
