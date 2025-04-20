full_name = input("Enter a full name: ")
phone = input("Enter phone number: ")
email = input("Enter email-id: ")

vcard = f'''
NAME : {full_name}
PHONE NUMBER : {phone}
EMAIL ID :{email}
'''

v_card_obj = open('vcard.vcf','w+',encoding='utf-8')
v_card_obj.write(vcard)

v_card_obj.close()

print("task completed")

#OUTPUT:
# Enter a full name: Ved Pramod Patel
# Enter phone number: 9192^^^^^^
# Enter email-id: xyz@trollmedia.com
# task completed
