# from datetime import datetime, timedelta
# import pandas as pd

# today = datetime.strptime("2011-01-02", '%Y-%m-%d')    # 将字符串格式化为datetime类型
# nowday = datetime.strptime("2023-05-08", '%Y-%m-%d')
# # print(n.strftime('%Y-%m-%d'))
# times = []
# while today < nowday:
#     times.append(str(today.strftime('%Y-%m-%d')))
#     sundays = timedelta(days=7)
#     today += sundays
# # print(len(times))
# df = pd.DataFrame(times, columns=['周'])
# df.to_csv('./new_get_index/sundays.csv', encoding='utf-8', index=False)

# for i in range(1,30):
#     print (str(i).rjust(2,'0'))

l = keys = ['大数据', '人工智能', '区块链', '云计算', '生物识别', '物联网', '分布式', '数字化', '智能化', '点对点网络', '流计算', '移动互联', '第三方支付', '在线支付', '移动支付', '云支付', '数字货币', '跨境支付平台', 'NFC支付', '电子交易', '网上银行', '电子银行', '网银', '众筹', 'P2P', '网贷', '网络贷款', '网络银行', '互联网银行', '直销银行', '手机银行', '精准营销', '电子商务', '在线理财', '网联', '互联网理财', '互联网保险', '互联网金融', '金融科技', '量化金融']
print(len(l))
