import test from 'node:test';
import assert from 'node:assert';
import {
    validarDocumento,
    validarCorreo,
    calcularFechaVencimiento,
    calcularDescuentoMembresia,
    obtenerEstadoMembresia,
    formatearMonedaCOP
} from '../src/gimnasio_utils.js';

// 1. Validación de documento válido
test('01. Debe aceptar un documento numérico válido', () => {
    assert.strictEqual(validarDocumento('1017234567'), true);
});

// 2. Validación de documento inválido (con letras o muy corto)
test('02. Debe rechazar documentos con letras o longitud insuficiente', () => {
    assert.strictEqual(validarDocumento('ABC12345'), false);
    assert.strictEqual(validarDocumento('123'), false);
});

// 3. Validación de formato de correo electrónico
test('03. Debe validar correctamente el formato de correo electrónico', () => {
    assert.strictEqual(validarCorreo('cliente@vipfit.com'), true);
    assert.strictEqual(validarCorreo('correo_invalido.com'), false);
});

// 4. Cálculo de fecha de vencimiento de plan mensual (30 días)
test('04. Debe sumar correctamente los días de duración de una membresía', () => {
    assert.strictEqual(calcularFechaVencimiento('2026-11-01', 30), '2026-12-01');
});

// 5. Cálculo de descuento por pago anticipado o anual
test('05. Debe aplicar el porcentaje de descuento correctamente al precio del plan', () => {
    assert.strictEqual(calcularDescuentoMembresia(100000, 15), 85000);
});

// 6. Control de límite en descuento (no permite descuentos negativos ni mayores al 100%)
test('06. Debe lanzar error si el porcentaje de descuento está fuera de rango', () => {
    assert.throws(() => calcularDescuentoMembresia(100000, -10), /Error/);
    assert.throws(() => calcularDescuentoMembresia(100000, 120), /Error/);
});

// 7. Estado de membresía activa
test('07. Debe retornar Activa si la fecha actual es anterior al vencimiento', () => {
    assert.strictEqual(obtenerEstadoMembresia('2026-12-15', '2026-11-12'), 'Activa');
});

// 8. Estado de membresía vencida
test('08. Debe retornar Vencida si la fecha actual supera el vencimiento', () => {
    assert.strictEqual(obtenerEstadoMembresia('2026-10-01', '2026-11-12'), 'Vencida');
});

// 9. Estado de membresía en su último día (límite)
test('09. Debe retornar Activa el mismo día de vencimiento', () => {
    assert.strictEqual(obtenerEstadoMembresia('2026-11-12', '2026-11-12'), 'Activa');
});

// 10. Formateo de moneda en pesos colombianos
test('10. Debe formatear un valor numérico como moneda sin decimales', () => {
    const resultado = formatearMonedaCOP(85000);
    assert.ok(resultado.includes('85.000') || resultado.includes('85,000'));
});