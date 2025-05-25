# proyecto
Esta es una aplicación web interactiva construida con **Streamlit** para explorar un conjunto de datos de anuncios de venta de coches en Estados Unidos. Los datos provienen de un archivo CSV llamado `vehicles_us.csv`, que contiene información como el precio, el kilometraje, el modelo del vehículo, el tipo de combustible, la condición, y otros detalles relevantes.

## Funcionalidades

-Visualización interactiva de los datos mediante gráficos construidos con **Plotly Express**.
-Puedes generar:
- Un **histograma** de la columna `odometer`, que muestra la distribución del kilometraje de los vehículos.
- Un **gráfico de dispersión** de `odometer` frente a `price`, para observar posibles relaciones entre el kilometraje y el precio.
-La interfaz contiene:
-Un **encabezado** que introduce la aplicación.
 -**Botones** o **casillas de verificación** que permiten construir los gráficos interactivamente.

## Cómo usar la aplicación

1. Asegúrate de tener `Python` y `Streamlit` instalados.
2. Coloca el archivo `vehicles_us.csv` en el mismo directorio que `app.py`.
3. Ejecuta la aplicación desde la terminal con:

streamlit run app.py