import pandas as pd
import json

json_path = r"F:\Machine Learning\loan\Member information.txt"
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.DataFrame(data)

min_income = 45000000

res = df[
    (df['income'] >= min_income) &
    (df['installment_count'] <= 12)
]
# id = عدد 1 تا 10
# full_name =نام و نام خانوادگی
# income = درامد
# account_balance = گردش حساب
# installment_count = تعداد اقساط

print(res[['id', 'full_name', 'income', 'account_balance', 'installment_count']])
