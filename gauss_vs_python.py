#!/usr/bin/env python

from alive_progress import alive_bar

def sum_trad(x):
    return sum(range(x + 1))

def sum_gauss(x):
    return (x / 2) * (x + 1)

def compara_trad_gauss(x):
    # print(f'x={x} : {sum_trad(x)} vs {sum_gauss(x)}')
    return sum_trad(x) == sum_gauss(x)

def gauss_vs_python(r):
    
    hipotesis = True
    print(f'Probando la formula de Gauss con el rango de numeros 0-{r}')   

    with alive_bar(r + 1) as bar:

        for x in range(r + 1):
            
            if not compara_trad_gauss(x):
                hipotesis = False
                print(f'Error para x = {x}')
                break
            
            bar()

    if hipotesis:
        print('Prueba exitosa, mis respetos forever Gauss!')
    else:
        print('Gauss... eres un fraude!')

if __name__ == '__main__':
    
    r = int(input('Valor de r: '))
    gauss_vs_python(r)
