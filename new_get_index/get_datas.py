import requests, sys, time, random,jsonpath,json
# import json,execjs,
import pandas as pd
from os.path import exists
from os import makedirs
# from fake_useragent import UserAgent
from urllib.request import quote

RESULTS_DIR = './new_get_index/results'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

# word_url = 'http://index.baidu.com/api/SearchApi/thumbnail?area=0&word={}'
headers = {
    'Cipher-Text': '1683468014403_1683518285561_JcZ4oGFjhq/k+CPu5FORPY6XKJvL8lSMGNQu3MAGqzaGfVpMeE6Ur1D6/Ved4Ozk8/2+I/Ao0RzngavIdjnxHKX1q9sjIJ75BjC+nTHmgnZzUjgTDZB8M2qLquSIyIcny4ZGtNC5vRhWA2cRrAW77gMeCcOgm/KOayrCzXcYL/grGeS5IyehtuemC1yIOci73HvMaHK+jmQ70J+WC0WrLrfUqkg2MyDh45MI0sf6TnyJP5iBbdP+o0QQrDHskQrEFwRnyJ1XLlQdEU8CkXEiHdB0tSpyHqiBaMZp5hJzUEh1C2C4UxzbtDzoSrUhPoO3mxVTVaZjbLwDA2ezPvaixmQdIX7JCOLzWEVWjd8lFIIXo3p96uiLm7ljk7jKCni1yL02QvuV9Pzzyd9AaxFQqXej9zYx2oWLh7E1VJOdGYWpGCKMH1OesgMlJuK0ToVZ6GDW8GDHBOjTLHtQYrJdfg==',
    'Cookie': 'BIDUPSID=5CB30231196662724CE3F2CD27C1B426; PSTM=1676436503; __bid_n=186bb5846aa41f57414207; ZD_ENTRY=bing; BAIDU_WISE_UID=wapp_1678682422132_128; delPer=0; newlogin=1; ZFY=vXXjBoFWXY:AGM6Y4rwg272B0S4o1PPBZ5mP6ZIP56CY:C; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=1; BCLID=11048300988302959666; BCLID_BFESS=11048300988302959666; BDSFRCVID=DwtOJeC62u-JmG7fbdqyeJRvQpgctV6TH6_nyZt8YtdIV7QI-ftzEG0Paf8g0Ku-HCKLogKKXeOTHiuF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; BDSFRCVID_BFESS=DwtOJeC62u-JmG7fbdqyeJRvQpgctV6TH6_nyZt8YtdIV7QI-ftzEG0Paf8g0Ku-HCKLogKKXeOTHiuF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=JnIj_KK5tCt3qbjkqRQh-JDfqxbXq5jM22OZ0l8KtJT0oMO8y4jvqf4Ibt6N-Dr0b6rCM-omWIQrDl7N-IcA0hKUKfj30jtjXK34KKJxafKWeIJoQxcz5P70hUJiBhv-Ban7B45IXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbC-lejK-D65Xep5BhnIDHDJOQn6j2tI_Hnur3fcrXUI8LNDH2n-fW6-e0qvhQbRqOxoCqJ7zDJD_5RO7tqRXbKo8aRPMaMJaj4P6b-KW-xL1Db3UW6vMtg3l266p-DOoepvoW-oc3Mkt5tjdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjKjLEtbIJoDK5JDD3fP36q45HMt00qxby26nibe39aJ5nQI5nhKIzbb5tqqDs5xoZQJ5zam3ion3vQUbmjRO206oay6O3LlO83h52aC5LKl0MLPbcq-Q2Xh3YBUL10UnMBMnv5mOnanTa3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDFmj58aejv-jaRf-b-XJC5hWbr2HJO_bPOvQMnkbfJBDRK8WfbDKKca0D3l-66HbD3zbhoJ06t7yajd2tv4-g_q2RQGMx3ijnnj-PRpQT8r3fDOK5Oi0mjMhnkbab3vOUnNXpO1MJLzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksDMDtqjDetnke_KIQb-3bKR6Yh47oK-QH-UnLqM3fbgOZ0l8KttKVOR6jjPjDbb_-bt6N-qoj5K7J-DQmWIQrD4TL557Z5-0P3GJIBCrhbTQ4KKJxKRLWeIJo5Dc1LUPThUJiBhv-Ban7B45IXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbRO4-TFMDjjWDf5; H_BDCLCKID_SF_BFESS=JnIj_KK5tCt3qbjkqRQh-JDfqxbXq5jM22OZ0l8KtJT0oMO8y4jvqf4Ibt6N-Dr0b6rCM-omWIQrDl7N-IcA0hKUKfj30jtjXK34KKJxafKWeIJoQxcz5P70hUJiBhv-Ban7B45IXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbC-lejK-D65Xep5BhnIDHDJOQn6j2tI_Hnur3fcrXUI8LNDH2n-fW6-e0qvhQbRqOxoCqJ7zDJD_5RO7tqRXbKo8aRPMaMJaj4P6b-KW-xL1Db3UW6vMtg3l266p-DOoepvoW-oc3Mkt5tjdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjKjLEtbIJoDK5JDD3fP36q45HMt00qxby26nibe39aJ5nQI5nhKIzbb5tqqDs5xoZQJ5zam3ion3vQUbmjRO206oay6O3LlO83h52aC5LKl0MLPbcq-Q2Xh3YBUL10UnMBMnv5mOnanTa3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDFmj58aejv-jaRf-b-XJC5hWbr2HJO_bPOvQMnkbfJBDRK8WfbDKKca0D3l-66HbD3zbhoJ06t7yajd2tv4-g_q2RQGMx3ijnnj-PRpQT8r3fDOK5Oi0mjMhnkbab3vOUnNXpO1MJLzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksDMDtqjDetnke_KIQb-3bKR6Yh47oK-QH-UnLqM3fbgOZ0l8KttKVOR6jjPjDbb_-bt6N-qoj5K7J-DQmWIQrD4TL557Z5-0P3GJIBCrhbTQ4KKJxKRLWeIJo5Dc1LUPThUJiBhv-Ban7B45IXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbRO4-TFMDjjWDf5; BAIDUID=63A64EC406BCCDDE8E0ACE9CD1BB74B6:FG=1; BAIDUID_BFESS=63A64EC406BCCDDE8E0ACE9CD1BB74B6:FG=1; FPTOKEN=Ljax/CRqkYDuA03lWw40wxNufuI0M7RohtwnYhkupZjYyEPEON9MEaKxw8ZK5O6wOQebmEwHMQAlAL6+paZ4e0GW20UVfRtDrMS76nMq/OhhRaxUOvx+NMtV4qhkRPN/R/BeXwbzzqR1N8fbv/r1eOXnVjkFZOmZ6D5Ahpvxoa7/dO8mYH62zuYGefNsoalRJKJesgKCs5rxKlC+KL5/PFa1jRrhgOvtjix5cT+ByfLAil5E5pnS1hATQzauOmaaei1yAX6qQL9dGtken/jRDuUU8Um4iH9Z9EyiAsMFiMocl4MKllYUhPjXEhxt4rYzip2B/ozltLmoR/VL6JAa+v3Ik+Rew2U6o6jRARLhMNBIenG8nEXz0+nbcJZZDct8/MMe5B35yF1BIXptQJCrZA==|OUBjri5OiUzNpj1GUNazLN6vAdrszvENiWF6FNX9uEI=|10|46f922e432b96d54bb236cdaf67bcc64; H_PS_PSSID=; BDRCVFR[w2jhEs_Zudc]=mbxnW11j9Dfmh7GuZR8mvqV; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1683461176; BDUSS=H4xekIyaGlwNk5ia0FzbW1rMVF4dmVBbTd4UzMySlFjeUZ3cnh6M0Nrdjd-MzlrRUFBQUFBJCQAAAAAABAAAAEAAABsQD~7bG92ZXNjcmFweQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPtyWGT7clhkT; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a04335306533KeNCY66sGY4wguyf2LLNa/P4ek+JbVOp/IB2TWzSgMZSOdlcHuAecv5GQzNcBFLIRETg7YfkFglc093EYxpls9D+Ksm8g/RNo5F+M4EomsbkZ//j77y9ayEAWXuJrI9KRqJQM1y9a9eFVBazJ5uehmTHDImceb7uwp69u9qr2H2geXT58MkxkOs5BoRCVBbSDGzYE6YZGnIRRGDUV4H6tfuZmfPUXsGe5FIgjMuimVn+vnivRu50TVLUZhP9XBjbPafbTTY7J7kL3oHL1ZTAGA==65790890538528177025886171553036; __cas__rn__=433530653; __cas__st__212=42a286ce276fd410e89665b5cd7e4a8f17d71475e58ca5e9f0cb7d1ea0e184e05cdaab448125f11f1c46c702; __cas__id__212=47819677; CPID_212=47819677; CPTK_212=2077794587; bdindexid=4eep29df8pgoc0nfe6se4cvk26; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1683526398; BDUSS_BFESS=H4xekIyaGlwNk5ia0FzbW1rMVF4dmVBbTd4UzMySlFjeUZ3cnh6M0Nrdjd-MzlrRUFBQUFBJCQAAAAAABAAAAEAAABsQD~7bG92ZXNjcmFweQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPtyWGT7clhkT; ab_sr=1.0.1_ZGRjMDZmMTVlMDg3ZTY3OGFhMmJhMmRhNDQwZDQyYTMzMGFmMjgyMWZiNDUwZGVlOTI3NDAzZDdhMzFhNTg1ZjZjNmQxZDE4ZjNhYjRlYTE2ZDU2ZmViMTE1MzRmOTU5NTQ4Y2U1YjNlZTkzZGJjNzRiZmM1ZjhkYWRjZTk4OTE5NzFhNjEwNTQ3YWFiOTYzNjhlZjc0YTIwNTUyNTk4YQ==; RT="z=1&dm=baidu.com&si=299f6a2c-0c8e-413d-ab6d-208f80e3ee2d&ss=lhe9yiws&sl=n&tt=2a65&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ld=6cmly"',
    'Host': 'index.baidu.com',
    'Referer': 'https://index.baidu.com/v2/main/index.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35',
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


def get_index_data(area, keyword, startdate, enddate):
    url = 'https://index.baidu.com/api/SearchApi/index?area={}&word=[[%7B%22name%22:%22{}%22,%22wordType%22:1%7D]]&startDate={}&endDate={}'.format(area, keyword, startdate, enddate)

    resp = requests.get(url, headers=headers)
    # print(resp.json())
    content = resp.json()
    data = content.get('data')
    user_indexes = data.get('userIndexes')[0]
    uniqid = data.get('uniqid')
    ptbk = get_ptbk(uniqid)
    all_data = user_indexes.get('all').get('data')
    result = decrypt(ptbk, all_data)
    result = result.split(',')

    # print(result)
    df = pd.DataFrame()
    df[keyword] = result
    return df
# get_index_data('金融科技')

def dict_slice(adict, start, end):
    keys = adict.keys()
    dict_slice = {}
    for k in list(keys)[start:end]:
        dict_slice[k] = adict[k]
    return dict_slice

def main(start_area, start_key, end_key):
    areas = {'北京':911,'天津':923,'河北':920,'安徽':928,'澳门':934,'重庆':904,'福建':909,'广东':913,'广西':912,'甘肃':925,'贵州':902,'黑龙江':921,'河南':927,'湖南':908,'湖北':906,'海南':930,'吉林':922,'江苏':916,'江西':903,'辽宁':907,'内蒙古':905,'宁夏':919,'青海':918,'上海':910,'四川':914,'山东':901,'山西':929,'陕西':924,'台湾':931,'西藏':932,'香港':933,'新疆':926,'云南':915,'浙江':917}
    startdate = '2011-01-02'
    enddate = '2023-05-06'
    # start = 25
    while 1:
        # 遍历省份
        for d in dict_slice(areas, start_area-1, 35).items():
            d_name = d[0]
            d_number = d[1]
            d_indexs = list(areas.keys()).index(d_name)
            df = pd.DataFrame(columns=['area','time'])
            keys = ['大数据', '人工智能', '区块链', '云计算', '生物识别', '物联网', '分布式', '数字化', '智能化', '点对点网络', '流计算', '移动互联', '第三方支付', '在线支付', '移动支付', '云支付', '数字货币', '跨境支付平台', 'NFC支付', '电子交易', '网上银行', '电子银行', '网银', '众筹', 'P2P', '网贷', '网络贷款', '网络银行', '互联网银行', '直销银行', '手机银行', '精准营销', '电子商务', '在线理财', '网联', '互联网理财', '互联网保险', '互联网金融', '金融科技']
            # '量化金融'未被收录
            # 遍历关键词
            for word in keys[start_key-1:end_key]:
                df = get_index_data(d_number, word, startdate, enddate)
                # df = pd.concat([df,df1])
                ts = random.uniform(5,10)
                key_indexs = keys.index(word)
                print('要睡{}s, 地区: {}, 地区排名: {}/34, 关键词: {}, keys排名: {}/40'.format(ts, d_name, d_indexs+1, word, key_indexs+1))
                time.sleep(ts)
                d_index = str(d_indexs).rjust(2,'0')
                key_index = str(key_indexs).rjust(2, "0")
                df.to_csv('./new_get_index/results/{}_{}.csv'.format(d_index, key_index), index=False, encoding="utf-8")
        break

if __name__ == "__main__":
    # main(34, 12, 38)
    main(5, 34, 34)
    # main(1, 1, 38)
    # 默认从第1个省份的第1个词弄到第38个词语