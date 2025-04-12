# Criterios de Aceptación y Rechazo

## Historia de Usuario 1: Iniciar sesión exitosamente

**Como** usuario estándar  
**Quiero** iniciar sesión con credenciales válidas  
**Para** acceder al listado de productos disponibles.

### ✅ Criterios de aceptación:
- El sistema permite el acceso con el usuario `standard_user` y contraseña `secret_sauce`.
- Después del login, se redirige automáticamente a la página con el título **“Products”**.
- La lista de productos se muestra correctamente.

### ❌ Criterios de rechazo:
- Si las credenciales son incorrectas, no debe avanzar de página.
- Si falta el usuario o la contraseña, debe mostrarse un mensaje de error.

---

## Historia de Usuario 2: Agregar producto al carrito

**Como** usuario logueado  
**Quiero** poder agregar productos al carrito  
**Para** poder comprarlos más adelante.

### ✅ Criterios de aceptación:
- El botón “Add to cart” debe cambiar a “Remove” tras agregar un producto.
- El contador del carrito debe reflejar el número de productos añadidos.
- El producto debe aparecer en el carrito si se accede al mismo.

### ❌ Criterios de rechazo:
- Si el botón no reacciona, la prueba falla.
- Si el contador del carrito no aumenta, es un fallo.
- Si el producto no aparece dentro del carrito, no se acepta.

---

## Historia de Usuario 3: Visualizar detalles de un producto

**Como** usuario  
**Quiero** ver información detallada de un producto  
**Para** conocer su nombre, descripción y precio.

### ✅ Criterios de aceptación:
- Al hacer clic en el nombre del producto, se debe cargar su detalle.
- Se debe mostrar el nombre, descripción y precio correctamente.
- El precio debe incluir el símbolo **“$”**.

### ❌ Criterios de rechazo:
- Si el nombre o precio están vacíos o incorrectos.
- Si la navegación a los detalles no funciona.

---

## Historia de Usuario 4: Filtrar productos por precio (menor a mayor)

**Como** usuario  
**Quiero** ordenar los productos por precio de menor a mayor  
**Para** facilitar mi decisión de compra.

### ✅ Criterios de aceptación:
- Debe existir un desplegable con la opción “Price (low to high)”.
- Al seleccionar la opción, los productos deben reorganizarse correctamente.
- Los precios deben estar ordenados ascendentemente.

### ❌ Criterios de rechazo:
- Si la opción no existe.
- Si el orden de los precios no cambia o no es correcto.

---

## Historia de Usuario 5: Iniciar el proceso de checkout

**Como** usuario  
**Quiero** iniciar el proceso de checkout desde el carrito  
**Para** completar una compra.

### ✅ Criterios de aceptación:
- Desde el carrito, al hacer clic en “Checkout” se debe navegar al paso 1.
- La página debe mostrar el título “Checkout: Your Information”.
- Se debe permanecer en el flujo sin errores de navegación.

### ❌ Criterios de rechazo:
- Si no redirige correctamente al checkout.
- Si la sección de información del usuario no se muestra.
- Si el producto no fue añadido previamente y se intenta checkout.
