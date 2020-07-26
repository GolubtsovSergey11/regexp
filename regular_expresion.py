import re
from pprint import pprint
import csv

with open('phonebook_raw.csv', encoding='utf-8') as fi:
    rows = csv.reader(fi, delimiter=',')
    contact_list = list(rows)

def name(contact_list):
    name_list = []

    patter = re.compile(r'(^[А-Я]?[а-я]*)\W([А-Я]?[а-я]*)\W([А-Я]?[а-я]*)')
    name_group = r'\1, \2, \3'
    for i in contact_list:
        i = ','.join(i)
        name = [patter.sub(name_group, i)]
        name_list.append(name)
        name_list = name_list
    return name_list

def number_phone(contact_list):
    number_phone = []
    patter = re.compile(r'(\+7|8)(\s?\(?)(\d{3})(\)?\s?|-?)(\d{3})-?(\d{2})-?(\d{2})(\s*\(?(доб\.)\s)?(\d{4})?\)?')
    phone_group = r' +7(\3)-\5-\6-\7 \9\10'
    for i in contact_list:
        i = ','.join(i)
        phone = patter.sub(phone_group, i)
        number_phone.append(phone)
    return number_phone


phone_book = number_phone(name(contact_list))

#print(phone_book)

def duplikat(contact_list):
    new_contact_list = []
    for contact in contact_list:
        contact = ''.join(contact)
        contact = contact.split(',')
        new_contact_list.append(contact)

    for contact in new_contact_list:
        while contact[3] == '':
            del (contact[3])
    name_list = []
    set_contact = []
    for i in new_contact_list:
        if i[0] not in name_list:
            name_list.append(i[0])
            set_contact.append(i)
    return set_contact


contact_list = duplikat(phone_book)

pprint(contact_list)

with open('phonebook.csv', 'w', encoding='utf-8') as fi:
    file = csv.writer(fi, delimiter=',')
    file.writerows(contact_list)