## 

功能1. ansi2img

把报错转为图像地址，可以继续发送给钉钉(微信 QQ没试过)

功能2. 发送邮件

##
```bash
sudo apt-get update
sudo apt-get install wkhtmltopdf
pip install ansi2html imgkit boto3 fastapi uvicorn python-dotenv yagmail markdown

git clone git@github.com:liuhetian/ansi2img.git
vi .secrets  # 写密码
uvicorn main:app --reload --host 0.0.0.0
```
效果
```python
import requests
a = '''
 \x1b[32m2023-12-12 17:03:19.484 \x1b[0m |  \x1b[33mRETRY    \x1b[0m |  \x1b[36mtest.testa \x1b[0m: \x1b[36mwrapper \x1b[0m: \x1b[36m37 \x1b[0m -  \x1b[33mAn error has occurred \x1b[0m
 \x1b[33m \x1b[1mTraceback (most recent call last): \x1b[0m

  File " \x1b[32m/home/ubuntu/main/重试并保存错误/ \x1b[0m \x1b[32m \x1b[1mtest.py \x1b[0m", line  \x1b[33m14 \x1b[0m, in  \x1b[35m<module> \x1b[0m
     \x1b[1mf \x1b[0m \x1b[1m( \x1b[0m \x1b[1m) \x1b[0m
     \x1b[36m└  \x1b[0m \x1b[36m \x1b[1m<function f at 0x7f49c028e200> \x1b[0m

> File " \x1b[32m/home/ubuntu/main/重试并保存错误/test/ \x1b[0m \x1b[32m \x1b[1mtesta.py \x1b[0m", line  \x1b[33m29 \x1b[0m, in  \x1b[35mwrapper \x1b[0m
     \x1b[35m \x1b[1mreturn \x1b[0m  \x1b[1mfunc \x1b[0m \x1b[1m( \x1b[0m \x1b[35m \x1b[1m* \x1b[0m \x1b[1margs \x1b[0m \x1b[1m, \x1b[0m  \x1b[35m \x1b[1m** \x1b[0m \x1b[1mkwargs \x1b[0m \x1b[1m) \x1b[0m
     \x1b[36m       │     │       └  \x1b[0m \x1b[36m \x1b[1m{} \x1b[0m
     \x1b[36m       │     └  \x1b[0m \x1b[36m \x1b[1m() \x1b[0m
     \x1b[36m       └  \x1b[0m \x1b[36m \x1b[1m<function f at 0x7f49c2a58ea0> \x1b[0m

  File " \x1b[32m/home/ubuntu/main/重试并保存错误/ \x1b[0m \x1b[32m \x1b[1mtest.py \x1b[0m", line  \x1b[33m12 \x1b[0m, in  \x1b[35mf \x1b[0m
     \x1b[35m \x1b[1mreturn \x1b[0m  \x1b[34m \x1b[1m5 \x1b[0m  \x1b[35m \x1b[1m+ \x1b[0m  \x1b[1ma \x1b[0m  \x1b[35m \x1b[1m/ \x1b[0m  \x1b[1mb \x1b[0m
     \x1b[36m           │   └  \x1b[0m \x1b[36m \x1b[1m0 \x1b[0m
     \x1b[36m           └  \x1b[0m \x1b[36m \x1b[1m1 \x1b[0m

 \x1b[31m \x1b[1mZeroDivisionError \x1b[0m: \x1b[1m division by zero \x1b[0m
'''


url = f'http://43.142.41.210:8000/ansi2img?ansi_string={a}'
requests.post(url).json()
```


```python
frim loguru import logger
def f(ansi_str):


```
