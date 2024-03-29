"""错误信息"""

# 百度语音合成错误信息，更多信息参考：
# https://cloud.baidu.com/doc/SPEECH/TTS-Online-Python-SDK/12.5C.E7.AE.80.E4.BB.8B.html
mix_error = {500: '不支持的输入', 501: '输入参数不正确', 502: 'token验证失败', 503: '合成后端错误'}


# 百度语音识别接口错误信息，更多信息参考下面链接：
# https://cloud.baidu.com/doc/SPEECH/ASR-Online-Python-SDK.html#.E9.94.99.E8.AF.AF.E7.A0.81
recog_error = {3300: '用户输入错误',
               3301: '没听清, 再说一遍试试',
               3302: '鉴权失败\ntoken字段校验失败。请使用正确的API_KEY 和 SECRET_KEY生成',
               3303: '服务端问题\n语音服务器后端问题\n请将api返回结果反馈至论坛或者QQ群',
               3304: '用户请求超限\n用户的请求QPS超限\n请降低识别api请求频率',
               3305: '用户请求超限\n用户的日pv（日请求量）超限\n请“申请提高配额”，如果暂未通过，请降低日请求量',
               3307: '服务端问题\n语音服务器后端识别出错问题\n目前请确保16000的采样率音频时长低于30s，8000的采样率音频时长低于60s。如果仍有问题，请将api返回结果反馈至论坛或者QQ群',
               3308: '音频过长\n音频时长不超过60s，请将音频时长截取为60s以下',
               3309: '音频数据问题\n服务端无法将音频转为pcm格式，可能是长度问题，音频格式问题等。 请将输入的音频时长截取为60s以下，并核对下音频的编码，是否是8K或者16K， 16bits，单声道。',
               3310: '输入的音频文件过大',
               3311: '采样率rate参数不在选项里\n目前rate参数仅提供8000,16000两种',
               3312: '音频格式format参数不在选项里\n目前格式仅仅支持pcm，wav或amr'}


# 图灵机器人接口错误信息，详情参考：
# https://www.kancloud.cn/turing/www-tuling123-com/718227
robot_error = {'0': '上传成功',
               '4000': '请求参数格式错误',
               '4001': '加密方式错误',
               '4002': '无功能权限',
               '4003': '该apikey没有可用请求次数',
               '4005': '无功能权限',
               '4007': 'apikey不合法',
               '4100': 'userid获取失败',
               '4200': '上传格式错误',
               '4300': '批量操作超过限制',
               '4400': '没有上传合法userid',
               '4500': 'userid申请个数超过限制',
               '4600': '输入内容为空',
               '4602': '输入文本内容超长(上限150)',
               '5000': '无解析结果',
               '6000': '暂不支持该功能',
               '7002': '上传信息失败',
               '8008': '服务器错误'}
