# Calculadora Básica – Prácticas de Calidad de Software

## Descripción
el proyecto consite en una calculadora basica desarollada en python, se pueden realizar las siguentes operaciones
* Suma
* Resta
* Multiplicacion
* Division

El objetivo del proyecto es aplicar practicas de calidad de software

## practicas de calidad aplicadas

### 1. Coding Standards

Se utilizo **Ruff** como herramienta de formateo de código
La configuracion se encuentra definida en el archivo `pyproject.toml`
Para verificar el código se utiliza:

```bash
ruff check .
```

Para aplicar el formato automáticamente:

```bash
ruff format .
```

### ¿Qué problema evita?

 permite detectar problemas de estilo, imports incorrectos, código inconsistente y algunos errores antes de integrar los cambios al proyecto

### Relacion con lo discutido en clase

Esta practica permite integrar calidad durante el desarrollo en lugar de revisar todos los problemas únicamente al finalizar el proyecto

### 2. Pull Request y Code Review

Para realizar cambios en el proyecto se creo una rama independiente de `main` llamada :

feature/add-validation

una vez realizados los cambios se hizo una *pull request* a la rama principal para que ser revisada y despues aprobada

### ¿Qué problema evita?

 Pull request nos permite revisar el codigo agragado o modificado, antes de integrarlos al codigo princiopal

El Code review ayuda a detectar:
* Errores de lógica.
* Problemas de mantenibilidad.
* Código innecesario.
* Posibles defectos.
* Incumplimiento de estándares.

Esto reduce la posibilidad de introducir errores directamente en la rama principal.

### Relación con lo discutido en clase

El Pull Request y el Code Review promueven una integracion progresiva y controlada

en vez de hacer grandes archivos de codigo y unirlos al final, se opta por hacer cambios pequeños progresivamente asi evitar errores de compatibilidad al querer unir todo el codigo a ultima hora

Esto ayuda a evitar el **Big Bang** y reduce las posibilidades de retrabajar el codigo

---

## Practica adicional: pruebas automatizadas

Tambien se utilizaron pruebas automatizadas con **pytest** para comprobar el funcionamiento de las operaciones de la calculadora

Las pruebas se ejecutan utilizando:

```bash
pytest
```

Las pruebas verifican las operaciones matematicas y tambien casos especiales, como intentar dividir entre cero



