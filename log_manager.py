from datetime import datetime, timedelta
import json

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

def detect_unallowed_ip(ip, allowed_ips):
    return ip not in allowed_ips
    
def add_login_log(log_list, user_id, ip, target, status, allowed_ips):
    log_list.append(create_login_log(user_id, ip, target, status))
    if detect_excessive_login(log_list, user_id):
        print(f"[경고] 사용자 {user_id}의 과도한 로그인 요청 감지")
        
    if detect_unallowed_ip(ip, allowed_ips):
        print(f"[경고] 허용되지 않은 IP 접근 감지 - 사용자: {user_id}, IP: {ip}")
        
    
# 로그 출력 확인 테스트용 함수
def print_logs(log_list):
    if not log_list:
        print("출력할 로그가 없습니다.")
        return
    
    for i, log in enumerate(log_list, start=1):
        print(f"[{i}번 로그]")
        print_log(log)
        # print(f"시간: {log['time']}")
        # print(f"사용자 ID: {log['user_id']}")
        # print(f"IP       : {log['ip']}")
        # print(f"대상     : {log['target']}")
        # print(f"결과     : {log['status']}")
        # print("-" * 30)
        

def print_log(log):
    print(f"시간      : {log['time']}")
    print(f"사용자 ID : {log['user_id']}")
    print(f"IP        : {log['ip']}")
    print(f"대상      : {log['target']}")
    print(f"결과      : {log['status']}")
    print("-" * 30)
    
# 로그 저장 함수
def save_logs(log_list):
    with open("logs.json", "w", encoding="utf-8") as f:
        json.dump(log_list, f,ensure_ascii=False, indent=2)
    
    

# 로그 불러오기 함수    
def load_logs():
    try:
        with open("logs.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_allowed_ips(allowed_ips):
    with open("allowed_ips.json", "w", encoding="utf-8") as f:
        json.dump(allowed_ips, f, ensure_ascii=False, indent=2)
        
def load_allowed_ips():
    try:
        with open("allowed_ips.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return [
            "192.168.10.1",
            "192.168.10.2"
        ]

# 로그 파일 초기화 함수
def clear_logs():
    with open("logs.json", "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=2)
        
def is_valid_ip(ip):
    parts = ip.split(".")
    
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part.isdigit():
            return False
        
        number = int(part)
        if number < 0 or number > 255:
            return False
        
    return True