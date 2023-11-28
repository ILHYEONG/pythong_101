# input은 콘솔에 유저가 입력한 값을 받는 함수

#newjeans_song = input("뉴진스 중에 좋아하는 노래 뭐임?")
#bangtan_song = input("방탄 노래중 좋아하는 노래는?")
#print(f"너가 좋아하는 뉴진스 노래는 {newjeans_song}이고 방탄선호곡은 {bangtan_song}이구나")

name = input("성함이 무엇입니까 ?")
age = input("당신의 나이는?")

first = input("외향입니까? 내향입니까? (E 또는 I 입력)")
second = input("직관적입니까? 감각적입니까? (N 또는 S 입력)")
third = input("너 감성적입니까? 비인간적입니까 (F 또는 T 입력)")
fourth = input("즉흥적입니까? 계획적입니까? (P 또는 J 입력)")
print(f"{age}세인 {name}님의 MBTI는 {first}{second}{third}{fourth}이군요")

