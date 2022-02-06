from io import BytesIO

from PIL import Image
from fastapi import FastAPI, Response

from app.models import QRInfo
from app.utils.qr_code import generate_qr_img

app = FastAPI()


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
