'''
2023.06.03
장준혁
사용자 정의 함수 만들기
'''

def print_address(): # print_address라는 함수 정의
    print("부산광역시")
    print("사상구 괘법동")
    print("신라대학교")
    
print_address() #함수 호출

def person():
    print("이름:장준혁(jjh)")
    print("나이:15살")
    print("학교:해연(haeyeon)중학교")
    
person()

def print_address(name): # print_address라는 함수 정의 / name은 매개변수
    print("부산광역시")
    print("사상구 괘법동")
    print("신라대학교")
    print(name) #전달받은 name에 값을 출력
    
print_address("장준혁")
