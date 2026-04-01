from log_manager import run_test_logs, add_login_log, print_log, print_logs, load_logs, save_logs

def main():
    log_list = load_logs()

    allowed_ips = [
        "192.168.10.1",
        "192.168.10.2"
    ]
    
    RUN_TEST_LOGS = True
    
    if RUN_TEST_LOGS:
        run_test_logs(log_list, allowed_ips)
        
    print_logs(log_list)
    save_logs(log_list)

if __name__ == "__main__":
    main()

    
# result = detect_excessive_login(log_list, user_id="admin2")
# print(result)


    