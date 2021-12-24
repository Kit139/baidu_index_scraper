import datetime,requests,execjs,time,random,jsonpath
import json
import pandas as pd
from os.path import exists
from os import makedirs
from fake_useragent import UserAgent
from urllib.request import quote

RESULTS_DIR = 'results'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

# 搜索指数数据解密
def decryption(keys, data):
    dec_dict = {}
    for j in range(len(keys) // 2):
        dec_dict[keys[j]] = keys[len(keys) // 2 + j]
    dec_data = ''
    for k in range(len(data)):
        dec_data += dec_dict[data[k]]
    return dec_data

def get_res(url):
    requests.adapters.DEFAULT_RETRIES = 5
    header = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Connection': 'keep-alive',
        'Connection': 'close',
        'Cookie': 'BDUSS=pUVVRsazRNV0xBb2V1ekVXdlFQZlc1WkhoY05jZGF-THR6RFZKd3VJbGlQc3RoSVFBQUFBJCQAAAAAABAAAAEAAABsQD~7bG92ZXNjcmFweQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGKxo2FisaNhTn; BDUSS_BFESS=pUVVRsazRNV0xBb2V1ekVXdlFQZlc1WkhoY05jZGF-THR6RFZKd3VJbGlQc3RoSVFBQUFBJCQAAAAAABAAAAEAAABsQD~7bG92ZXNjcmFweQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGKxo2FisaNhTn; __yjs_duid=1_3e0e0d21420e02edd28e3957e214d5d81638369910940; PSTM=1638440151; BIDUPSID=2B5A58CD9B34C75B73927D1173691AAB; BAIDUID=9075CEBBDB61149A821A686582441B6A:FG=1; BAIDUID_BFESS=ED34EE7BA6EA26D0E0D075C689E263A5:FG=1; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1640241464; __yjs_st=2_ODYzMjNkNTNkNDkxNTU5Yzk0NzE4NDg4YThmMDUxNTFkNWM0YjliMzQyNjFiOTUxODVjNDdkMmU2MWM5MDY3MGYzNjRlNGIzM2I4ZTYzNGRlMWI4NmUzNjgxY2YxY2I5NWNhM2Q3N2VjMGI0NzE5NTM2ZTFiOTYxMjJmMTkzZGQ1MWE0ZTY4MDlkZGU2ZDQ2OWIyMGJhYmYzZTY0MzgwYWNkZjliNDJiMDY1M2M0NWI4YmJmYThiOWYwYWNiNWM5MzkxMjFmMzE1MzE3NWUzZTA5Mjk2OTMyMjJjNDJmOGY3YWViNTc4Yjc0ZThkZjE4MDA1MDIwOTJjNDIxOGJjOV83XzNjN2E2ZDMz; ab_sr=1.0.1_MWM0YmYwNzEzNDQwZjFmZjA4ZDEwMzZiNTA2MDQ0Y2E0ZWMxMTU0MWY2NmY4OGVhYjAxZjFhNGM2NDczMzNmZjhkNDA2NDJiMWNhMWY5MTE5ZDFiYmNlZjVlYTViOTk4Mjg0MDRhZjViMTljZjQ5NjAzOGE2MWI1ZWMxOTZhNzJiZTU4NzY2ZGM1OTgyODk1ZGQ3N2YwYjliNjU5OGU2Mw==; bdindexid=oaim5ilmve01plumh8j13mheb6; RT="z=1&dm=baidu.com&si=mqrdx06prj9&ss=kxk5bhe9&sl=2&tt=7ha&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ld=6mt&ul=kum"',
        'Host': 'index.baidu.com',
        'Referer': 'https://index.baidu.com/v2/main/index.html',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # 'User-Agent': UserAgent(use_cache_server=False).random,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
    }
    try:
        res = requests.get(url,headers=header, timeout=30)
        if res.status_code == 200:
            return res
    
    except requests.RequestException:
        print('error occurred while scraping %s', url)


def get_datas(d_index,word,y,d_name,keys):
    dataUrl = 'https://index.baidu.com/api/SearchApi/index?area={}&word={}&startDate={}-01-01&endDate={}-12-31'.format(d_index,word,y,y)
    keyUrl = 'https://index.baidu.com/Interface/ptbk?uniqid='

    resData = get_res(dataUrl)
    uniqid = resData.json()['data']['uniqid']
    print("uniqid:{}".format(uniqid))

    keyData = get_res(keyUrl + uniqid)
    keyData.raise_for_status()
    keyData.encoding = resData.apparent_encoding

    startDate = resData.json()['data']['userIndexes'][0]['all']['startDate']
    endDate = resData.json()['data']['userIndexes'][0]['all']['endDate']
    print("{},{},{}".format(d_name,startDate,endDate))

    sources = jsonpath.jsonpath(resData.json(),'$..all.data')
    key = keyData.json()['data']  # 密钥

    dateStart = datetime.datetime.strptime(startDate, '%Y-%m-%d')
    dateEnd = datetime.datetime.strptime(endDate, '%Y-%m-%d')
    dataLs = []
    while dateStart <= dateEnd:
        dataLs.append(str(dateStart)[0:10])
        dateStart += datetime.timedelta(days=1)

    df = pd.DataFrame()
    df['area'] = [d_name for i in range(len(dataLs))]
    df['time'] = dataLs
    for source,ke in zip(sources,keys):
        res = decryption(key, source)
        resArr = res.split(",")
        lenth1 = len(dataLs)
        # lenth2 = len(resArr)
        if resArr == ['']:
            resArr = ['0' for i in range(lenth1)]
        # elif 1 <lenth2<lenth1:
        #     resArr = ['0' for i in range(lenth1-lenth2)]+resArr
        df[ke] = [0 if i == '' else i for i in resArr]
    return df

if __name__ == "__main__":
    areas = {'北京':911,'天津':923,'河北':920}
    # areas = {'北京':911,'天津':923,'河北':920,'安徽':928,'澳门':934,'重庆':904,'福建':909,'广东':913,'广西':912,'甘肃':925,'贵州':902,'黑龙江':921,'河南':927,'湖南':908,'湖北':906,'海南':930,'吉林':922,'江苏':916,'江西':903,'辽宁':907,'内蒙古':905,'宁夏':919,'青海':918,'上海':910,'四川':914,'山东':901,'山西':929,'陕西':924,'台湾':931,'西藏':932,'香港':933,'新疆':926,'云南':915,'浙江':917}
    for d in areas.items():
        d_name = d[0]
        d_index = d[1]
        df = pd.DataFrame(columns=['area','time'])
        keys = ['大数据','人工智能','区块链','第三方支付','在线支付','移动支付','网上银行','电子银行','网银','互联网理财','互联网保险','众筹','P2P','网贷']
        ky=10
        keys = keys[ky::]

        words = '[]]'
        # keys = ['大数据','人工智能']
        for k in keys:
            words = words.replace(']]','[%7B%22name%22:%22'+quote(k)+'%22,%22wordType%22:1%7D],]]')
        word = words.replace('],]]',']]')
        for y in range(2011,2021):
            df1=get_datas(d_index,word,y,d_name,keys)
            df = pd.concat([df,df1])
            ts = random.uniform(2.5,5.3)
            print('要睡{}s'.format(ts))
            time.sleep(ts)
        df.to_csv('./results/{}_{}.csv'.format(d_name,ky), index=False)