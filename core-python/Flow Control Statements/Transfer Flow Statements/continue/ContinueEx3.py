#ContinueEx3.py
s="PYTHON"
print("By using for loop")
for ch in s:
    print(ch)
else:
    print("i am from else part of for loop")
print("-----------------------------------------")
#My Reqriment is to display :  PYHN
print("By using for loop with continue stmt")
for ch in s: # s="PYTHON"
    if ch in ["T","O"]:
        continue
    print(ch,end="")
else:
    print("\ni am from else part of for loop")
print("-----------------------------------------")