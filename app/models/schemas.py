from pydantic import BaseModel

class LoginLogRequest(BaseModel):
    user_id: str
    ip: str
    target: str
    status: str
    