async function enviarDatos() {
    const mensaje = document.getElementById('mensaje');
    mensaje.textContent = 'Enviando...';
    mensaje.className = 'message';

    try {
        // Cambia esta URL por la de tu servidor
        const response = await fetch('http://localhost:8000', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ parametro: 2 })
        });

        if (response.ok) {
            mensaje.textContent = '✓ Datos enviados correctamente';
            mensaje.className = 'message success';
        } else {
            mensaje.textContent = '✗ Error al enviar datos';
            mensaje.className = 'message error';
        }
    } catch (error) {
        mensaje.textContent = '✗ Error de conexión';
        mensaje.className = 'message error';
        console.error('Error:', error);
    }
}