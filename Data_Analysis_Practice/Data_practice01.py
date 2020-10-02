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
#결과값 :
#2018년 1월 1일: Will be leaving Florida for Washington (D.C.) today at 4:00 P.M. Much work to be done, but it will be a great New Year!
#2018년 1월 2일: Companies are giving big bonuses to their workers because of the Tax Cut Bill. Really great!
#2018년 1월 3일: MAKE AMERICA GREAT AGAIN!


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
        
#결과를 확인해보세요.  
print_korea(trump_tweets)
#결과값: korea


################################################################


#Practice 03. 문자열 함수 : .startswith()
#데이터 분석에 응용하기 : 단어의 첫 글자 확인하기
#startswith() 메소드를 이용하면 단어가 특정 문자열로 시작하는지 쉽게 확인할 수 있습니다.

# 트럼프 대통령 트윗을 공백 기준으로 분리한 리스트입니다. 수정하지 마세요.
trump_tweets = ['thank', 'you', 'to', 'president', 'moon', 'of', 'south', 'korea', 'for', 'the', 'beautiful', 'welcoming', 'ceremony', 'it', 'will', 'always', 'be', 'remembered']

#해시태그와 멘션을 찾기 위서는 문자열이 # 또는 @로 시작하는지 확인해야 합니다.
#startswith() 메소드를 사용하여 앞서 인덱싱을 이용해 작성한 print_korea() 함수를 다시 작성하세요.

def print_korea2(tweet):
    for text in tweet:
        if text.startswith('k'):
            print(text)
    
#결과를 확인해보세요.  
print_korea2(trump_tweets)
#결과값: korea


################################################################


# Practice 04. 문자열 함수 : .split()
# 데이터 분석에 응용하기 : 문장을 단어 단위로 구분하기
# split() 메소드는 특정 문자를 기준으로 문자열을 분리합니다. 입력값을 넣지 않을 경우 공백을 기준으로 분리합니다. 분리된 문자열은 리스트의 원소로 저장됩니다.

# 트윗에 사용된 단어를 하나씩 살펴보기 위해서는 문자열을 리스트로 변환해야 합니다.
# trump_tweet을 공백을 기준으로 분리하고 리스트형으로 반환하는 break_into_words() 함수를 수정하세요. 

trump_tweets = "thank you to president moon of south korea for the beautiful welcoming ceremony it will always be remembered"

def break_into_words(text):
    words = text.split()
    return words

# 결과를 확인해보세요.  
print(break_into_words(trump_tweets))
# 결과값: ['thank', 'you', 'to', 'president', 'moon', 'of', 'south', 'korea', 'for', 'the', 'beautiful', 'welcoming', 'ceremony', 'it', 'will', 'always', 'be', 'remembered']


################################################################


# Practice 05. 리스트 함수 : .append()
# 데이터 분석에 응용하기 : 새로운 단어 추가하기
# append()는 리스트를 다룰 때 사용되는 가장 기본적인 메소드로, 리스트의 맨 마지막에 새로운 요소를 추가합니다.

trump_tweets = ['america', 'is', 'back', 'and', 'we', 'are', 'coming', 'back', 'bigger', 'and', 'better', 'and', 'stronger', 'than', 'ever', 'before']

# trump_tweets 리스트에서 b로 시작하는 요소를 빈 리스트 new_list에 저장하는 make_new_list() 함수를 수정하세요.
def make_new_list(text):
    
    new_list = []
    
    for word in text:
        if word.startswith('b'):
            new_list.append(word)
    return new_list


# 결과를 확인해보세요.  
new_list = make_new_list(trump_tweets)
print(new_list)
# 결과값: ['back', 'back', 'bigger', 'better', 'before']


################################################################


# Practice 06. 문자열 함수 : .lower(), .upper()
# 데이터 분석에 응용하기 : 대소문자 변환하기
# lower(), upper() 메소드를 이용하면 문자열을 쉽게 소문자 또는 대문자로 변환할 수 있습니다

# 가짜 뉴스를 뜻하는 Fake News는 트럼프 대통령이 가장 자주 사용하는 말 중 하나입니다.
# FAKE NEWS, Fake News는 대소문자가 다르기 때문에 두 단어가 몇 번 사용되었는지 정확하게 확인하기 위해서는 모두 소문자로 변환해야 합니다.
# trump_tweets 리스트의 문자열 요소를 모두 소문자로 변환하는 lowercase_all_characters() 함수를 완성하세요.

trump_tweets = [
    "FAKE NEWS - A TOTAL POLITICAL WITCH HUNT!",
    "Any negative polls are fake news, just like the CNN, ABC, NBC polls in the election.",
    "The Fake News media is officially out of control.",
]
 
def lowercase_all_characters(text):
    processed_text = []
    for sentence in text:
        lower_sentence = sentence.lower()
        processed_text.append(lower_sentence)
    return processed_text


# 결과를 확인해보세요.  
print('\n'.join(lowercase_all_characters(trump_tweets)))
# 결과값:
# fake news - a total political witch hunt!
# any negative polls are fake news, just like the cnn, abc, nbc polls in the election.
# the fake news media is officially out of control.


################################################################


# Practice 07. 문자열 함수 : .replace()
# 데이터 분석에 응용하기 : 특수기호 삭제하기
# replace() 메소드는 문자열에서 특정 문자나 문자열을 다른 문자(열)로 변경할 때 사용됩니다.
# replace()는 변경하고 싶은 문자열을 첫번째 입력값으로, 대체할 문자열을 두번째 입력값으로 받습니다.

# 소문자로 변환된 trump_tweets의 트윗을 공백을 기준으로 구분할 경우 christmas', christmas,, christmas!!!가 생성되기 때문에
# christmas가 몇 번 사용되었는지 정확하게 확인하기 위해서는 특수문자를 제거해야 합니다.
# trump_tweets 리스트의 문자열 요소에서 쉼표, 작은따옴표, 느낌표를 제거하는 remove_special_characters() 함수를 완성하세요.

trump_tweets = [
    "i hope everyone is having a great christmas, then tomorrow it’s back to work in order to make america great again.",
    "7 of 10 americans prefer 'merry christmas' over 'happy holidays'.",
    "merry christmas!!!",
]

def remove_special_characters(text):
    processed_text = []
    for sentence in text:
        replace_sentence = sentence.replace(',','').replace("'",'').replace("!",'')
        processed_text.append(replace_sentence)
    return processed_text


# 아래 주석을 해제하고 결과를 확인해보세요.  
print('\n'.join(remove_special_characters(trump_tweets)))
# 결과값:
# i hope everyone is having a great christmas then tomorrow it’s back to work in order to make america great again.
# 7 of 10 americans prefer merry christmas over happy holidays.
# merry christmas


################################################################


