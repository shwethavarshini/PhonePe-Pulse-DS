import os
from os import walk
from pathlib import Path
import pandas as pd

# Transaction = pd.DataFrame({})
# Transaction_Summary = pd.DataFrame({})
#
#
# def Transaction_fun(state, year, quarter, path):
#     global Transaction
#     global Transaction_Summary
#     djson = pd.read_json(path)
#
#     dfrom = djson['data']['from']
#     dto = djson['data']['to']
#     T_row = {'State': state, 'Year': year, 'Quarter': quarter, 'Data From': dfrom, 'Data To': dto}
#     Transaction_Summary = Transaction_Summary.append(T_row, ignore_index=True)
#     DAT_temp = djson['data']['transactionData']
#     if DAT_temp:
#         for i in DAT_temp:
#             DAT_row = {'Payment Mode': i['name'], 'Total Transactions count': i['paymentInstruments'][0]['count'],
#                        'Total Amount': i['paymentInstruments'][0]['amount'], 'Quarter': quarter, 'Year': year,
#                        'State': state}
#             Transaction = Transaction.append(DAT_row, ignore_index=True)
#
#
# # PATH FOR ALL STATES IN AGGREGATED TRANSACTIONS
# mt_s = r'C:\Users\SHWETHA\Documents\GitHub\pulse\data\aggregated\transaction\country\india\state'
# mt_path = r'C:\Users\SHWETHA\Documents\GitHub\pulse\data\aggregated\transaction\country\india\state'
# mt_states = os.listdir(mt_path)  # NAMES OF ALL DIRECTORIES IN STATES (36 STATES)
#
# for i in mt_states:  # ITERATE ALL STATES
#     # print(i)
#     p = mt_s + '\\' + i  # PICK ONE STATE PATH
#     states_year = os.listdir(p)  # PICK 2018 TO 2022 DIRECTORIES IN ONE STATE
#     for j in states_year:  # ITERATE YEARS 2018 TO 2022
#         # print(j)
#         pt = p + '\\' + j  # PICK ONE YEAR PATH
#         f = []
#         for (dirpath, dirnames, filenames) in walk(pt):
#             f.extend(filenames)  # PICK ALL THE QFILES IN SELECTED YEAR
#             break
#         for k in f:  # ITERATE THROUGH QFILES 1.JSON TO 4.JSON
#             fp = pt + '\\' + k  # PICK ONE QFILE PATH
#             fn = Path(fp).stem  # NOTE DOWN QUARTER
#             # print(i,j,fn)
#             Transaction_fun(i, j, fn, fp)  # CALL FUNCTION WITH STATE,YEAR,QFILE,QUARTER
#             # print(fp)
# # Transaction.to_csv('Transaction.csv', index=False)
# # print(len(Transaction))
# # print(Transaction.head(5))
#
# # Transaction_Summary.to_csv('Transaction_Summary.csv',index=False)
# # print(len(Transaction_Summary))
# # print(Transaction_Summary.head(5))
#
# ###User_Table
# User_Table = pd.DataFrame({})
# User_Summary = pd.DataFrame({})
#
#
# def User_fun(state, year, quarter, path):
#     global User_Table
#     global User_Summary
#     djson2 = pd.read_json(path)
#
#     regUsers = djson2['data']['aggregated']['registeredUsers']
#     appOpens = djson2['data']['aggregated']['appOpens']
#     U_row = {'State': state, 'Year': year, 'Quarter': quarter, 'Registered Users': regUsers,
#              'AppOpenings': appOpens}
#     User_Summary = User_Summary.append(U_row, ignore_index=True)
#
#     DAU_temp = djson2['data']['usersByDevice']
#     if DAU_temp:
#         for i in DAU_temp:
#             DAU_row = {'Brand Name': i['brand'], 'Registered Users Count': i['count'],
#                        'Percentage Share of Brand': i['percentage'], 'Quarter': quarter, 'Year': year, 'State': state}
#             User_Table = User_Table.append(DAU_row, ignore_index=True)
#
#
# s = r'C:\Users\SHWETHA\Documents\GitHub\pulse\data\aggregated\user\country\india\state'
# u_path = r'C:\Users\SHWETHA\Documents\GitHub\pulse\data\aggregated\user\country\india\state'
# states = os.listdir(u_path)
#
# for i in states:
#     # print(i)
#     p = s + '\\' + i
#     states_year = os.listdir(p)
#     for j in states_year:
#         # print(j)
#         pt = p + '\\' + j
#         f = []
#         for (dirpath, dirnames, filenames) in walk(pt):
#             f.extend(filenames)
#             break
#         for k in f:
#             fp = pt + '\\' + k
#             fn = Path(fp).stem
#             # print(i,j,fn)
#             User_fun(i, j, fn, fp)
#             # print(fp)
# User_Table
# User_Table.to_csv('User_Table.csv', index=False)
# print(len(User_Table))
# print(User_Table.head(5))
#
# User_Summary.to_csv('Data_Aggregated_User_Summary_Table.csv',index=False)
# print(len(User_Summary))
# print(User_Summary.head(5))

# Map_Transaction = pd.DataFrame({})
#
#
# def Map_Transaction_Fun(state,year,quarter,path):
#     global Map_Transaction
#     dmt = pd.read_json(path)
#     DMT_temp=dmt['data']['hoverDataList']
#     if DMT_temp:
#         for i in DMT_temp:
#             DMT_row={ 'Place Name':i['name'], 'Total Transactions count':i['metric'][0]['count'], 'Total Amount':i['metric'][0]['amount'],'Quarter':quarter,'Year': year,'State':state}
#             Map_Transaction = Map_Transaction.append(DMT_row, ignore_index = True)
#
# mt_s= r'C:\Users\SHWETHA\Documents\GitHub\pulse\data\map\transaction\hover\country\india\state'
# mt_path = r'C:\Users\SHWETHA\Documents\GitHub\pulse\data\map\transaction\hover\country\india\state'
# mt_states = os.listdir(mt_path)
#
# for i in mt_states:
#     #print(i)
#     p= mt_s + '\\' + i
#     states_year=os.listdir(p)
#     for j in states_year:
#         #print(j)
#         pt=p+'\\'+j
#         f=[]
#         for (dirpath, dirnames, filenames) in walk(pt):
#             f.extend(filenames)
#             break
#         for k in f:
#             fp=pt+'\\'+k
#             fn=Path(fp).stem
#             #print(i,j,fn)
#             Map_Transaction_Fun(i, j, fn, fp)
#             #print(fp)
#
# Map_Transaction.to_csv('Map_Transaction.csv', index=False)
# print(len(Map_Transaction))
# print(Map_Transaction.head(5))
#

Map_User = pd.DataFrame({})


def Map_User_Fun(state, year, quarter, path):
    global Map_User
    dmu = pd.read_json(path)

    DMU_temp = dmu['data']['hoverData']
    if DMU_temp:
        for i in DMU_temp:
            # print(i, DMU_temp[i]['registeredUsers'],DMU_temp[i]['appOpens'])
            DMU_row = {'Place Name': i, 'Registered Users Count': DMU_temp[i]['registeredUsers'],
                       'App Openings': DMU_temp[i]['appOpens'], 'Quarter': quarter, 'Year': year, 'State': state}
            Map_User = Map_User.append(DMU_row, ignore_index=True)


mu_s = r'C:\Users\SHWETHA\Documents\GitHub\pulse\data\map\user\hover\country\india\state'
mu_path = r'C:\Users\SHWETHA\Documents\GitHub\pulse\data\map\user\hover\country\india\state'
mu_states = os.listdir(mu_path)

for i in mu_states:
    # print(i)
    p = mu_s + '\\' + i
    states_year = os.listdir(p)
    for j in states_year:
        # print(j)
        pt = p + '\\' + j
        f = []
        for (dirpath, dirnames, filenames) in walk(pt):
            f.extend(filenames)
            break
        for k in f:
            fp = pt + '\\' + k
            fn = Path(fp).stem
            # print(i,j,fn)
            Map_User_Fun(i, j, fn, fp)
            # print(fp)

Map_User.to_csv('Map_User.csv', index=False)
print(len(Map_User))
print(Map_User.head(5))