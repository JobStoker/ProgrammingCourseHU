inputoldpassword = input('Input your old password: ')
inputnewpassword = input('Input your new password: ')

def new_password(oldpassword, newpassword):
    if newpassword != oldpassword and len(newpassword) >= 6 and newpassword.isalpha() == False:
        return True
    else:
        return False

print(new_password(inputoldpassword, inputnewpassword))