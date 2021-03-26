"""Given 2 strings a and b. a represent the first lane in which vehicles move from left to right. 
The b represents the second lane in which vehicles move from right to left. 
Vehicles can be B (bike), C (car), T (truck). collision will occur only between two trucks. Find the probability of collision."""

a = "TCCBCTTB"
b = "BTCCBBTT"

if len(a) >= len(b):
    n=len(b) 
    tot = n*(n+1)/2
else:
    n = len(a)
    tot = n*(n+1)/2 + (len(b)-len(a))*n


ans = 0
T_in_a_tillNow = 0
for i in range(min(len(a), len(b))):
    if a[i]=='T':
        T_in_a_tillNow+=1
    if b[i]=='T':
        ans+= T_in_a_tillNow
if len(b) > len(a):
    for j in range(i+1, len(b)):
        if b[j]=='T':
            ans+= T_in_a_tillNow


print("{}/{}".format( ans, tot))




