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
log_list = []

def add_login_log(log_list, user_id, ip, target, status):
    log_list.append(create_login_log(user_id, ip, target, status))
    return 

add_login_log(log_list, "admin", "192.168.10.1", "DB_SERVER_1", "Success")
add_login_log(log_list, "admin2", "192.168.10.2", "DB_SERVER_1", "Success")

# 로그 출력 확인 테스트용 함수
# def log_output(log_list):
#     for i, log in enumerate(log_list, start=1):
#         print(f"[{i}번 로그]")
#         print(f"사용자 ID: {log['user_id']}")
#         print(f"IP       : {log['ip']}")
#         print(f"대상     : {log['target']}")
#         print(f"결과     : {log['status']}")
#         print("-" * 30)
        
# log_output(log_list)