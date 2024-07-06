# Control2Progra
Temporal repository for the 2nd test of EL4203-1. \\ Repositorio temporal para el segundo control de EL4203-1 "Programación Avanzada".

En este repositorio se presentan 3 programas relacionados a cada apartado del enunciado. \
La recomendación es que ejecuten estos programas a través del "programa_master.py". Al ejecutar este programa maestro, se le darán 3 opciones al usuario, cada opción para ejecutar el programa de cada punto.

A continuación, se presenta una breve descripción de las funciones:\
\
"function1.py" justifica el texto entregado dado un máximo ancho de línea. No es 100% eficiente utilizando los espacios, pero se intentó.\
\
"function2.py" es un programa que utiliza otras 5 funciones que están definidas en "DP_functions.py" y "CRUD_file.py". Con esas funciones lee un archivo de texto entregado por el usuario, por medio de input(), 
luego de tener el archivo cargado, le pregunta al usuario qué quiere hacer.\
La primera opción es encontrar el "Longest Common Substring" entre el texto del archivo y un texto entregado por el usuario mediante input().\
La segunda opción ejecuta "Word Break" entre el texto del archivo y el string entregado por el usuario median input(). \
La tercera opción ejecuta "Word Wrap", retornando el mínimo costo de "wrapear" el texto del archivo en el largo de línea entregado mediante input().\
La cuarta opción ejecuta "function1.py" para el texto entregado y pide el largo de línea al usuario.\
\
"function3.py" ejecuta las funciones CRUD para un archivo de texto entregado (mediante input()), dándole la opción al usuario de elegir si quiere Crear (C), Leer (R), Actualizar (U) o Eliminar (D) cierto texto del archivo. No crea archivos de texto de cero, solo los modifica.\
"Crear" anexa el texto entregado por el usuario al final del archivo.\
"Leer" simplemente muestra todo el texto del archivo.\
"Actualizar" busca cierto texto entregado por el usuario y lo modifica por otro texto entregado por el usuario.\
"Eliminar" busca y elimina el texto entregado por el usuario del texto del archivo.\


### Comentarios sobre el enunciado
La verdad el enunciado es muy ambigüo, y no se entiende muy bien qué hay que hacer y qué cosas requieren las funciones, sobretodo del punto 2 y 3. ¿El punto 3 requiere DP? El punto 3 dice que sólo debe ser capaz de ejecutar funciones CRUD sobre
el texto dado un archivo, y eso es lo que hice.\
\
También el punto 2 dice "la habilidad de una función debería ser ...". ¿Por qué se enuncia de esa manera? Podría decir "Haga una función que utilice los 3 tipos de DP dado un archivo de texto entregado". Ni siquiera sé si debería 
crear yo las funciones DP o las puedo sacar literalmente de las referencias porque no lo indica. Por lo tanto, modifiqué las funciones de las referencias para ese punto.\
\
Por último, en el punto 1 dice que hay que realizar las "`format_text` functions efficiently ", ¿acaso quiere decir que hay más de una función "format_text"?\
\
Eso es todo el rant, que tengan un buen fin de semestre!
