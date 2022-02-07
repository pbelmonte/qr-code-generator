from io import BytesIO

from PIL import Image
from fastapi import FastAPI, Response

from app.models import QRInfo
from app.utils.qr_code import generate_qr_img


app = FastAPI(
    title="QRCodeGenerator",
    description='Given an url and logo (optional), generates a QR code',
    version="0.0.1",
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


@app.post(
    "/generate-qr-code",
    responses={200: {"content": {"image/png": {}}}},
    response_class=Response,
)
async def generate_qr_code(qrinfo: QRInfo) -> Response:
    logo = qrinfo.logo
    if logo:
        request_object_content = await logo.read()
        logo = Image.open(BytesIO(request_object_content))

    result_qr = generate_qr_img(qrinfo.url, logo)

    return Response(content=result_qr, media_type="image/png")
