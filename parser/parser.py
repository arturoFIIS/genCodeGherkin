import re

def procesar_requisito(requisito, idioma="es"):
    if idioma == "es":
        pantalla_regex = r"Característica: (.+)"
        campo_texto_regex = r'campo\s*de\s*texto\s*"(.*?)"'
        dropdown_regex = r'lista\s*desplegable\s*"(.*?)"'
        checkbox_regex = r'casilla\s*de\s*verificación\s*"(.*?)"'
        radio_regex = r'botón\s*de\s*opción\s*"(.*?)"'
        fecha_regex = r'campo\s*de\s*fecha\s*"(.*?)"'
        hora_regex = r'campo\s*de\s*hora\s*"(.*?)"'
        button_regex = r'botón\s*"(.*?)"'
        slider_regex = r'slider\s*"(.*?)"'
        textarea_regex = r'área\s*de\s*texto\s*"(.*?)"'
        switch_regex = r'interruptor\s*"(.*?)"'

    # Validar que se encuentre una característica
    pantalla_match = re.search(pantalla_regex, requisito)
    if not pantalla_match:
        raise ValueError("No se encontró una característica válida en el requisito.")
    pantalla = pantalla_match.group(1)

    componentes = []

    # Diccionario de expresiones regulares para componentes
    componentes_regex = {
        'text': campo_texto_regex,
        'dropdown': dropdown_regex,
        'checkbox': checkbox_regex,
        'radio': radio_regex,
        'date': fecha_regex,
        'time': hora_regex,
        'button': button_regex,
        'slider': slider_regex,
        'textarea': textarea_regex,
        'switch': switch_regex
    }

    # Detectar componentes
    for tipo, regex in componentes_regex.items():
        matches = re.findall(regex, requisito)
        for match in matches:
            componente = {'tipo': tipo, 'nombre': match}
            if tipo == 'radio':
                # Agregar opciones predeterminadas para los botones de opción
                componente['opciones'] = ["opcion 1", "opcion 2", "otro"]
            componentes.append(componente)

    return {'pantalla': pantalla, 'componentes': componentes}

def validar_requisito(requisito):
    # Validar que el requisito contenga la palabra "Característica" o "Feature"
    if not re.search(r'Característica:|Feature:', requisito):
        raise ValueError(
            "El requisito debe contener la palabra 'Característica' o 'Feature'. "
            "Ejemplo: 'Característica: Pantalla de inicio'."
        )
    
    # Validar que haya al menos un componente
    if not re.search(r'campo de texto|text field|lista desplegable|dropdown list|casilla de verificación|checkbox|botón de opción|radio button|botón|button', requisito):
        raise ValueError(
            "El requisito no contiene componentes válidos. Por favor, verifica el formato. "
            "Ejemplo: 'campo de texto \"Nombre\"'."
        )
    return True