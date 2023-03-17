import requests

def get_stat(): #получить значение счетчика
   return requests.get('http://127.0.0.1:5000/api/get_stat')

def reg_unk(): #увеличить на 1
   return requests.get('http://127.0.0.1:5000/api/register_unknown')

def res_unk(): #сбросить счетчик
   return requests.get('http://127.0.0.1:5000/api/reset_unknown')

print(get_stat().json()['unknown'])
# # reg_unk()
# print(get_stat().json()['unknown'])
# # res_unk()
# print(get_stat().json()['unknown'])

