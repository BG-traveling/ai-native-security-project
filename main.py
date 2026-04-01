from log_manager import save_allowed_ips, load_allowed_ips, clear_logs, add_login_log, print_logs, load_logs, save_logs


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

    allowed_ips = load_allowed_ips()
    
    
    while True:
        print("1.로그 초기화\n2.테스트 함수 실행\n3.로그 출력\n4.로그 직접 입력\n5.허용 IP 추가\n6.허용 IP 목록 보기\n7.종료") 
        
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
            user_id = input("사용자 ID: ")
            ip = input("IP: ")
            target = input("접속 대상: ")
            while True:
                status = input("결과 (Success/Fail): ")
                if status in ["Success", "Fail"]:
                    break
                else:
                    print("결과는 Success 또는 Fail만 입력해주세요.")
            
            add_login_log(log_list, user_id, ip, target, status, allowed_ips)
            save_logs(log_list)
            
            print("로그가 추가되었습니다.")
        elif user_input == 5:
            new_ip = input("추가할 허용 IP: ")
            
            if new_ip in allowed_ips:
                print("이미 등록된 허용 IP입니다.")
            else:
                allowed_ips.append(new_ip)
                save_allowed_ips(allowed_ips)
                print(f"허용 IP가 추가되었습니다.")
                print(f"[추가된 허용 IP: {new_ip}]")
        elif user_input == 6:
            print("[허용 IP 목록]")
            for i, ip in enumerate(allowed_ips, start=1):
                print(f"{i}. {ip}")
        elif user_input == 7:
            save_logs(log_list)
            print("로그를 저장하고 종료합니다.")
            break
        else:
            print("올바른 번호를 입력해주세요.")

if __name__ == "__main__":
    main()

    


    