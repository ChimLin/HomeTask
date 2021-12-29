from re import *

txt = """
    Аудио стоит 1000
    БМВ стоит 8000
    VW стоит 1000
"""
# Возвращает список всех найденных элементов

# lst_pr = re.compile('\d+')
# print(lst_pr.findall(txt))
#
# # search return the podhodyachiq object
#
# re_rool = re.compile("\d+")
# print(re_rool.search(txt))
#
# # sub - zamena
#
# re_r = re.compile('\d+')
# print(re_r.sub('....',txt))

text = "27 December 2021"
print(findall('\D+',text))
print(findall('\w+',text))
print(findall('\d{4}',text))
print(findall("colou?r", ""))
email = "test@mail.ru"
rool_ ='^test@mail.ru$'
print(match(rool_,email))

ip ="1.0.111.4"
r_ip ="^[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[0-9]{1,3}$"
print(findall(r_ip, ip))

print(findall("[\w]{1,}", "asd!ddaa"))