섭씨 온도 3개 평균 반환 함수
def avg_celsius(t1, t2, t3):
    return (t1 + t2 + t3) / 3

# 최소 3회 호출
print(avg_celsius(10, 20, 30))  # 20.0
print(avg_celsius(0, 5, 10))    # 5.0
print(avg_celsius(-5, 5, 15))   # 5.0

이름 + 좋아하는 언어 2개 출력 함수
def print_fav_lang(name, lang1, lang2):
    print(f"{name}님의 선호 언어는 {lang1}, {lang2} 입니다.")

# 최소 3회 호출
print_fav_lang("홍길동", "Python", "Java")
print_fav_lang("이율비", "JavaScript", "Python")
print_fav_lang("김철수", "C", "Go")

점수 리스트에서 60점 이상만 합산하는 함수
def sum_pass_scores(scores):
    total = 0
    for s in scores:
        if s >= 60:
            total += s
    return total

# 최소 3회 호출
print(sum_pass_scores([50, 60, 70]))       # 130
print(sum_pass_scores([100, 20, 30, 90]))  # 190
print(sum_pass_scores([59, 58, 57]))       # 0

문자열 두 개를 이어 붙이는 함수
def combine(str1, str2):
    return str1 + str2

# 최소 3회 호출
print(combine("안녕", "하세요"))         # 안녕하세요
print(combine("율빛", "힐링센터"))        # 율빛힐링센터
print(combine("GREEUM ", "PDRN"))        # GREEUM PDRN


온도 리스트 → 모두 섭씨로 변환하여 새 리스트 반환(Celsius = (F - 32) / 1.8)
def to_celsius_list(temp_list):
    result = []
    for f in temp_list:
        c = (f - 32) / 1.8
        result.append(c)
    return result

# 최소 3회 호출
print(to_celsius_list([32, 50, 68]))       # [0.0, 10.0, 20.0]
print(to_celsius_list([77, 86, 95]))       # [25.0, 30.0, 35.0]
print(to_celsius_list([104, 122]))         # [40.0, 50.0]
