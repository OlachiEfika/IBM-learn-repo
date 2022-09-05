# I challenged myself to learn python this year. I am enjoying learning using Python for Everyone (PY4E) resources
print('Hello World! is not the only thing I have learnt')
print('I  have also learnt about variables, expressions, statements and conditional executions')
print('My next lesson is on Functions')
print('See sample code of my learning below')

score = input("Enter Score: ")
score = float(score)
if score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
elif score < 0.6:
    print('F')
else: print('Try again next year')
