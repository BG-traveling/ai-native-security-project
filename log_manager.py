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
multi_log_list = []

login_log = create_login_log(
    user_id="admin",
    ip="192.168.0.10",
    target="DB_SERVER_1",
    status="SUCCESS"
)
multi_log_list.append(login_log)

login_log = create_login_log(
    user_id="user",
    ip="192.168.1.10",
    target="DB_SERVER_1",
    status="SUCCESS"
)
 
multi_log_list.append(login_log)

# print(login_log)
print(multi_log_list)
    
    
