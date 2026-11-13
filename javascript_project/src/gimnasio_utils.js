const REGEX_DOCUMENTO = /^[0-9]{6,12}$/;
const REGEX_CORREO = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export function validarDocumento(documento) {
    return REGEX_DOCUMENTO.test(String(documento));
}

export function validarCorreo(correo) {
    return REGEX_CORREO.test(String(correo));
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
    const factorDescuento = 1 - (porcentajeDescuento / 100);
    return precioBase * factorDescuento;
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