import numpy as np
from dwave.system import DWaveSampler, EmbeddingComposite
import dwave.inspector as inspector

# Creamos una instancia de problema para trabajar
U = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
size_U = len(U)

subarray1 = np.array([1,4,7, 8])
subarray2 = np.array([1,4, 10,11])
subarray3 = np.array([4,5,7, 11])
subarray4 = np.array([2,3,5,6, 14, 15])
subarray5 = np.array([2,3,6,7])
subarray6 = np.array([2,7, 8,10])
subarray7 = np.array([9,10,11,12,13])
subarray8 = np.array([1,6,8,9])
subarray9 = np.array([15])
subarray10 = np.array([13,15])
subarray11 = np.array([3,9,14])

subarrays = np.array([subarray1,subarray2,subarray3,subarray4, subarray5, subarray6, subarray7,subarray8, subarray9, subarray10,subarray11], dtype=object)
num_subarrays = subarrays.size

# → A
matriz_de_cantidades = np.zeros((size_U,num_subarrays))

for i in range(size_U):
    for j in range(num_subarrays):
        if U[i] in subarrays[j]:
            matriz_de_cantidades[i][j]= 1

# print("Matriz de cantidades: \n",matriz_de_cantidades)
cant_1_col = np.count_nonzero(matriz_de_cantidades ==1, axis=0)
q_a= np.diag(-cant_1_col)

for i in range(size_U):
    for j in range(num_subarrays-1):
        for k in range(num_subarrays-1-j):
            if matriz_de_cantidades[i][j] == 1 and matriz_de_cantidades[i][j+k+1]==1:
                q_a[j][j+k+1] = q_a[j][j+k+1] +1
                q_a[j+k+1][j] = q_a[j+k+1][j] +1
                            
print("Q_a: \n",q_a)

# → B
q_b = np.identity(num_subarrays)

# Armamos el modelo:
a = 5
b = 1
qubo = a * q_a + b * q_b

# Elejimos el sampler de Dwave que queremos
sampler_manual = DWaveSampler(solver={'topology__type': 'chimera'})
# Usamos el EmbeddingComposite con nuestro sampler
embedding = EmbeddingComposite(sampler_manual)
#Corremos nuestra matriz
sampleset = embedding.sample_qubo(qubo, num_reads=20)
#Inspeccionar cosas
inspector.show(sampleset)

# Acá imprime las soluciones encontradas con las energías
print(sampleset)
