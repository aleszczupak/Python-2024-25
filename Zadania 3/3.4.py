#import sys

while True:
    f = input("Wpisz liczbę rzeczywistą lub 'stop' jeśli chcesz zakończyć:\n")
    if f == 'stop':
        break
        #sys.exit(0)
    try: num = float(f)
    except: # też działa
    #except ValueError:
        print('To nie liczba!')
        continue
    print(num, pow(num, 3))
