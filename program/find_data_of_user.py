my_dict = {
    "nitin":20241094,
     'abhi':2024111,
     'rahul':123456765,
     'sinu':7346647,
}
user = input("enter user info : ")
if user in my_dict:
    print("phone",my_dict[user])
else:
    print('invalid user input')
   