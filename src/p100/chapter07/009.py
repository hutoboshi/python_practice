with open("example.txt", "w") as f:
    print(f.write("サンプルテキスト"))
    print(f.closed)
print(f.closed)