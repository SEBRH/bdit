from ollama import chat
import templates
import sys

import argparse

parser = argparse.ArgumentParser(description='Generar componente')
parser.add_argument('tipo', type=str, help='Tipo de componente')
parser.add_argument('--color', type=str, help='Color del componente')

args = parser.parse_args()

html = """ 

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SEXO</title>
</head>
<body>
    
</body>
</html>

 """.strip()

print(f"Generando {args.tipo} con color {args.color}")



# pasa el tipo a templates y el color



stream = chat(model='qwen2.5-coder:3b', messages=[
  {
    'role': 'user',
    'content': templates.templatePadre(args.tipo, args.color),
  },
], stream=True)

unfiltered = ""

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)
  unfiltered += chunk['message']['content']

def generate_markdown(final_code):
    md_content = final_code
    with open("output.md", "w", encoding="utf-8") as file:
        file.write(md_content)
    print(md_content)  # Enviar el contenido a VS Code

generate_markdown(unfiltered)