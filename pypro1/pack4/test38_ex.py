'''
우편번호 data 파일 사용
키보드로 동이름을 입력해서 해당 동이름의 자료만 읽기 

https://cafe.daum.net/flowlife/9A8Q/136
'''

try:
    dong = input('동이름 입력 :')
    # dong = '개포'
    # print(dong)
    
    with open(r'zipcode.txt', 'r', encoding = 'euc-kr') as f: # 한국어 텍스트를 나타내는 가변 너비 인코딩
        line = f.readline() # 한줄 읽기
        # print(line)
        
        while line: # 자료가 있으면 ture
            # lines = line.split('\t') # 탭을 기준으로 자르기
            lines = line.split(chr(9)) # 아스키 코드값으로 처리하기
            
            # print(lines) 
        
            if lines[3].startswith(dong): # startswith : 문자열이 지정된 문자열로 시작하는 경우 true를 반환
                print('[' + lines[0] + '] ' + lines[1] + ' ' + \
                      lines[2] + ' ' + lines[3] + ' ' + lines[4])
                
            line = f.readline()
    
except Exception as e:
    print('err : ', e)

















