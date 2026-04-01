from datetime import datetime, timedelta

# create_login_log 함수 동작 테스트
log_list = []

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
def detect_excessive_login(log_list, user_id):
    now = datetime.now()
    
    count = 0
    
    for log in log_list:
        if log['user_id'] == user_id:
            log_time = datetime.strptime(log["time"], "%Y-%m-%d %H:%M:%S")
            
            if now - log_time <= timedelta(minutes=1):
                count += 1
    if count >= 4:
        return True
    else:
        return False

def add_login_log(log_list, user_id, ip, target, status):
    log_list.append(create_login_log(user_id, ip, target, status))
    if detect_excessive_login(log_list, user_id):
        print("과도한 로그인 요청 감지")
# 로그 출력 확인 테스트용 함수
def log_output(log_list):
    for i, log in enumerate(log_list, start=1):
        print(f"[{i}번 로그]")
        print(f"사용자 ID: {log['user_id']}")
        print(f"IP       : {log['ip']}")
        print(f"대상     : {log['target']}")
        print(f"결과     : {log['status']}")
        print("-" * 30)
        

add_login_log(log_list, "admin", "192.168.10.1", "DB_SERVER_1", "Success")
add_login_log(log_list, "admin2", "192.168.10.2", "DB_SERVER_1", "Success")
add_login_log(log_list, "admin2", "192.168.10.2", "DB_SERVER_1", "Success")
add_login_log(log_list, "admin2", "192.168.10.2", "DB_SERVER_1", "Success")
add_login_log(log_list, "admin2", "192.168.10.2", "DB_SERVER_1", "Success")

log_output(log_list)
    
# result = detect_excessive_login(log_list, user_id="admin2")
# print(result)   