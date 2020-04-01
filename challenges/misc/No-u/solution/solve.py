flag_file = 'text.txt'
f = open(flag_file, 'rb')
strange_text = f.read().decode()[::-1]
print(strange_text)
f.close()

solution_file = 'solve.txt'
f = open(solution_file, 'wb+')
f.write(strange_text.encode())
f.close()