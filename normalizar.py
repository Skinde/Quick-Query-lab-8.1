import math


def normalizar(vector):
    vector2 = []
    for i in range(len(vector)):
        vector2.append(math.log10(vector[i] + 1))
    return vector2

def producto_punto(vector1, vector2):
    output = []
    if (len(vector1) == len(vector2)):
        for i in range(len(vector1)):
            output.append(vector1[i]*vector2[i])
    else:
        print("Different sizes!")   
    return output

def sumatoria_cuadratica(vector):
    sumatoria = 0
    for i in range(len(vector)):
        sumatoria = sumatoria + vector[i]*vector[i]
    return sumatoria

def sumatoria(vector):
    sum = 0
    for n in vector:
        sum = n + sum
    return sum

def producto_punto_sum(vector1, vector2):
    valor = sumatoria(producto_punto(vector1, vector2))
    return valor
def cosine(vector1, vector2):
    valor = (sumatoria(producto_punto(vector1, vector2)))/(math.sqrt(sumatoria_cuadratica(vector1)*sumatoria_cuadratica(vector2)))
    return valor

q = [1.452, 0, 2.122, 3.564, 4.123, 0, 0, 2.342, 0, 0, 0, 1.975, 4.543, 0, 6.134, 2.234]
d1 = [0, 2.093, 0, 0, 4.245, 1.234, 0, 0, 0, 0, 2.345, 0, 2.135, 0, 0, 3.456]
d2 = [0, 1.345, 1.453, 1.987, 0, 2.133, 0, 0, 0, 0, 0, 0, 3.452, 0, 0, 4.234]

q_normal = normalizar(q)
d1_normal = normalizar(d1)
d2_normal = normalizar(d2)




print(producto_punto_sum(q_normal, d1_normal))
print(producto_punto_sum(q_normal, d2_normal))
print(cosine(q_normal,d1_normal))
print(cosine(q_normal, d2_normal))