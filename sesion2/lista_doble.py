

"""
Respuesta pregunta 1: 
El nuevo nodo tendrá su referencia anterior apuntando a la cola vieja, pero la cola vieja no apuntará al nuevo nodo.
Respuesta pregunta 2:
Inicio ↔ Catálogo ↔ Contacto
Contacto ↔ Catálogo ↔ Inicio
Respuesta pregunta 3:
Ambas variables apuntan al mismo nodo porque es el primero y también el último. Sus referencias anterior y siguiente permanecen en None.
Respuesta pregunta 4:
Eliminar el primer nodo, el último y el único nodo, porque en ellos se deben actualizar cabeza o cola, además de las referencias de los nodos vecinos. Tu función eliminar() ya contempla correctamente estos casos.

Una recomendación: para comprobar el último caso, creá una lista nueva con un solo nodo, eliminá ese nodo y verificá que ambas variables queden en None.
"""