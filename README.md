# ansi2img

把报错转为图像地址，可以继续发送给钉钉(微信 QQ没试过)

##
```bash
sudo apt-get install wkhtmltopdf
pip install ansi2html imgkit boto3 fastapi uvicorn python-dotenv

git clone git@github.com:liuhetian/ansi2img.git
vi .secrets  # 写密码
uvicorn main:app --reload
```
