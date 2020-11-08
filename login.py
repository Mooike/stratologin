import twill.commands as twill

twill.go('https://www.strato.de/apps/CustomerService#/skl')

twill.showforms()

#get username 
with open("creds.txt", "r") as text_file:
    data = text_file.readlines()

print("username: ", data[0])
print("password: ", data[1])

twill.fv("LoginForm", "login", data[0])
twill.fv("LoginForm", "login", data[1])

twill.submit()

print("logged in!")