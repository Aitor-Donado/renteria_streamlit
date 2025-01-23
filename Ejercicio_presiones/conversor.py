def convertir_a_atmosferas(valor, unidad):
    if unidad == "mm de mercurio":
        return valor / 760
    elif unidad == "milibares":
        return valor / 1013.25
    else:
        return valor

def convertir_a_mm_de_mercurio(valor, unidad):
    if unidad == "atmósferas":
        return valor * 760
    elif unidad == "milibares":
        return valor * 760 / 1013.25
    else:
        return valor

def convertir_a_milibares(valor, unidad):
    if unidad == "atmósferas":
        return valor * 1013.25
    elif unidad == "mm de mercurio":
        return valor * 1013.25 / 760
    else:
        return valor

def convertir_presion(valor, unidad):
    if unidad not in ["atmósferas", "mm de mercurio", "milibares"]:
        raise ValueError("Unidad no válida. Las unidades permitidas son 'atmósferas', 'mm de mercurio' y 'milibares'.")
    
    atmosferas = convertir_a_atmosferas(valor, unidad)
    mm_de_mercurio = convertir_a_mm_de_mercurio(valor, unidad)
    milibares = convertir_a_milibares(valor, unidad)
    
    return atmosferas, mm_de_mercurio, milibares

if __name__ == "__main__":
    # Ejemplo de uso:
    valor = 2.1
    unidad = "mm de mercurio"
    resultado = convertir_presion(valor, unidad)
    print(f"Presión en atmósferas: {resultado[0]}")
    print(f"Presión en mm de mercurio: {resultado[1]}")
    print(f"Presión en milibares: {resultado[2]}")