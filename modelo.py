import tensorflow as tf
import numpy as np 

#entradas y salidas
celsius = np.array([-40,-10,0,8,15,22,38],dtype=float)
fahrenheit = np.array([-40,14,32,46,59,72,100], dtype=float)

#dense es la capa principal del modelo
capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

modelo.compile(
    optimizer = tf.keras.optimizers.Adam(0.1),
    loss = 'mean_squared_error'

)

#entreno
print("Comenzando entrenamiento...")
historial = modelo.fit(celsius, fahrenheit, epochs=1000,verbose=False)
print("modelo entrenado!!")

#guardo la arquitectura del modelo
modelo.save('modelo.h5')

#print("prueba del modelo")
#resultado = modelo.predict([100.0])
#print("result:" + str(resultado))