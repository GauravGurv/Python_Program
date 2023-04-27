import re               #regit module is used to pass multiple condition
email_cond="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
# \._ =
user=input("Enter Your E-Mail: - ")

if re.search(email_cond,user):
    print("E-Mail is Valid")
else:
    print("E-mail is not Valid")