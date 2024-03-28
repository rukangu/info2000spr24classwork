# this demonstrates advanced unpacking
# we convert currencies into USD

# def Converter(kes, gpb, eur, yen, yuan, inr, peso): 
#     return kes*0.0076 + gpb*1.26 + eur*1.08 + yen*0.0066 + yuan*0.14 + inr*0.012 + peso * 0.06

# # wallet = [1000, 500, 80,150,200,8000]

# # usd = Converter(wallet[0], wallet[1], wallet[2],wallet[3],wallet[4],wallet[5])
# # usd = Converter(*wallet)
wallet = {'gpb':500, 'eur':80,'yen':150,'yuan':200,'inr':8000, 'kes':1000, 'peso':2000}

# # usd = Converter(wallet['gpb'],wallet['kes'] , wallet['eur'], wallet['yen'], wallet['yuan'], wallet['inr'])
# usd = Converter(**wallet)

# # usd = Converter(gpb = 500, eur = 80,yen = 150, yuan = 200,inr = 8000, kes = 1000, peso =2000)
# print(f"You have {usd:.2f} $")


def GenericFunction(*args, **kwargs):
    print(f"positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")
    print(f"{kwargs['gpb']} pounds!") 

GenericFunction(1,2,4,4,5,6,**wallet)


