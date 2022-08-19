# import requests
# from bs4 import BeautifulSoup
#
# r = requests.get('https://www.digikala.com/search/category-men-tee-shirts/')
# # print(r.status_code)
# # print(r.text)
# # print("@" * 100)
# # print(type(r))
# # print(type(r.text))
#
# sop = BeautifulSoup(r.text, 'html.parser')
# tshirtlinks = sop.find_all('a', attrs={'class': ' pointer '})
# print(str(tshirtlinks))
# doc = list()
# doc.extend(tshirtlinks)
#
#
# # for i in tshirtlinks:
# #     doc.append(i.get('href'))
# print(doc)
# print(r.text)
