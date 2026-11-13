export function validarDocumento(documento) {
    const regex = /^[0-9]{6,12}$/;
    return regex.test(String(documento));
}

export function validarCorreo(correo) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(String(correo));
}

export function calcularFechaVencimiento(fechaInicioISO, diasDuracion) {
    const fecha = new Date(`${fechaInicioISO}T00:00:00Z`);
    fecha.setUTCDate(fecha.getUTCDate() + diasDuracion);
    return fecha.toISOString().split('T')[0];
}

export function calcularDescuentoMembresia(precioBase, porcentajeDescuento) {
    if (porcentajeDescuento < 0 || porcentajeDescuento > 100) {
        throw new Error('Error: El porcentaje de descuento debe estar entre 0 y 100');
    }
    return precioBase - (precioBase * (porcentajeDescuento / 100));
}

export function obtenerEstadoMembresia(fechaVencimientoISO, fechaActualISO) {
    return fechaActualISO <= fechaVencimientoISO ? 'Activa' : 'Vencida';
}

export function formatearMonedaCOP(valor) {
    return new Intl.NumberFormat('es-CO', {
        style: 'currency',
        currency: 'COP',
        maximumFractionDigits: 0
    }).format(valor);
}