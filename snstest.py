import seaborn as sns
import pandas as pd
import random
0
filepath='C:/Users/Andre/Downloads/income/all_income.csv'
income_data=pd.read_csv(filepath) #read csv file from path

#print(len(income_data)) #13098
income_data = income_data[income_data.總薪資 != '… ']
income_data = income_data[income_data.總薪資 != '— ']
income_data = income_data[income_data.總薪資 != '總薪資']
#print(len(income_data)) #6129

#print(income_data.head())
income_data.總薪資=pd.to_numeric(income_data.總薪資, errors='coerce')
income_data.受僱員工人數=pd.to_numeric(income_data.受僱員工人數, errors='coerce')
#print(income_data.總薪資.dtype) #float64

income_data = income_data.dropna()
#print(len(income_data)) #6125
print('歡迎來到猜薪水遊戲。')
print(f'資料庫中共有{len(income_data)}種職業別。請輸入題目中從事各職業的人數下限：')
thres=input()
while thres!='ok':
    thres=int(thres)
    j=thres
    temp=income_data[income_data.受僱員工人數 >= thres]
    print(f'受僱員工人數超過{thres}的職業別共有{len(temp)}種')
    print('確定請輸入ok，或是可以直接重新輸入數字設定人數下限')
    thres=input()
print('遊戲開始')
        
def guess_income_game(thres):
    hp=200
    score=0
    while hp>0: 
        i=random.randint(0,len(income_data)-1)
        while income_data.受僱員工人數.iloc[i]<thres:
            i=random.randint(0,len(income_data)-1)
        job=income_data.iloc[i].職類別
        typ=income_data.iloc[i].行業別
        peep=int(income_data.iloc[i].受僱員工人數)
        income=int(income_data.iloc[i].總薪資)
        print(f'猜{peep}位從事於{typ}的{job}的平均每月總薪資？')
        
        ans=int(input())
        err=round(min(abs(ans-income)/income, 1)*100,2)
        print(f'答案是{income}元，您的誤差為{err}%')

        hp-=err
        hp=round(hp,2)
        score+=1
        print(f'您的血量剩餘{hp}。恭喜獲得1分')
    print(f'遊戲結束。您的總分為{score}分')

guess_income_game(j)
