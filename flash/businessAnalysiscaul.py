import os

import pandas as pd
# 对账计算

# 读取订单信息，和商品信息，并关联
parcel_path = "/Users/flash/LCP仓储/经营分析日报4月/包裹详情"
parcel_name = "2024-04-30-parcel.csv"
order_path = "/Users/flash/LCP仓储/经营分析日报4月/订单详情"
order_name = "2024-04-30订单详情_订单查询_20240502.csv"

merchandise_path = "/Users/flash/LCP仓储/经营分析日报4月/商品基础信息"
merchandise_name = "商品基本信息0429_商品基本信息列表页导出lzd_20240430.csv"

data1 = pd.read_csv(os.path.join(parcel_path, parcel_name), encoding='unicode_escape', usecols=['External Order No.', 'Packaging Material Code', 'Manufct. Barcode', 'Pack Operator'])
data2 = pd.read_csv(os.path.join(merchandise_path, merchandise_name), encoding='unicode_escape')
data3 = pd.read_csv(os.path.join(order_path, order_name), usecols=['外部订单号', '发货数量'])

data1['Manufct. Barcode'] = data1['Manufct. Barcode'].str.replace('`', '')
data2['MB'] = data2['MB'].str.replace('`', '')

data4 = pd.merge(data1, data2, left_on='Manufct. Barcode', right_on='MB', how='left')
data = pd.merge(data4, data3, left_on='External Order No.', right_on='外部订单号', how='left')

# 筛选订单的最长边，最大重量
# 只保留需要的列：包裹号，包材，最长边，最大重量，件数
# 'Length[cm]\t', 'Width[cm]\t', 'Height[cm]\t', 'Volume[cm3]\t', 'Weight[kg]'

df1 = data.groupby(['External Order No.', 'Packaging Material Code', '发货数量']).agg(
    {'Length[cm]\t': 'max', 'Width[cm]\t': 'max', 'Height[cm]\t': 'max', 'Volume[cm3]\t': 'max', 'Weight[kg]': 'max'})

df = pd.DataFrame(df1)
df.reset_index(inplace=True)

df['max_length'] = df[['Length[cm]\t', 'Width[cm]\t', 'Height[cm]\t']].max(axis=1)

df = df.rename(columns={'Weight[kg]': 'Weight'})
df = df.rename(columns={'发货数量': 'Number'})


# 根据最长边和最大重量分类订单大小
def size(a, b):
    if a <= 25 and b <= 15:
        return 'Small'
    elif 25 < a <= 50 and b <= 15:
        return 'Standard'
    elif 50 < a <= 105 and b <= 15:
        return 'Large'
    else:
        return 'Bulky'


df['size'] = df.apply(lambda x: size(x['max_length'], x['Weight']), axis=1)
df = df.astype({'size':'string'})

# 计算超出5pcs的单品数量
def pcs_exceed_5(a):
    if a > 5:
        return a - 5
    else:
        return 0


df['pcs_exceed_5'] = df.apply(lambda x: pcs_exceed_5(x['Number']), axis=1)

def price(a, b):
    if a == 'Small':
        return (1.96+b*0.2)
    else:
        return (3+b*0.2)

df['price'] = df.apply(lambda x: price(x['size'], x['pcs_exceed_5']), axis=1)


#导出每一笔订单的账单详情
# df.to_csv("/Users/flash/OneDrive/闪电快车/LCP/0404经营分析日报/0301V5/20240301的账单详细数据.csv")

print(df['size'].value_counts())

groupedSize = df.groupby('size').agg({'Number': 'sum'}).reset_index().sort_values(by='Number', ascending=False)
print(groupedSize)
# print(df.groupby(['size'])['Number'].sum())

groupedExceed5 = df.groupby('size').agg({'pcs_exceed_5': 'sum'}).reset_index().sort_values(by='pcs_exceed_5', ascending=False)
print(groupedExceed5)

# print(df.groupby(['size'])['pcs_exceed_5'].sum())

print(df['Packaging Material Code'].value_counts())
print(df['pcs_exceed_5'].sum())