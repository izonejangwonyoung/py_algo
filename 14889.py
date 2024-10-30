def calculate_team_ability(team):
    """팀의 능력치를 계산하는 함수"""
    ability = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            ability += row[team[i]][team[j]] + row[team[j]][team[i]]
    return ability
def dfs(index,start_team):
    global min_diff
    if len(start_team)==N//2:
        link_team = [i for i in range(N) if i not in start_team]

        start_ability=calculate_team_ability(start_team)
        link_ability=calculate_team_ability(link_team)
        min_diff=min(min_diff,abs(link_ability-start_ability))
        return
    for i in range(index,N):
        if i not in start_team:
            start_team.append(i)
            dfs(i + 1, start_team)  # 다음 인덱스부터 시작하여 중복을 피함
            start_team.pop()
test = []
min_diff = float('inf')  # 능력치 차이의 최소값을 저장할 변수

N = int(input())
row=[list(map(int, input().split())) for _ in range(N)]


# 결과 출력 확인
dfs(0,[])
print(min_diff)

