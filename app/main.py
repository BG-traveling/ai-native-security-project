from fastapi import FastAPI
from app.services.log_service import load_logs, load_allowed_ips, save_logs, add_login_log
from app.models.schemas import LoginLogRequest

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI 서버가 정상적으로 실행 중입니다."}

@app.get("/logs")
def get_logs():
    return load_logs()

@app.get("/allowed-ips")
def get_allowed_ips():
    return load_allowed_ips()

@app.post("/logs")
def create_log(log: LoginLogRequest):
    log_list = load_logs()
    allowed_ips = load_allowed_ips()
    
    add_login_log(
        log_list=log_list,
        user_id=log.user_id,
        ip=log.ip,
        target=log.target,
        status=log.status,
        allowed_ips=allowed_ips
    )
    
    save_logs(log_list)
    
    return {
        "message": "로그가 추가되었습니다.",
        "log": log_list[-1]
    }