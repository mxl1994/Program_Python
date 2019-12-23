#encoding:utf-8
import base64

def convert_base(param):
    a = base64.b64encode(param)
    print a


if __name__ == '__main__':
    param = '220891'
    convert_base(param)
