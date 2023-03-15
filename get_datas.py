import datetime,requests,time,random,jsonpath,json
# import json,execjs,
import pandas as pd
from os.path import exists
from os import makedirs
# from fake_useragent import UserAgent
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
            "Connection": "keep-alive",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://index.baidu.com/v2/main/index.html",
            "Accept-Language": "zh-CN,zh;q=0.9",
            'Cookie': 'BAIDUID=5CB30231196662724CE3F2CD27C1B426:FG=1; BAIDUID_BFESS=5CB30231196662724CE3F2CD27C1B426:FG=1; newlogin=1; BDUSS=FZwY3JUc1hYMlJFZVdOUEpZMH4xNndLVWZ2cHVQM1ducHA3T2dpS0xJM2tTQU5rSVFBQUFBJCQAAAAAAQAAAAEAAAAJNBQtyP3Uwl9zY3JhcHkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOS722Pku9tja; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1676263263; Hm_up_d101ea4d2a5c67dab98251f0b5de24dc={"uid_":{"value":"5051266057","scope":1}}; bdindexid=1i5b0fcjv93geoei799tnn07v0; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a042644833221CgF/af/m8LrCjwe2KfSSRSQPByyMNGwYSe5VBd8r0qToUM1rMsI9fvG3N76yaXFXmn2WDP4xQ06aR5kxKBhN7vrYQdS96og8f8JF+qsrCtHOdzJd5RnVA6I01fP9GciLGG0IdXfMu4Tbk1rFaI7Zh6w5lztAMqRkyw4Ch77Qnt0W4Nna9jU6JIrjsL3s5jCk8/KUHxsVGFwmpCxFB7FpBsfdAmOfdqbX9WE1hLoCpniR3AueIIyBlGVJD3sMdFVwDfJIp+FIT2N9/FbjIJGyyxsh1rbl5JMjqoAMjEhMaQ=17862942550376409269103581343364; __cas__rn__=426448332; __cas__st__212=51cb64bef0a44e8cc866657c1d8891bc2a23ee2686d576f3a6eadfd67014d821e31e04903e138f4275225e9b; __cas__id__212=45415758; CPID_212=45415758; CPTK_212=658038598; BIDUPSID=5CB30231196662724CE3F2CD27C1B426; PSTM=1676436503; BA_HECTOR=2h05a42l2g85850g8g8ha4bj1huop0p1l; ZFY=w6SIYO7nechMXco6A5nV68uSVBHpRSrZ3vso8vlok:BE:C; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=5; delPer=0; H_PS_PSSID=38186_36542_37517_38091_38055_37910_38145_37989_38177_38170_37799_37927_38088_37900_26350_38136_38101_38008_37881; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1676436638; BDUSS_BFESS=FZwY3JUc1hYMlJFZVdOUEpZMH4xNndLVWZ2cHVQM1ducHA3T2dpS0xJM2tTQU5rSVFBQUFBJCQAAAAAAQAAAAEAAAAJNBQtyP3Uwl9zY3JhcHkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOS722Pku9tja; ab_sr=1.0.1_Y2IzNzFjYjA1Y2NkNTlhNDg5ZGQyZTI5MGRmMDZkOWRjY2I4NWUxMzc0MzYwMjUwZGZiYzdkNTJjZTQ0ODcyYzA4NDdhZmY5NzEyNWQ0NjUzMzRiZTA1NDM1ZmExNmM2NDg3MjYxMTczMjA0Zjc2ZDQwZjk0YzM2MTM2ODM2NTI0OGRhYjU5YTQ1ZjAyZWQ0NGZlOThmYjM2NmFmZDMyNg==; RT="z=1&dm=baidu.com&si=41530608-8ed0-42cb-bbcb-33a7ab8995eb&ss=le56n2zk&sl=4r&tt=2m4l&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ld=25umw&nu=4irf3z7s&cl=1znaq"',
            "Host": "index.baidu.com",
            "X-Requested-With": "XMLHttpRequest",
            "Cipher-Text": "1656572408684_1656582701256_Nvm1pABkNsfD7V9VhZSzzFiFKylr3l5NR3YDrmHmH9yfFicm+Z9kmmwKVqVV6unvzAEh5hgXmgelP+OyOeaK8F21LyRVX1BDjxm+ezsglwoe1yfp6lEpuvu5Iggg1dz3PLF8e2II0e80ocXeU0jQFBhSbnB2wjhKl57JggTej12CzuL+h9eeVWdaMO4DSBWU2XX6PfbN8pv9+cdfFhVRHCzb0BJBU3iccoFczwNQUvzLn0nZsu0YPtG5DxDkGlRlZrCfKMtqKAe1tXQhg3+Oww4N3CQUM+6A/tKZA7jfRE6CGTFetC7QQyKlD7nxabkQ5CReAhFYAFAVYJ+sEqmY5pke8s3+RZ6jR7ASOih6Afl35EArbJzzLpnNPgrPCHoJiDUlECJveul7P5vvXl/O/Q==",

        }
    # header = {
    #     'Accept': 'application/json, text/plain, */*',
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'Accept-Language': 'zh-CN,zh;q=0.9',
    #     # 'Connection': 'keep-alive',
    #     'Connection': 'close',
    #     'Cookie': 'BAIDUID=5CB30231196662724CE3F2CD27C1B426:FG=1; BAIDUID_BFESS=5CB30231196662724CE3F2CD27C1B426:FG=1; newlogin=1; BDUSS=FZwY3JUc1hYMlJFZVdOUEpZMH4xNndLVWZ2cHVQM1ducHA3T2dpS0xJM2tTQU5rSVFBQUFBJCQAAAAAAQAAAAEAAAAJNBQtyP3Uwl9zY3JhcHkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOS722Pku9tja; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1676263263; Hm_up_d101ea4d2a5c67dab98251f0b5de24dc=%7B%22uid_%22%3A%7B%22value%22%3A%225051266057%22%2C%22scope%22%3A1%7D%7D; bdindexid=1i5b0fcjv93geoei799tnn07v0; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a042644833221CgF%2Faf%2Fm8LrCjwe2KfSSRSQPByyMNGwYSe5VBd8r0qToUM1rMsI9fvG3N76yaXFXmn2WDP4xQ06aR5kxKBhN7vrYQdS96og8f8JF%2BqsrCtHOdzJd5RnVA6I01fP9GciLGG0IdXfMu4Tbk1rFaI7Zh6w5lztAMqRkyw4Ch77Qnt0W4Nna9jU6JIrjsL3s5jCk8%2FKUHxsVGFwmpCxFB7FpBsfdAmOfdqbX9WE1hLoCpniR3AueIIyBlGVJD3sMdFVwDfJIp%2BFIT2N9%2FFbjIJGyyxsh1rbl5JMjqoAMjEhMaQ%3D17862942550376409269103581343364; __cas__rn__=426448332; __cas__st__212=51cb64bef0a44e8cc866657c1d8891bc2a23ee2686d576f3a6eadfd67014d821e31e04903e138f4275225e9b; __cas__id__212=45415758; CPID_212=45415758; CPTK_212=658038598; BIDUPSID=5CB30231196662724CE3F2CD27C1B426; PSTM=1676436503; BA_HECTOR=2h05a42l2g85850g8g8ha4bj1huop0p1l; ZFY=w6SIYO7nechMXco6A5nV68uSVBHpRSrZ3vso8vlok:BE:C; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=5; delPer=0; H_PS_PSSID=38186_36542_37517_38091_38055_37910_38145_37989_38177_38170_37799_37927_38088_37900_26350_38136_38101_38008_37881; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1676436638; BDUSS_BFESS=FZwY3JUc1hYMlJFZVdOUEpZMH4xNndLVWZ2cHVQM1ducHA3T2dpS0xJM2tTQU5rSVFBQUFBJCQAAAAAAQAAAAEAAAAJNBQtyP3Uwl9zY3JhcHkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOS722Pku9tja; ab_sr=1.0.1_Y2IzNzFjYjA1Y2NkNTlhNDg5ZGQyZTI5MGRmMDZkOWRjY2I4NWUxMzc0MzYwMjUwZGZiYzdkNTJjZTQ0ODcyYzA4NDdhZmY5NzEyNWQ0NjUzMzRiZTA1NDM1ZmExNmM2NDg3MjYxMTczMjA0Zjc2ZDQwZjk0YzM2MTM2ODM2NTI0OGRhYjU5YTQ1ZjAyZWQ0NGZlOThmYjM2NmFmZDMyNg==; RT="z=1&dm=baidu.com&si=41530608-8ed0-42cb-bbcb-33a7ab8995eb&ss=le56n2zk&sl=4r&tt=2m4l&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=25umw&nu=4irf3z7s&cl=1znaq"',
    #     'Host': 'index.baidu.com',
    #     'Referer': 'https://index.baidu.com/v2/main/index.html',
    #     'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    #     'sec-ch-ua-mobile': '?0',
    #     'Sec-Fetch-Dest': 'empty',
    #     'Sec-Fetch-Mode': 'cors',
    #     'Sec-Fetch-Site': 'same-origin',
    #     # 'User-Agent': UserAgent(use_cache_server=False).random,
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
    # }
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
    # print(resData)
    # uniqid = json.loads(resData)['data']['uniqid']
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
    ky=5
    while 1:
        for d in areas.items():
            d_name = d[0]
            d_index = d[1]
            df = pd.DataFrame(columns=['area','time'])
            # keys = ['大数据','人工智能','区块链','第三方支付','在线支付','移动支付','网上银行','电子银行','网银','互联网理财','互联网保险','众筹','P2P','网贷']
            # keys = ['大数据','人工智能']
            keys = ['大数据', '人工智能', '区块链', '云计算', '生物识别', '物联网', '分布式', '数字化', '智能化', '点对点网络', '流计算', '移动互联', '第三方支付', '在线支付', '移动支付', '云支付', '数字货币', '跨境支付平台', 'NFC支付', '电子交易', '网上银行', '电子银行', '网银', '众筹', 'P2P', '网贷', '网络贷款', '网络银行', '互联网银行', '直销银行', '手机银行', '精准营销', '电子商务', '在线理财', '网联', '互联网理财', '互联网保险', '互联网金融', '金融科技', '量化金融']
            
            keys = keys[ky:ky+5]

            words = '[]]'
            # keys = ['大数据','人工智能']
            for k in keys:
                words = words.replace(']]','[%7B%22name%22:%22'+quote(k)+'%22,%22wordType%22:1%7D],]]')
            word = words.replace('],]]',']]')
            for y in range(2011,2021):
                df1=get_datas(d_index,word,y,d_name,keys)
                df = pd.concat([df,df1])
                ts = random.uniform(5,10)
                print('要睡{}s, ky={}'.format(ts, ky))
                time.sleep(ts)
            df.to_csv('./results/{}_{}.csv'.format(d_name,ky), index=False)
        # ky+=5
        break








# import requests
# import json
# from datetime import date, timedelta
# import pandas as pd


# class DownloadBaiDuIndex(object):
#     def __init__(self, cookie):
#         self.cookie = cookie
#         self.headers = {
#             "Connection": "keep-alive",
#             "Accept": "application/json, text/plain, */*",
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
#             "Sec-Fetch-Site": "same-origin",
#             "Sec-Fetch-Mode": "cors",
#             "Sec-Fetch-Dest": "empty",
#             "Referer": "https://index.baidu.com/v2/main/index.html",
#             "Accept-Language": "zh-CN,zh;q=0.9",
#             'Cookie': self.cookie,
#             "Host": "index.baidu.com",
#             "X-Requested-With": "XMLHttpRequest",
#             "Cipher-Text": "1656572408684_1656582701256_Nvm1pABkNsfD7V9VhZSzzFiFKylr3l5NR3YDrmHmH9yfFicm+Z9kmmwKVqVV6unvzAEh5hgXmgelP+OyOeaK8F21LyRVX1BDjxm+ezsglwoe1yfp6lEpuvu5Iggg1dz3PLF8e2II0e80ocXeU0jQFBhSbnB2wjhKl57JggTej12CzuL+h9eeVWdaMO4DSBWU2XX6PfbN8pv9+cdfFhVRHCzb0BJBU3iccoFczwNQUvzLn0nZsu0YPtG5DxDkGlRlZrCfKMtqKAe1tXQhg3+Oww4N3CQUM+6A/tKZA7jfRE6CGTFetC7QQyKlD7nxabkQ5CReAhFYAFAVYJ+sEqmY5pke8s3+RZ6jR7ASOih6Afl35EArbJzzLpnNPgrPCHoJiDUlECJveul7P5vvXl/O/Q==",

#         }

#     def decrypt(self, ptbk, index_data):
#         n = len(ptbk) // 2
#         a = dict(zip(ptbk[:n], ptbk[n:]))
#         return "".join([a[s] for s in index_data])

#     def get_index_data_json(self, keys, start=None, end=None):
#         words = [[{"name": key, "wordType": 1}] for key in keys]
#         words = str(words).replace(" ", "").replace("'", "\"")

#         url = f'http://index.baidu.com/api/SearchApi/index?area=0&word={words}&area=0&startDate={start}&endDate={end}'
#         print(words, start, end)
#         res = requests.get(url, headers=self.headers)
#         data = res.json()['data']
#         uniqid = data['uniqid']
#         url = f'http://index.baidu.com/Interface/ptbk?uniqid={uniqid}'
#         res = requests.get(url, headers=self.headers)
#         ptbk = res.json()['data']
#         result = {}
#         result["startDate"] = start
#         result["endDate"] = end
#         for userIndexe in data['userIndexes']:
#             name = userIndexe['word'][0]['name']
#             tmp = {}
#             index_all = userIndexe['all']['data']
#             index_all_data = [int(e) for e in self.decrypt(ptbk, index_all).split(",")]
#             tmp["all"] = index_all_data
#             index_pc = userIndexe['pc']['data']
#             index_pc_data = [int(e) for e in self.decrypt(ptbk, index_pc).split(",")]
#             tmp["pc"] = index_pc_data
#             index_wise = userIndexe['wise']['data']
#             index_wise_data = [int(e)
#                                for e in self.decrypt(ptbk, index_wise).split(",")]
#             tmp["wise"] = index_wise_data
#             result[name] = tmp
#         return result

#     def GetIndex(self, keys, start=None, end=None):
#         today = date.today()
#         if start is None:
#             start = str(today - timedelta(days=8))
#         if end is None:
#             end = str(today - timedelta(days=2))

#         try:
#             raw_data = self.get_index_data_json(keys=keys, start=start, end=end)
#             raw_data = pd.DataFrame(raw_data[keys[0]])
#             raw_data.index = pd.date_range(start=start, end=end)

#         except Exception as e:
#             print(e)
#             raw_data = pd.DataFrame({'all': [], 'pc': [], 'wise': []})

#         finally:
#             return raw_data


# cookie = 'BAIDUID=5CB30231196662724CE3F2CD27C1B426:FG=1; BAIDUID_BFESS=5CB30231196662724CE3F2CD27C1B426:FG=1; newlogin=1; BDUSS=FZwY3JUc1hYMlJFZVdOUEpZMH4xNndLVWZ2cHVQM1ducHA3T2dpS0xJM2tTQU5rSVFBQUFBJCQAAAAAAQAAAAEAAAAJNBQtyP3Uwl9zY3JhcHkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOS722Pku9tja; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1676263263; Hm_up_d101ea4d2a5c67dab98251f0b5de24dc={"uid_":{"value":"5051266057","scope":1}}; bdindexid=1i5b0fcjv93geoei799tnn07v0; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a042644833221CgF/af/m8LrCjwe2KfSSRSQPByyMNGwYSe5VBd8r0qToUM1rMsI9fvG3N76yaXFXmn2WDP4xQ06aR5kxKBhN7vrYQdS96og8f8JF+qsrCtHOdzJd5RnVA6I01fP9GciLGG0IdXfMu4Tbk1rFaI7Zh6w5lztAMqRkyw4Ch77Qnt0W4Nna9jU6JIrjsL3s5jCk8/KUHxsVGFwmpCxFB7FpBsfdAmOfdqbX9WE1hLoCpniR3AueIIyBlGVJD3sMdFVwDfJIp+FIT2N9/FbjIJGyyxsh1rbl5JMjqoAMjEhMaQ=17862942550376409269103581343364; __cas__rn__=426448332; __cas__st__212=51cb64bef0a44e8cc866657c1d8891bc2a23ee2686d576f3a6eadfd67014d821e31e04903e138f4275225e9b; __cas__id__212=45415758; CPID_212=45415758; CPTK_212=658038598; BIDUPSID=5CB30231196662724CE3F2CD27C1B426; PSTM=1676436503; BA_HECTOR=2h05a42l2g85850g8g8ha4bj1huop0p1l; ZFY=w6SIYO7nechMXco6A5nV68uSVBHpRSrZ3vso8vlok:BE:C; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=5; delPer=0; H_PS_PSSID=38186_36542_37517_38091_38055_37910_38145_37989_38177_38170_37799_37927_38088_37900_26350_38136_38101_38008_37881; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1676436638; BDUSS_BFESS=FZwY3JUc1hYMlJFZVdOUEpZMH4xNndLVWZ2cHVQM1ducHA3T2dpS0xJM2tTQU5rSVFBQUFBJCQAAAAAAQAAAAEAAAAJNBQtyP3Uwl9zY3JhcHkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOS722Pku9tja; ab_sr=1.0.1_Y2IzNzFjYjA1Y2NkNTlhNDg5ZGQyZTI5MGRmMDZkOWRjY2I4NWUxMzc0MzYwMjUwZGZiYzdkNTJjZTQ0ODcyYzA4NDdhZmY5NzEyNWQ0NjUzMzRiZTA1NDM1ZmExNmM2NDg3MjYxMTczMjA0Zjc2ZDQwZjk0YzM2MTM2ODM2NTI0OGRhYjU5YTQ1ZjAyZWQ0NGZlOThmYjM2NmFmZDMyNg==; RT="z=1&dm=baidu.com&si=41530608-8ed0-42cb-bbcb-33a7ab8995eb&ss=le56n2zk&sl=4r&tt=2m4l&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ld=25umw&nu=4irf3z7s&cl=1znaq"'

# # 初始化一个类
# downloadbaiduindex = DownloadBaiDuIndex(cookie=cookie)

# data = downloadbaiduindex.GetIndex(keys=['金融科技'], start='2021-01-01', end='2021-11-12')

# data.to_csv('data.csv')

