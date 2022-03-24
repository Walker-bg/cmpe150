def multiplePrinter(string, times):
    if times == 0:
        return ''
    return string+multiplePrinter(string, times-1)

print(multiplePrinter("hello", 3))
print(multiplePrinter("this is fun", 1))
print(multiplePrinter("wow", 0))
print(multiplePrinter("hi ho! ", 5))