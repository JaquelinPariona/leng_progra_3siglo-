#  operaciones aritmeticas con numeros en python 
# 1. suma - operador binario
# Variables Globales
## Son datos que se utilizar en cualquier parte del software que este construyendo
# Variables Locales
## Son datos que solo son accesibles en pequeñas porciones de codigo o "scope".
firts_numb:int|float=20
second_numb:int|float=5
# Resultado 
print(f"la suma de {firts_numb}+{second_numb}es{firts_numb+second_numb}")
print(f"la resta de {firts_numb}-{second_numb}es{firts_numb-second_numb}")

# Divi
print(f"la divicion de {firts_numb}/{second_numb}es{firts_numb/second_numb}")

# Multiplicacion
print(f"la multide {firts_numb}*{second_numb}es{firts_numb*second_numb}")

# Divicion exacta
print(f"la diviexac de {firts_numb}//{second_numb}es{firts_numb//second_numb}")

## Incremento (++,+=) OJO: Esta es una avreviatura de  (numero=numero+1 , numero+=1)
print(f"el incremento de {firts_numb} es {++firts_numb}")

## Decremento (--,+=) (numero=numero-1 , numero-=1)
print(f"el decremento de {firts_numb} es {--firts_numb}")

## Potenciacion 
print(f"el poten de {firts_numb} es {second_numb}={firts_numb**second_numb}")

# OJO : "hola" +"mundo" -> concatenacion