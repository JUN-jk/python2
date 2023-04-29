'''
2023.04.29
장준혁
조건문 연습 - if, if else
#문제 정의
    입력받은 성적이 90이상이면 "합격",아니면 "불합격"을 출력
#문제 분석
    변수: 성적(score)
#알고리즘
    1.변수 선언
        score에 점수 정수로 입력
    2.프로그램 논리(선택:if else)
        (조건식) if score>=90:   
'''

score=int(input("점수입력:")) # 점수 정수로 입력
if score>=90: # 조건식
    print("합격") # 조건식 참 일때   
else:
    print("불합격") # 조건식 거짓 일때 실행
print("수고하셨습니다.") # 조건과 관계 없이 실행