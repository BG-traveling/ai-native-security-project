from log_manager import clear_logs, add_login_log, print_logs, load_logs, save_logs


# 실행 테스트 함수
def run_test_logs(log_list, allowed_ips):
    add_login_log(log_list, "admin", "192.168.10.1", "DB_SERVER_1", "Success", allowed_ips)
    add_login_log(log_list, "admin2", "192.168.10.2", "DB_SERVER_1", "Success", allowed_ips)
    add_login_log(log_list, "admin2", "192.168.10.2", "DB_SERVER_1", "Success", allowed_ips)
    add_login_log(log_list, "admin2", "192.168.10.2", "DB_SERVER_1", "Success", allowed_ips)
    add_login_log(log_list, "admin2", "192.168.10.2", "DB_SERVER_1", "Success", allowed_ips)
    add_login_log(log_list, "admin3", "192.168.10.4", "DB_SERVER_1", "Success", allowed_ips)

def main():
    log_list = load_logs()

    allowed_ips = [
        "192.168.10.1",
        "192.168.10.2"
    ]
    
    
    while True:
        print("1.로그 초기화\n2.테스트 함수 실행\n3.로그 출력\n4.종료") 
        
        try:
            user_input = int(input("입력: "))
        except ValueError:
            print("숫자만 입력해주세요! [ValueError!]")
            continue
        
        if user_input == 1:
            clear_logs()
            log_list = []
            print("로그를 초기화 하였습니다.")
        elif user_input == 2:
            run_test_logs(log_list, allowed_ips)
            save_logs(log_list)
            print("테스트 로그를 추가했습니다.")
        elif user_input == 3:
            print("[로그 출력]")
            print("=" * 30)
            print_logs(log_list)
        elif user_input == 4:
            save_logs(log_list)
            print("로그를 저장하고 종료합니다.")
            break
        else:
            print("올바른 번호를 입력해주세요.")

if __name__ == "__main__":
    main()

    


    