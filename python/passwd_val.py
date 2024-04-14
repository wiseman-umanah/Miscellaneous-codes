def main(password):
    num = spec = 0
    for i in password:
        if i.isdigit():
            num  += 1
        elif i in special:
            spec += 1
    return (num, spec)


special = ['!', '@', '#', '$', '%', '&', '*']
num = spec = 0

password = input()
num, spec = main(password)

if len(password) < 7:
    print("Weak")
else:
    if num < 2 or spec < 2:
        print("Weak")
    else:
        print("Strong")
