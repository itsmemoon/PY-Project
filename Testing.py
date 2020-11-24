print ('Question 3a')
a = True;
if a == True:
    print ('a result is true');

print ('Question 3b')
b = 5;
if b <=5:
    print('b is less or equal to 5');

print ('Question 4')
a,b = 5,6
if a is not b:
    print('a is not b is true')
print(" ")

print ('Question 5')
a,b = 5,10
if a > 5 and b > 5 :
    print('a and b is greater than 5')
elif a > 5 or b > 5 :
    print('a or b is greater than 5')
else:
    print('a and b is lesser or equal to 5) # try to change b to value less or equal to 5')
print(" ")

print ('Question 6')
n = 6
current_sum = 0
i = 0
while i <= n:
    current_sum += i
    i += 1
    print(current_sum)
print(" ")

print ('Question 7')
myFriends = ['Joe', 'Zoe', 'Alvin', 'Paris']
for friend in myFriends:
    invite = 'Hi ' + friend + '. Please come to my party!'
    print(invite)
print(" ")

print ('Question 8')
dict = {}
dict['one'] = 'This is one'
dict[2] = 'This is two'
tinydict = {'name': 'john', 'code':6734, 'dept': 'sales'}
print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())
print(" ")

dictionary_tk = { "name": "Leandro", "nickname": "Tk", "nationality": "Brazilian", "age": 24 }
for attribute, value in dictionary_tk.items():
    print("My %s is %s" %(attribute, value))
print(" ")

print ('Question 9')
numbers = [10,5,24,8,6]
for number in numbers:
    if number % 2 == 1:
        print(True)
        break
    else: print(False)
print(" ")

numbers = [10,5,24,8,6]
for number in numbers:
    if number % 2 == 1:
        print(True)
        continue
    else:
        print(False)

print ('Question 10 Challenge')
n = 6
current_sum = 0
i = 0
while i <= n:
    current_sum += i
    i += 1
    continue;

print (current_sum);

