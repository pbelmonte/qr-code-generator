from io import BytesIO
from typing import Optional

from PIL import Image
from fastapi import FastAPI, Response, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from app.utils.qr_code import generate_qr_img


app = FastAPI(
    title='QRCodeGenerator',
    description='Given an url and logo (optional), generates a QR code',
    version='0.0.1',
    license_info={
        'name': 'Apache 2.0',
        'url': 'https://www.apache.org/licenses/LICENSE-2.0.html',
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.post(
    '/generate-qr-code',
    responses={200: {'content': {'image/png': {}}}},
    response_class=Response,
)
async def generate_qr_code(url: str = Form(...), logo: Optional[UploadFile] = None) -> Response:
    if logo:
        request_object_content = await logo.read()
        logo = Image.open(BytesIO(request_object_content))

    result_qr = generate_qr_img(url, logo)

    return Response(content=result_qr, media_type='image/png')
