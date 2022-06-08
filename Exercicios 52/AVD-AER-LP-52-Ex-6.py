x=str(input("Digite uma palavra:"))
sub=''

if "1" in x:
    sub = (x.replace("1", "11"))

if "2" in x:
    sub = (sub.replace("2", "22"))

if "3" in x:
    sub = (sub.replace("3", "33"))

if "4" in x:
    sub = (sub.replace("4", "44"))

if "5" in x:
    sub = (sub.replace("5", "55"))

if "6" in x:
    sub = (sub.replace("6", "66"))

if "7" in x:
    sub = (sub.replace("7", "77"))

if "8" in x:
    sub = (sub.replace("8", "88"))

if "9" in x:
    sub = (sub.replace("9", "99"))

if "0" in x:
    sub = (sub.replace("0", "00"))

print(sub)


