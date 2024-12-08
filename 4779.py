def calc(list, start, end):
    if end - start == 1:  # 선의 길이가 1이면 더 이상 처리하지 않음
        return
    length = (end - start) // 3  # 현재 구간의 길이를 3등분
    list[start + length:start + 2 * length] = [' '] * length  # 가운데 구간을 공백으로 변경
    calc(list, start, start + length)  # 왼쪽 구간 재귀 처리
    calc(list, start + 2 * length, end)  # 오른쪽 구간 재귀 처리

while True:
    try:
        user_input = input()  # 한 줄 입력받기
        if user_input == "":  # 빈 줄 입력 시 종료
            break
        else:
            try:
                user_input = int(user_input)  # 숫자로 변환
                line_list = ['-'] * (3 ** user_input)  # 길이가 3^N인 리스트 생성
                calc(line_list, 0, len(line_list))  # 칸토어 집합 계산
                print(''.join(line_list))  # 리스트를 문자열로 변환하여 출력
            except ValueError:
                print("숫자를 입력하세요.")  # 숫자가 아닌 경우 예외 처리
    except:
        break