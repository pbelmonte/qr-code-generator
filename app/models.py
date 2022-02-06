from typing import Optional

from fastapi import UploadFile
from pydantic import BaseModel


class QRInfo(BaseModel):
    url: str
    logo: Optional[UploadFile] = None
