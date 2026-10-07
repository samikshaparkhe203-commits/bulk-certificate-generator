from pydantic import BaseModel
from typing import List

class Recipient(BaseModel):
    name: str
    course: str

class CertificateRequest(BaseModel):
    recipients: List[Recipient]
