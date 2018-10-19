## Break Statement
#In FOR LOOP
for i in range(10):
    if i == 7:
        print("break execution")
        break
    print(i)
print("loop end \n")

#In WHILE LOOP
i = 1
while(i<=10):
    if i == 7:
        print("break execution")
        break
    print(i)
    i = i+1
print("loop end \n")

## Continue statement
#In FOR LOOP
for i in range(10):
    if i == 7:
        print("continue execution")
        continue
    print(i)
print("loop end \n")
#In WHILE LOOP
i = 0
while(i<=10):
    if i == 7:
        print("continue execution")
        i = i+1
        continue
    print(i)
    i = i+1
print("loop end \n")


### PASS STATEMENT ###
#In FOR LOOP
for i in range(10):
    if i == 7:
        print("pass execution")
        pass
    print(i)
print("loop end \n")
#In WHILE LOOP
i = 0
while(i<=10):
    if i == 7:
        print("pass execution")
        i = i+1
        pass
    print(i)
    i = i+1
print("loop end \n")
