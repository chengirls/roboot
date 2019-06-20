import requests
import json
import time
from aip import AipSpeech
import os

def get_roboot_answer(info):
    url = 'http://api.qingyunke.com/api.php'

    params = {
        'key': 'free',
        'appid': 0,
        'msg': info
    }
    res = requests.get(url, params=params)
    if res.status_code == 200:
        return res.json()['content']
    else:
        return '网络连接错误!'

APP_ID='16574992'
API_KEY = 'Se1pQXlRIVxiNCiwC4YPezgg'
SECRET_KEY = 'aoxVXTChFGhEe4A0NSkvkwTPqtSLuOP3'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result  = {
    'vol': 5, 'per':'4','pit':'5'
}
def text2audio(worlds,role_param,out_putfile,lang='zh'):
    result = client.synthesis(worlds,lang,1,role_param)

    if not isinstance(result, dict):
        with open(out_putfile, 'wb') as f:
            f.write(result)
        return 'ok'

def anything2pcm(input_file):
    """将一切格式的音频转为 pcm 格式，需将ffmpeg 添加到环境变量"""
    # input_file = os.path.join(os.getcwd(), input_file)
    output_file = input_file.rsplit('.', 1)[0] + '.pcm'
    cmd = 'ffmpeg -y  -i {}  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {}'.format(input_file, output_file)
    print(os.popen(cmd).read())
    # print('转换完成！')
    return output_file


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read


if __name__ == '__main__':
    # 测试代码，如发现/static/audio_file下有auido.pcm，先删除 然后运行，发现生成 auido.pcm，证明 ffmpeg可用
    input_file = os.path.join('static', 'audio_file', 'auido.mp3')
    print(input_file)
print(anything2pcm(input_file))


if __name__ == '__main__':
    file_name = 'auido.mp3'

    output_file = anything2pcm(file_name)
    resul = client.asr(get_file_content(output_file), 'pcm', 16000, {
        'dev_pid': 1536
    })

    print(result)
