import os, imgkit, boto3
from fastapi import FastAPI
from ansi2html import Ansi2HTMLConverter
from datetime import datetime
from zoneinfo import ZoneInfo
from io import BytesIO
from dotenv import load_dotenv

load_dotenv(dotenv_path='.secrets')
access_key = os.getenv('ACCESS_KEY')
secret_key = os.getenv('SECRET_KEY')
endpoint = os.getenv('ENDPOINT')
bucket = os.getenv('BUCKET')

app = FastAPI()   

@app.post('/ansi2img')
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
