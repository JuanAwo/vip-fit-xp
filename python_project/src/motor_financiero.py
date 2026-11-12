TOLERANCIA = 1e-6


def calcular_van(inversion_inicial: float, tasa_descuento: float, flujos_caja: list[float]) -> float:
    if inversion_inicial <= 0:
        raise ValueError("La inversión inicial debe ser mayor a cero.")
    if tasa_descuento <= -1:
        raise ValueError("La tasa de descuento debe ser mayor a -1.")
    if not flujos_caja:
        raise ValueError("La lista de flujos de caja no puede estar vacía.")

    van = -inversion_inicial
    for t, flujo in enumerate(flujos_caja, start=1):
        van += flujo / ((1 + tasa_descuento) ** t)
    return van


def calcular_tir(inversion_inicial: float, flujos_caja: list[float]) -> float | None:
    lim_inf = -0.99
    lim_sup = 10.00
    max_iter = 1000

    van_inf = calcular_van(inversion_inicial, lim_inf, flujos_caja)
    van_sup = calcular_van(inversion_inicial, lim_sup, flujos_caja)

    if van_inf * van_sup > 0:
        return None

    for _ in range(max_iter):
        punto_medio = (lim_inf + lim_sup) / 2
        van_medio = calcular_van(inversion_inicial, punto_medio, flujos_caja)

        if abs(van_medio) <= TOLERANCIA:
            return punto_medio

        if van_inf * van_medio < 0:
            lim_sup = punto_medio
            van_sup = van_medio
        else:
            lim_inf = punto_medio
            van_inf = van_medio

    return None


def evaluar_van(van: float) -> str:
    if abs(van) <= TOLERANCIA:
        return "Indiferente"
    return "Viable" if van > 0 else "No viable"


def evaluar_tir(tir: float, tasa_descuento: float) -> str:
    if abs(tir - tasa_descuento) <= TOLERANCIA:
        return "Indiferente"
    return "Aceptable" if tir > tasa_descuento else "Insuficiente"


def generar_dictamen(eval_van: str, eval_tir: str) -> str:
    matriz = {
        ("Viable", "Aceptable"): "Viable",
        ("Viable", "Indiferente"): "Viable con observación",
        ("Viable", "Insuficiente"): "Viabilidad condicionada",
        ("Indiferente", "Aceptable"): "Viable con observación",
        ("Indiferente", "Indiferente"): "Indiferente",
        ("Indiferente", "Insuficiente"): "No recomendable",
        ("No viable", "Aceptable"): "Viabilidad condicionada",
        ("No viable", "Indiferente"): "No recomendable",
        ("No viable", "Insuficiente"): "No viable",
    }
    return matriz.get((eval_van, eval_tir), "Análisis incompleto")