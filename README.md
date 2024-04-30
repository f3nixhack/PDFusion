# PDFusion

**Este programa escrito en Python permite fusionar múltiples archivos PDF en un solo archivo PDF.**
![Captura de pantalla 2024-04-30 185258](https://github.com/f3nixhack/PDFusion/assets/50671074/feacd15c-67ee-4ede-bf4e-ebaf3de17288)

**Funcionalidades:**

* **Seleccionar archivos PDF:** Puedes seleccionar varios archivos PDF utilizando un cuadro de diálogo de selección de archivos.
* **Visualizar archivos seleccionados:** Los archivos PDF seleccionados se mostrarán en una lista para su confirmación.
* **Elegir archivo de salida:** Puedes especificar la ubicación y el nombre del archivo PDF fusionado resultante.
* **Combinar archivos PDF:** El programa combina los archivos PDF seleccionados en un solo archivo utilizando la biblioteca `PyPDF2`.
* **Mostrar mensaje de éxito:** Una vez que la fusión se realiza correctamente, se muestra un mensaje de confirmación.
* **Borrar lista de archivos seleccionados:** La lista de archivos seleccionados se borra para preparar la siguiente fusión.
* **Mostrar mensaje de advertencia:** Si no se selecciona ningún archivo de salida, se muestra un mensaje de advertencia.

**Componentes principales:**

* **Librería `tkinter`:** Esta librería se utiliza para crear la interfaz gráfica de usuario (GUI) de la aplicación.
* **Librería `PyPDF2`:** Esta librería se utiliza para manipular archivos PDF, como la lectura y escritura de contenido.
* **Funciones:**
    * `select_files()`: Abre un cuadro de diálogo para seleccionar archivos PDF y los agrega a una lista.
    * `merge_pdfs()`: Combina los archivos PDF seleccionados en un solo archivo y lo guarda en la ubicación especificada.

**En resumen, este programa proporciona una herramienta fácil de usar para fusionar archivos PDF en un solo documento.**
