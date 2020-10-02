# Practice 01. 리스트 순회하기
# 리스트에 있는 문장을 하나씩 가져와보자
# for 반복문에 in 키워드를 이용하면 리스트의 원소를 하나씩 가져와 변수에 저장할 수 있습니다.
# 여기에 리스트의 길이를 구하는 len()와, 연속된 정수를 만들어주는 range() 함수를 함께 사용하면 원소의 인덱스를 가져올 수 있습니다.

# 트럼프 대통령의 1월 1~3일 트윗을 각각 리스트의 원소로 저장합니다.
trump_tweets = [
    'Will be leaving Florida for Washington (D.C.) today at 4:00 P.M. Much work to be done, but it will be a great New Year!',
    'Companies are giving big bonuses to their workers because of the Tax Cut Bill. Really great!',
    'MAKE AMERICA GREAT AGAIN!'
]

# 데이터 분석에 응용하기
# lower(), replace() 등 다양한 메소드를 이용해 트럼프 대통령의 트윗을 정제하기 위해선 먼저 리스트에 담긴 요소를 하나씩 가져와야 합니다.

# trump_tweets 리스트의 문자열 요소를 하나씩 가져와서 트윗 게시일과 함께 출력하는 date_tweet 함수를 살펴보고, 실행·제출해보세요.
def date_tweet(i):

# index에 0~2을 차례대로 저장하여 반복문을 실행합니다.
    for index in range(len(i)):
        print("2018년 " + "1월 " + str(index+1) + "일: " + i[index])

# 실행 결과를 확인하기 위한 코드입니다.
date_tweet(trump_tweets)



################################################################



# Practice 02. 문자열 인덱싱
# 데이터 분석에 응용하기 : 단어의 일부분 가져오기
# 인덱스를 이용하면 문자열 또는 리스트의 특정 요소에 접근할 수 있습니다. 인덱스는 0부터 시작하며 -1은 맨 마지막 문자 또는 요소를 가리킵니다.
# 시작 인덱스와 끝 인덱스를 이용하면 특정 구간의 요소를 리스트형으로 접근할 수 있습니다. 끝 인덱스를 생략하면 시작 인덱스부터 마지막 요소까지 접근합니다.

# 문자열로 이루어진 text 리스트에서 k로 시작하는 문자열을 하나씩 출력하는 print_korea() 함수를 완성하세요.
trump_tweets = ['thank', 'you', 'to', 'president', 'moon', 'of', 'south', 'korea', 'for', 'the', 'beautiful', 'welcoming', 'ceremony', 'it', 'will', 'always', 'be', 'remembered']

def print_korea(text):
    # 아래 코드를 작성하세요.
    # for i in range(len(text)):
    #     if text[i][0] == 'k':
    #         print(text[i])

    #simple version
    for word in text:
        if word[0] == 'k':
            print(word)
        
# 결과를 확인해보세요.  
print_korea(trump_tweets)