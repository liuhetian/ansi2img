# ansi2img

把报错转为图像地址，可以继续发送给钉钉(微信 QQ没试过)

##
```bash
sudo apt-get update
sudo apt-get install wkhtmltopdf
pip install ansi2html imgkit boto3 fastapi uvicorn python-dotenv

git clone git@github.com:liuhetian/ansi2img.git
vi .secrets  # 写密码
uvicorn main:app --reload
```
效果
```python

import requests
a = '''
[32m2023-12-12 17:03:19.484[0m | [33mRETRY   [0m | [36mtest.testa[0m:[36mwrapper[0m:[36m37[0m - [33mAn error has occurred[0m
[33m[1mTraceback (most recent call last):[0m

  File "[32m/home/ubuntu/main/重试并保存错误/[0m[32m[1mtest.py[0m", line [33m14[0m, in [35m<module>[0m
    [1mf[0m[1m([0m[1m)[0m
    [36m└ [0m[36m[1m<function f at 0x7f49c028e200>[0m

> File "[32m/home/ubuntu/main/重试并保存错误/test/[0m[32m[1mtesta.py[0m", line [33m29[0m, in [35mwrapper[0m
    [35m[1mreturn[0m [1mfunc[0m[1m([0m[35m[1m*[0m[1margs[0m[1m,[0m [35m[1m**[0m[1mkwargs[0m[1m)[0m
    [36m       │     │       └ [0m[36m[1m{}[0m
    [36m       │     └ [0m[36m[1m()[0m
    [36m       └ [0m[36m[1m<function f at 0x7f49c2a58ea0>[0m

  File "[32m/home/ubuntu/main/重试并保存错误/[0m[32m[1mtest.py[0m", line [33m12[0m, in [35mf[0m
    [35m[1mreturn[0m [34m[1m5[0m [35m[1m+[0m [1ma[0m [35m[1m/[0m [1mb[0m
    [36m           │   └ [0m[36m[1m0[0m
    [36m           └ [0m[36m[1m1[0m

[31m[1mZeroDivisionError[0m:[1m division by zero[0m
'''
url = f'http://43.142.41.210:8000/ansi2img?ansi_string={a}'
response = requests.post(url)

```
