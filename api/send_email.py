def send(msg, to_addr):
    from email.header import Header
    from email.mime.text import MIMEText
    from email.utils import parseaddr, formataddr

    import smtplib

    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    from_addr = 'fzk466569@sina.com'
    password = 'fzk466566'
    smtp_server = 'smtp.sina.com'

    msg = MIMEText(msg, 'plain', 'utf-8')
    msg['From'] = _format_addr('基于webshell的校园网络安全系统 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr[0])
    msg['Subject'] = Header('服务器webshel提示', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


def send_email(data, address=['fzk466569@163.com']):
    print('data111111111111111111111111', data)
    # print(data.get('username'))
    # print(data.get('ip'))
    # print(data.get('filename'))
    message = '亲爱的{0}:\n\t你的服务器{1}，现在有文件{2}上传，对该文件扫描后发现该文件很可疑{3}，建议马上处理。'.format(data.get('username'),
                                                                                        data.get('ip'),
                                                                                        data.get('filename'),
                                                                                        data.get('target'))
    return send(message, address)


if __name__ == '__main__':
    # send_data = dict(username='樊志魁', ip='127-0-0-1', filename='I:/bishexiangguan/test/safe/unsafe', target='ffff')
    send_data = {'username': 'fzk', 'ip': '127.0.0.1', 'filename': 'I:/bishe/test/1 - 副本 - 副本.txt', 'target': '1'}
    send_email(send_data, ['fzk466569@163.com'])
