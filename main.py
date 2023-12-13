import os, imgkit, boto3
from fastapi import FastAPI
from ansi2html import Ansi2HTMLConverter
from datetime import datetime
from zoneinfo import ZoneInfo
from io import BytesIO
from dotenv import load_dotenv

import yagmail

load_dotenv(dotenv_path='.secrets')
access_key = os.getenv('ACCESS_KEY')
secret_key = os.getenv('SECRET_KEY')
endpoint = os.getenv('ENDPOINT')
bucket = os.getenv('BUCKET')

app = FastAPI()   

@app.post('/v1/ansi2img')
def ansi2img(ansi_string: str):
    conv = Ansi2HTMLConverter(dark_bg=False) 
    html = conv.convert(ansi_string)
    filename = datetime.now(ZoneInfo("Asia/Shanghai")).strftime('%Y-%m-%d_%H:%M:%S.png')
    image_bytes = imgkit.from_string(html, False, options={'format': 'png', 'encoding': 'utf-8', "quality": 100})
    fixed_image_bytes = image_bytes[image_bytes.find(b'\x89PNG\r\n'):]
    buffer = BytesIO(fixed_image_bytes)
    s3_resource = boto3.resource(
        "s3",
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        endpoint_url=endpoint
    )
    s3_resource.Object(bucket, filename).put(Body=buffer.getvalue())
    return f'{endpoint}/{bucket}/{filename}'


import markdown
from pydantic import BaseModel

email_address = os.getenv('EMAIL_ADDRESS')
email_password = os.getenv('EMAIL_PASSWORD')

class Mail(BaseModel):
    to: str
    title: str
    markdown: bool = True
    contents: str

@app.post('/v1/sendmail')
def sendmail(mail: Mail):
    yag = yagmail.SMTP(
        email_address, 
        email_password, 
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


