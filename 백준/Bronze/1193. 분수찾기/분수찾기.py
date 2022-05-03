n = int(input())

line = 0
end = 0
while n > end:
    line += 1
    end += line

num = end-n
if line%2 == 0:
    top = line - num
    bottom = num + 1
else:
    top = num + 1
    bottom = line - num
    
print(f'{top}/{bottom}')