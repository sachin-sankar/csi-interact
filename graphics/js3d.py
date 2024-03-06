from json import load
from rich.pretty import pprint as print

with open('data.json','r') as file:
    data = load(file)

for hint in data:
    paths = []
    for model in data[hint]:
        for pathList in model['paths']:
            paths.extend(pathList)
    vertices = []
    for i in range(0,len(paths),3):
        vertices.append(paths[i:i+3])
    obj = 'o Cube\n'
    for vertex in vertices:
        obj += f'v {vertex[0]} {vertex[1]} {vertex[2]}\n'
    line = " ".join([str(i) for i in range(1,len(vertices)+1)])
    obj += f'l {line}'
    with open(f'{hint}.obj','w') as file:
        file.write(obj)