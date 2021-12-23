import datetime

import requests
import execjs
import pandas as pd


# 搜索指数数据解密
def decryption(keys, data):
    dec_dict = {}
    for j in range(len(keys) // 2):
        dec_dict[keys[j]] = keys[len(keys) // 2 + j]

    dec_data = ''
    for k in range(len(data)):
        dec_data += dec_dict[data[k]]
    return dec_data

def get_datas(d,scenicName,y,d_name):
    dataUrl = 'https://index.baidu.com/api/SearchApi/index?area={}&word=[[%7B%22name%22:%22{}%22,%22wordType%22:1%7D]]&startDate={}-01-02&endDate={}-01-01'.format(d,scenicName,y,y+1)
    keyUrl = 'https://index.baidu.com/Interface/ptbk?uniqid='
    header = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'BDUSS=pUVVRsazRNV0xBb2V1ekVXdlFQZlc1WkhoY05jZGF-THR6RFZKd3VJbGlQc3RoSVFBQUFBJCQAAAAAABAAAAEAAABsQD~7bG92ZXNjcmFweQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGKxo2FisaNhTn; BDUSS_BFESS=pUVVRsazRNV0xBb2V1ekVXdlFQZlc1WkhoY05jZGF-THR6RFZKd3VJbGlQc3RoSVFBQUFBJCQAAAAAABAAAAEAAABsQD~7bG92ZXNjcmFweQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGKxo2FisaNhTn; __yjs_duid=1_3e0e0d21420e02edd28e3957e214d5d81638369910940; PSTM=1638440151; BIDUPSID=2B5A58CD9B34C75B73927D1173691AAB; BAIDUID=9075CEBBDB61149A821A686582441B6A:FG=1; BAIDUID_BFESS=ED34EE7BA6EA26D0E0D075C689E263A5:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=34443_35292_35104_31253_35239_34968_34584_35490_35532_35233_26350_35478; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1640241464; bdindexid=fgh0b7raeif6vv7uutc981o777; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1640241483; __yjs_st=2_ODYzMjNkNTNkNDkxNTU5Yzk0NzE4NDg4YThmMDUxNTFkNWM0YjliMzQyNjFiOTUxODVjNDdkMmU2MWM5MDY3MGYzNjRlNGIzM2I4ZTYzNGRlMWI4NmUzNjgxY2YxY2I5NWNhM2Q3N2VjMGI0NzE5NTM2ZTFiOTYxMjJmMTkzZGQ1MWE0ZTY4MDlkZGU2ZDQ2OWIyMGJhYmYzZTY0MzgwYWNkZjliNDJiMDY1M2M0NWI4YmJmYThiOWYwYWNiNWM5MzkxMjFmMzE1MzE3NWUzZTA5Mjk2OTMyMjJjNDJmOGY3YWViNTc4Yjc0ZThkZjE4MDA1MDIwOTJjNDIxOGJjOV83XzNjN2E2ZDMz; RT="z=1&dm=baidu.com&si=fplw3nxjjyk&ss=kxj0hz4z&sl=2&tt=3q3&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=31sy"',
        'Host': 'index.baidu.com',
        'Referer': 'https://index.baidu.com/v2/main/index.html',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
    }
    # 设置请求超时时间为30秒
    resData = requests.get(dataUrl, timeout=30, headers=header)

    uniqid = resData.json()['data']['uniqid']
    print("uniqid:{}".format(uniqid))
    keyData = requests.get(keyUrl + uniqid, timeout=30, headers=header)
    keyData.raise_for_status()
    keyData.encoding = resData.apparent_encoding

    # 开始对json数据进行解析
    startDate = resData.json()['data']['userIndexes'][0]['all']['startDate']
    print("startDate:{}".format(startDate))
    endDate = resData.json()['data']['userIndexes'][0]['all']['endDate']
    print("endDate:{}".format(endDate))
    source = (resData.json()['data']['userIndexes'][0]['all']['data'])  # 原加密数据
    # print("原加密数据:{}".format(source))
    key = keyData.json()['data']  # 密钥
    # print("密钥:{}".format(key))


    res = decryption(key, source)
    resArr = res.split(",")

    dateStart = datetime.datetime.strptime(startDate, '%Y-%m-%d')
    dateEnd = datetime.datetime.strptime(endDate, '%Y-%m-%d')
    dataLs = []
    while dateStart <= dateEnd:
        dataLs.append(str(dateStart))
        dateStart += datetime.timedelta(days=1)

    ls = []
    for i in range(len(dataLs)):
        ls.append([d_name, scenicName, dataLs[i], resArr[i]])

    # for i in range(len(ls)):
    #     print(ls[i])
    return pd.DataFrame(ls,columns=['areas','keys','times','keys'])

if __name__ == "__main__":
    areas = {'北京':911,'天津':923,'河北':920}
    # areas = {'北京':911,'天津':923,'河北':920,'安徽':928,'澳门':934,'重庆':904,'福建':909,'广东':913,'广西':912,'甘肃':925,'贵州':902,'黑龙江':921,'河南':927,'湖南':908,'湖北':906,'海南':930,'吉林':922,'江苏':916,'江西':903,'辽宁':907,'内蒙古':905,'宁夏':919,'青海':918,'上海':910,'四川':914,'山东':901,'山西':929,'陕西':924,'台湾':931,'西藏':932,'香港':933,'新疆':926,'云南':915,'浙江':917}
    for d in areas.items():
        d_name = d[0]
        d_index = d[1]
        print(d_name)
        df = pd.DataFrame(columns=['areas','keys','times','keys'])
        keys = ['第三方支付','人工智能','P2P']
        for k in keys:           
            for y in range(2011,2021):
                df1=get_datas(d_index,k,y,d_name)
                df = pd.concat([df,df1])
        df.to_csv('./results/{}.csv'.format(d_name), index=False)
