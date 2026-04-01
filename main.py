from log_manager import add_login_log, print_log, print_logs

log_list = []

allowed_ips = [
    "192.168.10.1",
    "192.168.10.2"
]

# 테스트
add_login_log(log_list, "admin", "192.168.10.1", "DB_SERVER_1", "Success", allowed_ips)
add_login_log(log_list, "admin2", "192.168.10.2", "DB_SERVER_1", "Success", allowed_ips)
add_login_log(log_list, "admin2", "192.168.10.2", "DB_SERVER_1", "Success", allowed_ips)
add_login_log(log_list, "admin2", "192.168.10.2", "DB_SERVER_1", "Success", allowed_ips)
add_login_log(log_list, "admin2", "192.168.10.2", "DB_SERVER_1", "Success", allowed_ips)
add_login_log(log_list, "admin3", "192.168.10.4", "DB_SERVER_1", "Success", allowed_ips)

print_logs(log_list)
print_log(log_list[0])
    
# result = detect_excessive_login(log_list, user_id="admin2")
# print(result)