# Python3 샘플 코드 #
import pandas as pd
import xmltodict
import requests

# 'pageNo' : '26'까지
url = 'http://apis.data.go.kr/1360000/TourStnInfoService/getTourStnVilageFcst'
params ={'serviceKey' : '4hfjQRMp3NUakGj6w+fTuBIKpB9zdwnZ8QzwME1OsMTNrC+d79ChoOLJiyiez+WQpuLu+vsog4mAh3J1aMTrng==', 'pageNo' : '1', 'numOfRows' : '10', 'dataType' : 'XML', 'CURRENT_DATE' : '2019122010', 'HOUR' : '24', 'COURSE_ID' : '1' }

# response = requests.get(url, params=params)
# print(response.content)


resp = requests.get(url, params=params)
print(resp.content.decode('utf-8'))
print()
data = xmltodict.parse(resp.content.decode('utf-8'))
print(data)
print()
print(data['response']['body']['items']['item'])
print()
print(pd.DataFrame(data['response']['body']['items']['item']))



# import requests
# import xmltodict
# import pandas as pd
#
# # http://apis.data.go.kr/1360000/TourStnInfoService
# # 4hfjQRMp3NUakGj6w+fTuBIKpB9zdwnZ8QzwME1OsMTNrC+d79ChoOLJiyiez+WQpuLu+vsog4mAh3J1aMTrng==
# url = 'http://apis.data.go.kr/1360000/TourStnInfoService'
# params ={'serviceKey' : '4hfjQRMp3NUakGj6w+fTuBIKpB9zdwnZ8QzwME1OsMTNrC+d79ChoOLJiyiez+WQpuLu+vsog4mAh3J1aMTrng==', 'pageNo' : '1', 'numOfRows' : '10', 'dataType' : 'XML', 'CURRENT_DATE' : '2019122010', 'HOUR' : '24', 'COURSE_ID' : '1'}
#
# resp = requests.get(url, params=params)
# print(resp.content.decode('utf-8'))
# print()
# data = xmltodict.parse(resp.content.decode('utf-8'))
# print(data)
# print()
# print(data['response']['body']['items']['item'])
# print()
# print(pd.DataFrame(data['response']['body']['items']['item']))







