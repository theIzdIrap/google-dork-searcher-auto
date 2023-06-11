a = input("the word u wanna search for : ")
b = input("Which domain u searching for (e.g. google.com google.co.in) write a com,org,tk or something : ")
c = int(input("How many results you want MIN : "))
d = int(input("How many results you want MAX : "))
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")


query = a

for j in search(query, tld=b, num=c, stop=d, pause=2):
    print(j)
