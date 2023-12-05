a=len("""이 소장은 이날 오후 서울 종로구 헌법재판소에서 열린 취임식에서 "먼 미래를 내다보고 헌법재판소가 새로운 도약을 할 수 있는 발판 하나를 마련하는 것이 제게 주어진 소명"이라며 이같이 말했다.

이 소장의 임기는 헌법재판관 임기가 종료되는 2024년 10월까지다.

그는 "헌법재판소는 창립 이래 줄곧 정치적 중리에 기초하여 재판의 독립""")

print(f"이 기사의 글자 수는 {a}입니다.")

article ="""A Korean frozen gimbap product, which created a huge buzz in the US organic market, is now making its domestic debut.

According to E-mart 24, E-mart's convenience store chain, on Friday, it has stocked Baba Gimbap’s frozen gimbap product for a two-week special sale.

Created by Korean food firm Allgot, the supplier behind the Trader Joe’s hit rice rolls, the gimbap is rapid frozen at minus 50 degree Celsius so that it retains the shape and texture of a freshly wrapped roll during microwaving, E-mart officials explained.

Priced at 1980 won ($1.5), the frozen gimbap requires two to three minutes of cooking time in a microwave.
"""


print(article.join(['start','end']))