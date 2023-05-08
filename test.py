# print('hello world!')

# import pandas as pd

# df = pd.read_csv('bth.csv', encoding="gbk")
# print(df)

# areas = {'北京':911,'天津':923,'河北':920,'安徽':928,'澳门':934,'重庆':904,'福建':909,'广东':913,'广西':912,'甘肃':925,'贵州':902,'黑龙江':921,'河南':927,'湖南':908,'湖北':906,'海南':930,'吉林':922,'江苏':916,'江西':903,'辽宁':907,'内蒙古':905,'宁夏':919,'青海':918,'上海':910,'四川':914,'山东':901,'山西':929,'陕西':924,'台湾':931,'西藏':932,'香港':933,'新疆':926,'云南':915,'浙江':917}
# # print(list(areas.keys()).index('吉林'))
# # print(areas.items()[16::])
# print(len(areas))

import requests
import sys
import time

word_url = 'http://index.baidu.com/api/SearchApi/thumbnail?area=0&word={}'
headers = {
    'Cipher-Text': '1683381603090_1683465841465_cBL6JPQcXfYJb8GTBNZ7oLh07nimUUJmt9KQ3M5o0yYJjB8ugeggt6ONlReMzjsaz+4VL/W4Q6ojWnHF6MW7LTbY5qSnyttbKOtqUwVrTFRz1G7gLwkYhVz/fBoHdlDVDW19uELBDoWcpzXcS2QCAubDcC0+sKqDdAVh3X5cBOQNFQt1sTrBu7xyjhPzexvGw8XLtEqcpMhIdo3qIIgYxR2eFvBo4uMhpIxtwdR4afc7+F3VwyoqlLCay1PAlNgumc9u4A3Fz8weOYWqpvrGt6Kfu0tjxH4p4joL2uH5A2/qpEmt3OTFrvgWcq76vRFhoyJbTBAKPMRVdikqq8xTnI4fgQ6nODO/QqIx7PHsaUx5lS7fRpnue6nHYtrwQrFDq/gczjDIto3W8ilskoNO4h//ZHl1C+YVOzk0dlULzrS/VqTVMqpvc8YG0MZyhokH',
    'Cookie': 'BIDUPSID=5CB30231196662724CE3F2CD27C1B426; PSTM=1676436503; __bid_n=186bb5846aa41f57414207; ZD_ENTRY=bing; BAIDU_WISE_UID=wapp_1678682422132_128; delPer=0; newlogin=1; ZFY=vXXjBoFWXY:AGM6Y4rwg272B0S4o1PPBZ5mP6ZIP56CY:C; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=1; BCLID=11048300988302959666; BCLID_BFESS=11048300988302959666; BDSFRCVID=DwtOJeC62u-JmG7fbdqyeJRvQpgctV6TH6_nyZt8YtdIV7QI-ftzEG0Paf8g0Ku-HCKLogKKXeOTHiuF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; BDSFRCVID_BFESS=DwtOJeC62u-JmG7fbdqyeJRvQpgctV6TH6_nyZt8YtdIV7QI-ftzEG0Paf8g0Ku-HCKLogKKXeOTHiuF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=JnIj_KK5tCt3qbjkqRQh-JDfqxbXq5jM22OZ0l8KtJT0oMO8y4jvqf4Ibt6N-Dr0b6rCM-omWIQrDl7N-IcA0hKUKfj30jtjXK34KKJxafKWeIJoQxcz5P70hUJiBhv-Ban7B45IXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbC-lejK-D65Xep5BhnIDHDJOQn6j2tI_Hnur3fcrXUI8LNDH2n-fW6-e0qvhQbRqOxoCqJ7zDJD_5RO7tqRXbKo8aRPMaMJaj4P6b-KW-xL1Db3UW6vMtg3l266p-DOoepvoW-oc3Mkt5tjdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjKjLEtbIJoDK5JDD3fP36q45HMt00qxby26nibe39aJ5nQI5nhKIzbb5tqqDs5xoZQJ5zam3ion3vQUbmjRO206oay6O3LlO83h52aC5LKl0MLPbcq-Q2Xh3YBUL10UnMBMnv5mOnanTa3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDFmj58aejv-jaRf-b-XJC5hWbr2HJO_bPOvQMnkbfJBDRK8WfbDKKca0D3l-66HbD3zbhoJ06t7yajd2tv4-g_q2RQGMx3ijnnj-PRpQT8r3fDOK5Oi0mjMhnkbab3vOUnNXpO1MJLzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksDMDtqjDetnke_KIQb-3bKR6Yh47oK-QH-UnLqM3fbgOZ0l8KttKVOR6jjPjDbb_-bt6N-qoj5K7J-DQmWIQrD4TL557Z5-0P3GJIBCrhbTQ4KKJxKRLWeIJo5Dc1LUPThUJiBhv-Ban7B45IXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbRO4-TFMDjjWDf5; H_BDCLCKID_SF_BFESS=JnIj_KK5tCt3qbjkqRQh-JDfqxbXq5jM22OZ0l8KtJT0oMO8y4jvqf4Ibt6N-Dr0b6rCM-omWIQrDl7N-IcA0hKUKfj30jtjXK34KKJxafKWeIJoQxcz5P70hUJiBhv-Ban7B45IXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbC-lejK-D65Xep5BhnIDHDJOQn6j2tI_Hnur3fcrXUI8LNDH2n-fW6-e0qvhQbRqOxoCqJ7zDJD_5RO7tqRXbKo8aRPMaMJaj4P6b-KW-xL1Db3UW6vMtg3l266p-DOoepvoW-oc3Mkt5tjdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjKjLEtbIJoDK5JDD3fP36q45HMt00qxby26nibe39aJ5nQI5nhKIzbb5tqqDs5xoZQJ5zam3ion3vQUbmjRO206oay6O3LlO83h52aC5LKl0MLPbcq-Q2Xh3YBUL10UnMBMnv5mOnanTa3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDFmj58aejv-jaRf-b-XJC5hWbr2HJO_bPOvQMnkbfJBDRK8WfbDKKca0D3l-66HbD3zbhoJ06t7yajd2tv4-g_q2RQGMx3ijnnj-PRpQT8r3fDOK5Oi0mjMhnkbab3vOUnNXpO1MJLzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksDMDtqjDetnke_KIQb-3bKR6Yh47oK-QH-UnLqM3fbgOZ0l8KttKVOR6jjPjDbb_-bt6N-qoj5K7J-DQmWIQrD4TL557Z5-0P3GJIBCrhbTQ4KKJxKRLWeIJo5Dc1LUPThUJiBhv-Ban7B45IXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbRO4-TFMDjjWDf5; BDUSS=m1MSS0zTmtQaW9BbXZVYlVYY3EwR3FpTnhwUWxCOXJkN3VDa2VmQkNEN0RWMnBrRVFBQUFBJCQAAAAAAQAAAAEAAAAJNBQtyP3Uwl9zY3JhcHkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMPKQmTDykJkV; BAIDUID=63A64EC406BCCDDE8E0ACE9CD1BB74B6:FG=1; BAIDUID_BFESS=63A64EC406BCCDDE8E0ACE9CD1BB74B6:FG=1; FPTOKEN=Ljax/CRqkYDuA03lWw40wxNufuI0M7RohtwnYhkupZjYyEPEON9MEaKxw8ZK5O6wOQebmEwHMQAlAL6+paZ4e0GW20UVfRtDrMS76nMq/OhhRaxUOvx+NMtV4qhkRPN/R/BeXwbzzqR1N8fbv/r1eOXnVjkFZOmZ6D5Ahpvxoa7/dO8mYH62zuYGefNsoalRJKJesgKCs5rxKlC+KL5/PFa1jRrhgOvtjix5cT+ByfLAil5E5pnS1hATQzauOmaaei1yAX6qQL9dGtken/jRDuUU8Um4iH9Z9EyiAsMFiMocl4MKllYUhPjXEhxt4rYzip2B/ozltLmoR/VL6JAa+v3Ik+Rew2U6o6jRARLhMNBIenG8nEXz0+nbcJZZDct8/MMe5B35yF1BIXptQJCrZA==|OUBjri5OiUzNpj1GUNazLN6vAdrszvENiWF6FNX9uEI=|10|46f922e432b96d54bb236cdaf67bcc64; H_PS_PSSID=; BDRCVFR[w2jhEs_Zudc]=mbxnW11j9Dfmh7GuZR8mvqV; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1683461176; bdindexid=kqj8sf8hrga4k6l4n05krc8ud2; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a04334736266gRgu4HVJpa9P8EwOOJj8/TXNQBXB3LX3xV91BnkiOzSeXRBIwd6i4yJ/lEYtyijeTDW5DYyG8Z7TgQ9ZSlhPdMuVDLWeDFCfszvlFePzETie7/lIvoOjBasASQSnbZWljIU0oPS4Hn7pUTWqO941WljyBaohAHGRpv15+gpI4SqLZLpdNtZjPpptgV/3yo8t9zMvAlVGVEItp5WKYLTfFs5VF1l6LgcTfEnj2bXz2C6A9wI8fMWvtmnY3472A2ZJKIYUG+UHPy2vsdpCPdZpCmNPg6tVIXhHQTYzdq4d2bM=44335251061930669046019855388032; __cas__rn__=433473626; __cas__st__212=5f8dcc6d39210adbccbb7174bc26d2e713979ed2ebd67014d821ade3b092ea13c1bfc2205b9ca13c19495350; __cas__id__212=45415758; CPID_212=45415758; CPTK_212=347146412; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1683464920; BDUSS_BFESS=m1MSS0zTmtQaW9BbXZVYlVYY3EwR3FpTnhwUWxCOXJkN3VDa2VmQkNEN0RWMnBrRVFBQUFBJCQAAAAAAQAAAAEAAAAJNBQtyP3Uwl9zY3JhcHkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMPKQmTDykJkV; ab_sr=1.0.1_NWY1MTlkZTE2YzA5ZmRkOTVhMTcxY2YyMjA3OTRhODNjZGYyYTYzMjQwMGZiNTRkNjFkYmUwMjM4YzY5ODk0MjhmOTk2MGQ2NTZmYTFkYzc0N2RkMzM3OTM3OTI1NDQ0MTEyZjQ1YmFiOWYyOTVjNGI0MTA5YzhhNGNjZGVkMmJiOTEyZmRlYWNjYTc1ZWRkY2JjMWY4ZmYzZWU3NzA1MQ==; RT="z=1&dm=baidu.com&si=299f6a2c-0c8e-413d-ab6d-208f80e3ee2d&ss=lhddbdmt&sl=c&tt=x0h&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ld=2rz72"',
    'Host': 'index.baidu.com',
    'Referer': 'https://index.baidu.com/v2/main/index.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
    # 'X-Requested-With': 'XMLHttpRequest',
}


def decrypt(t, e):
    n = list(t)
    i = list(e)
    a = {}
    result = []
    ln = int(len(n) / 2)
    start = n[ln:]
    end = n[:ln]
    for j, k in zip(start, end):
        a.update({k: j})
    for j in e:
        result.append(a.get(j))
    return ''.join(result)


def get_ptbk(uniqid):
    url = 'http://index.baidu.com/Interface/ptbk?uniqid={}'
    resp = requests.get(url.format(uniqid), headers=headers)

    if resp.status_code != 200:
        print('获取uniqid失败')
        sys.exit(1)
    return resp.json().get('data')


def get_index_data(keyword, start='2011-02-10', end='2021-08-16'):
    keyword = str(keyword).replace("'", '"')
    # url = f'https://index.baidu.com/api/SearchApi/index?area=0&word=[[%7B%22name%22:%22python%22,%22wordType%22:1%7D]]&days=30'
    url = 'https://index.baidu.com/api/SearchApi/index?area=0&word=[[%7B%22name%22:%22{}%22,%22wordType%22:1%7D]]&startDate=2011-01-02&endDate=2023-05-06'.format(keyword)

    resp = requests.get(url, headers=headers)
    print(resp.json())
    content = resp.json()
    data = content.get('data')
    user_indexes = data.get('userIndexes')[0]
    uniqid = data.get('uniqid')
    ptbk = get_ptbk(uniqid)
    all_data = user_indexes.get('all').get('data')
    result = decrypt(ptbk, all_data)
    result = result.split(',')

    print(result)


get_index_data('金融科技')