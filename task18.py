
with open("Input/students.txt","r") as infile, open("output/output18.txt") as outfile:

    names = list(map(str.title,infile.read().split()))

    your_name = input("Ismingiz ").strip().title()

    if your_name in names:
        outfile.write(f"{your_name} ism bor")
    else:
        outfile.write(f"{your_name} ismi yoq")
