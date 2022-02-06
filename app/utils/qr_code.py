import io
from typing import Optional

from PIL import Image
import qrcode


def generate_qr_img(url: str, logo_img: Optional[Image.Image]) -> bytes:
    QRcode = qrcode.QRCode(
        version=10,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
    )
    QRcode.add_data(url)
    QRcode.make()
    QRimg = QRcode.make_image().convert("RGB")

    if logo_img:
        # adjust image size
        basewidth = 240
        wpercent = basewidth / float(logo_img.size[0])
        hsize = int((float(logo_img.size[1]) * float(wpercent)))
        logo_img = logo_img.resize((basewidth, hsize), Image.ANTIALIAS)

        pos = (
            (QRimg.size[0] - logo_img.size[0]) // 2,
            (QRimg.size[1] - logo_img.size[1]) // 2,
        )
        QRimg.paste(logo_img, pos)

    buffered = io.BytesIO()
    QRimg.save(buffered, format="PNG")
    return buffered.getvalue()
