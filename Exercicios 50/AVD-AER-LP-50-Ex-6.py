x=str(input("Digite uma palavra ou uma frase:"))

if "a" in x or "A" in x:
    sub = (x.replace("a", "aa"))
    sub = (sub.replace("A", "AA"))

if "e" in x or "E" in x:
    sub = (sub.replace("e", "ee"))
    sub = (sub.replace("E", "EE"))

if "i" in x or "I" in x:
    sub = (sub.replace("i", "ii"))
    sub = (sub.replace("I", "II"))

if "o" in x or "O" in x:
    sub = (sub.replace("o", "oo"))
    sub = (sub.replace("O", "OO"))

if "u" in x or "U" in x:
    sub = (sub.replace("u", "uu"))
    sub = (sub.replace("U", "UU"))

print(sub)

