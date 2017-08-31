import json

from top.alidayu import AlibabaAliqinFcSmsNumSendRequest

appkey = '23604482'
secret = 'e9553ce6ae0354af1ad294532fafd3a7'
sign = '樊志魁'
msgTemplate = "SMS_68700066"


# 其中appkey和secret是必须的参数
# url可选，默认为沙箱的URL，正式应用请传入 https://eco.taobao.com/router/rest
# partner_id为可选，其值为下载的TOP SDK中的top/api/base.py里的SYSTEM_GENERATE_VERSION
def send_msg(data, tel='17600618812'):
    print(data)
    req = AlibabaAliqinFcSmsNumSendRequest(appkey, secret, 'https://eco.taobao.com/router/rest',
                                           'taobao-sdk-python-20160607')
    req.extend = ""
    req.sms_type = "normal"
    req.sms_free_sign_name = sign
    req.sms_param = json.dumps(data)
    req.rec_num = tel
    req.sms_template_code = msgTemplate
    try:
        resp = req.getResponse()
        print(resp)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    data = dict(username='樊志魁', ip='127-0-0-1', filename='C:\\6.0')
    send_msg(data, '18435155938')
