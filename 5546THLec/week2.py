import math
f = 0.2 + 0.2 + 0.2
print(math.isclose(0.6))

x = str('abc')
xup = str.upper(x)
print(xup)  # --> 'ABC'

y = 'abc'.upper()
print(y)  # --> 'ABC'

# Downloads Qantas share price beginning 1 January 2020
import yfinance                                           # (1)
tic = "QAN.AX"                                            # (2)
start = '2020-01-01'                                      # (3)
end = None                                                # (4)
df = yfinance.download(tic, start, end, ignore_tz=True)   # (5)
print(df)                                                 # (6)
df.to_csv('qan_stk_prc.csv')                              # (7)


L = 56
W = 33
H = 30.5
V = L*W*H
print(V)
print(f"the volume of the ox is {V} cubic ccentimeters.")
print("the volume of the box is {} cubic centemeters".format(V))


# write a short program to get teh email domain name of the following example
line = 'From firstname.surname@unsw.edu.au Tue Oct 06 10:10:15 2020'
domain = line.split()[1].split('@')[1]
print(domain)

#in-class exercise
hours = int(input("working_hours"))
if hours <= 35:
    rate = 51.45
    weekly_pay = hours * rate
    print(weekly_pay)
else:
    rate = 88.9
    weekly_pay = hours * rate
    print(weekly_pay)

f_suburbs = {"Randwick": 29986, "Kensington": 15004, "Frenchs Forest": 13473, "Flemington": None}
f_suburbs.pop("Kensington")
f_suburbs.pop("Randwick")
print(f_suburbs)

list_a = ['this', 'list', 'has', 'bad', 'words', 'in', 'it', 'bad', 'naughty', 'impish']
list_b = ['good', 'nice', 'friendly']
# 1. Create a new list called sol (for solution) consisting of a slice
#    from list_a from the second element through to the word 'it'
sol = list_a[1:7]
# 2. Remove the value 'bad' from sol
sol.remove('bad')
# 3. Add a value 'including' so that it is the last value in sol
sol.append('including')
# 4. Add a value 'good' so that it is the third value in sol
sol.insert(2,'good')
# 5. Add all elements from list_b to the end of sol
sol.extend(list_b)
print(sol)

f_suburbs = {"Randwick": 29986, "Kensington": 15004, "Frenchs Forest": 13473, "Flemington": None}
f_suburbs.pop("Kensington")
f_suburbs.pop("Randwick")
# 2. Ensure that your dictionary contains:
f_suburbs.update({
     'Fairfield': 18081,
     'Fairfield East': 5273,
     'Fairfield Heights': 7517,
     'Fairfield West': 11575,
     'Fairlight': 5840,
     'Fiddletown': 233,
     'Five Dock': 9356,
     'Flemington': None,
     'Forest Glen': None,
     'Forest Lodge': 4583,
     'Forestville': 8329,
     'Freemans Reach': 1973,
     'Frenchs Forest': 13473,
     'Freshwater': 8866,
})
print(f_suburbs)

number=[3,9,1,5,7,2,11,0,3,12,3,15]
largest = number[0]
for n in number:
    if n>= largest:
        largest = n
print(largest)
