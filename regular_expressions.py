import re
from pprint import pprint
import csv
with open('phonebook_raw.csv', encoding='utf-8', newline='') as f:
  rows = csv.reader(f)
  contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ

pat1 = r'(^\w+)\ (\w+)\ (\w+)'
sub1 = r'\1'

fixed = []
for x in contacts_list:
  result = re.findall(pat1, x[0])
  for x in result:
    arr = list(x)
    for i in arr:
      fixed.append(i)

arrow = []
for x in contacts_list:
  for y in x:
    text = str(y)
    txt = text.split()
    for i in txt:
      arrow.append(i)
    if txt in fixed:
      ind = fixed.index(txt)
      txt = fixed[ind]


# TODO 2: сохраните получившиеся данные в другой файл

csv.register_dialect('my_dialect', delimiter='!', lineterminator=" ")
with open('phonebook.csv', 'w', newline='') as file:
  datawriter = csv.writer(file, 'my_dialect')
  for item in arrow:
    datawriter.writerow([item])

with open('phonebook.csv', newline='') as f:
  rows = csv.reader(f)
  rows_list = list(rows)

pattern = r'((\s,)\w+[ев]|\w+[ов]|\w+[ина])\ ([А-Я][а-я]+)\ ([А-Я][а-я]+)' #names
subst = r'\n\1 \3 \4'
pattern2 = r'(\+7|8)(\s*\(*)(\d{2,3})(\)*|\s*|\-*)\s*(\d{1,3})[\s-]*(\d{2})[\s-]*(\d{2})' #numbers
subst2 = r'+7(\3)\5-\6-\7'
pattern3 = r'(\s*\(*)(\доб.)( )(\d*)(\s|\)\s)' #доб
subst3 = r' \2\4 '

for x in range(len(rows_list)):
  txt2 = str(rows_list[x])
  result = re.sub(pattern, subst, txt2)
  txt2 = result
  result2 = re.sub(pattern2, subst2, txt2)
  txt2 = result2
  result3 = re.sub(pattern3, subst3, txt2)
  txt2 = result3
  print(txt2)
