import os, imgkit, boto3
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
# from fastapi.middleware.cors import CORSMiddleware
from ansi2html import Ansi2HTMLConverter
from datetime import datetime
from zoneinfo import ZoneInfo
from io import BytesIO
from dotenv import load_dotenv
from pydantic import BaseModel

import yagmail

load_dotenv()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # 允许所有域名跨域，生产环境应该修改为实际的域名
#     allow_credentials=True,
#     allow_methods=["*"],  # 允许所有方法
#     allow_headers=["*"],  # 允许所有头部
# )

class Ansi(BaseModel):
    ansi_string: str
    to_boto: bool=False
    
@app.post('/v1/ansi2img')
def ansi2img(ansi_string: Ansi):
    conv = Ansi2HTMLConverter(dark_bg=False) 
    html = conv.convert(ansi_string.ansi_string)
    filename = datetime.now(ZoneInfo("Asia/Shanghai")).strftime('%Y-%m-%d_%H:%M:%S.png')

    if ansi_string.to_boto:  # 可以使用对象储存
        endpoint = os.getenv('ENDPOINT')
        bucket = os.getenv('BUCKET')
        image_bytes = imgkit.from_string(html, False, options={'format': 'png', 'encoding': 'utf-8', "quality": 100})
        fixed_image_bytes = image_bytes[image_bytes.find(b'\x89PNG\r\n'):]
        buffer = BytesIO(fixed_image_bytes)
        s3_resource = boto3.resource(
            "s3",
            aws_access_key_id=os.getenv('ACCESS_KEY'),
            aws_secret_access_key=os.getenv('SECRET_KEY'),
            endpoint_url=endpoint
        )
        s3_resource.Object(bucket, filename).put(Body=buffer.getvalue())
        return f'{endpoint}/{bucket}/{filename}'
    else:
        imgkit.from_string(html, f'static/{filename}', options={'format': 'png', 'encoding': 'utf-8', "quality": 100})
        return f'http://api.liuhetian.work/static/{filename}'


import markdown

class Mail(BaseModel):
    to: str
    title: str
    markdown: bool = True
    contents: str

@app.post('/v1/sendmail')
def sendmail(mail: Mail):
    try:
        yag = yagmail.SMTP(
            os.getenv('EMAIL_ADDRESS'), 
            os.getenv('EMAIL_PASSWORD'), 
            host='smtp.qq.com', 
            timeout=30
        )
        if mail.markdown:
            mail.contents = markdown.markdown(mail.contents)
        return yag.send(
            to=mail.to,
            subject=mail.title,
            contents=mail.contents
        )
    except:
        return '发送失败'



