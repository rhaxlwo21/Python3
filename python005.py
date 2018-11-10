#가격
americano_price = 2000
cafelatte_price = 3000
capucino_price = 3500

#판매 수
americanos = int(input("아매리카노 판매 개수: "))
cafelattes = int(input("카페라테 판매 개수: "))
capucinos = int(input("카푸치노 판매 개수: "))

#매출 개산하기
sales = americanos * americano_price
sales = sales + cafelattes * cafelatte_price
sales = sales + capucinos * capucino_price

#출력
print("총 매출은", sales, "입니다.")

#알수있었던 것
#변수활용
