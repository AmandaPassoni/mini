import re

def lex_html(html_code):
    tags = re.findall(r'<([a-zA-Z0-9]+)', html_code)  # Reconhece as tags HTML
    attributes = re.findall(r'([a-zA-Z0-9-]+)="([^"]+)"', html_code)  # Reconhece os atributos das tags
    inner_html = re.findall(r'>([^<]+)<', html_code)  # Reconhece o valor do inerHTML das tags

    return tags, attributes, inner_html

# Exemplo de código HTML
html_code = '<html> <head> <title> Compiladores </title> </head><body> <p style="color:red;background:blue;" id="abc"> Unipinhal </p> <br> </body></html>'

tags, attributes, inner_html = lex_html(html_code)

# Imprime as tags encontradas
print("Tags:")
for tag in tags:
    print(tag)

# Imprime os atributos de cada tag
print("\nAtributos:")
for attr in attributes:
    print("Atributo:", attr[0])
    print("Valor:", attr[1])

# Imprime o valor do inerHTML de cada tag
print("\ninnerHTML:")
for html in inner_html:
    print(html)