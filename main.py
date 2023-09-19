import re

def extract_attributes(tag):
    pattern = r'(\w+)\s*=\s*["\'](.*?)["\']'
    attributes = re.findall(pattern, tag)
    return attributes

def parse_html(html):
    stack = []
    lines = html.split('\n')

    for line in lines:
        tags = re.findall(r'<\s*\/?\s*(\w+)', line)

        for tag in tags:
            if re.match(r'<\s*\/', line):  # Tag de fechamento
                if stack:
                    print('Tag de fechamento:', tag)
                    stack.pop()
            else:  # Tag de abertura
                print('Tag de abertura:', tag, ', Nível', len(stack))
                stack.append(tag)

                attributes = extract_attributes(line)
                for attr, value in attributes:
                    if attr == 'style':
                        styles = value.split(';')
                        for style in styles:
                            if style.strip() != '':
                                name, val = style.split(':')
                                print('Atributo de Tag:', attr)
                                print('Conteúdo 1 do style:', name.strip())
                                print('valor conteúdo 1:', val.strip())
                    else:
                        print('Atributo de Tag:', attr)
                        print('valor atributo', attr + ':', value)

        content = re.findall(r'>(.*?)<', line)
        for item in content:
            if item.strip() != '':
                print('conteúdo da tag:', item)

html_input = """<html> <head> <title> Compiladores </title> </head><body> <p style="color:red;background:blue;" id="abc"> Unipinhal </p> <br> </body></html>"""

parse_html(html_input)
