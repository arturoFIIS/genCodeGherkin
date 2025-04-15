import os
import webbrowser
from jinja2 import Environment, FileSystemLoader

def generar_html_ui(datos):
    # Configurar Jinja2
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('base.html.j2')

    # Renderizar la plantilla con los datos
    html_content = template.render(
        pantalla=datos['pantalla'],
        componentes=datos['componentes'],
        # externalLinks=[
        #     '<link href="../static/css/tailwind-all.css" rel="stylesheet">'
        # ],
        externalScripts=[
            '<script src="https://example.com/script.js"></script>'
        ]
    )

    # Crear la carpeta de salida si no existe
    output_dir = 'salida'
    os.makedirs(output_dir, exist_ok=True)

    # Guardar el archivo HTML
    output_file = os.path.join(output_dir, f"{datos['pantalla'].replace(' ', '_').lower()}.html")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    # Abrir el archivo HTML en el navegador
    webbrowser.open(f"file://{os.path.abspath(output_file)}")