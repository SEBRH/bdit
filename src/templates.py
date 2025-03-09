
def templatePadre(tipo, color):

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

    if tipo == "template_sidebar":
        return template_sidebar(html, color)



def template_sidebar(code_smurf, color):
    return f"""
generate a sidebar in the following code: 

```

{code_smurf}

```

when styling do it with a scale of the color: {color}

Here is the Layout / Template on how to build a sidebar:

```
<div class="sidebar">
    <a href="#home">Home</a>
    <a href="#news">News</a>
    <a href="#contact">Contact</a>
    <a href="#about">About</a>
</div>

```

""".strip()