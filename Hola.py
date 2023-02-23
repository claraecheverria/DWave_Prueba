#Importamos numpy para crear nuestras matrices
import numpy as np
# El DWaveSampler es lo que corre y el EmbeddingComposite sirve para pasar la matriz QUBO a la computadora de D-Wave
from dwave.system import DWaveSampler, EmbeddingComposite
# El inspector nos permite ver más lindo todo los grafos de la implementación en la computadora
import dwave.inspector as inspector

#Aca esta la matriz que nosotros conseguimos con nuestro trabajo de QUBO
matriz = np.identity(4)

# Elejimos el sampler de Dwave que queremos
sampler_manual = DWaveSampler(solver={'topology__type': 'chimera'})
# Usamos el EmbeddingComposite con nuestro sampler
embedding = EmbeddingComposite(sampler_manual)
#Corremos nuestra matriz
sampleset = embedding.sample_qubo(matriz, num_reads=2)
#Inspeccionar cosas
inspector.show(sampleset)

# Acá imprime las soluciones encontradas con las energías
print(sampleset)

