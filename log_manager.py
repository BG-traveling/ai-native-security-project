from datetime import datetime

def create_login_log(user_id, ip, target, status):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    login_log = {
        "user_id": user_id,
        "ip": ip,
        "target": target,
        "status": status,
        "time": now
    }
    
    return login_log

# create_login_log 함수 동작 테스트
login_log = create_login_log(
    user_id="admin",
    ip="192.168.0.10",
    target="DB_SERVER_1",
    status="SUCCESS"
)

print(login_log)
    
    
