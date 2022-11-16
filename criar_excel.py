import os
import requests
import json
import pandas as pd


documentos = ['81517468078', '64756598005', '41899190040', '22582334022', '52489892053', '11527478009']
dataset = [
      [d] for d in documentos
    ]

url = f'http://localhost:5000/get_1'
resp = requests.get(url)
response = resp.json()
# response = json.loads(resp.text)

representantes = json.loads(json.dumps(response['data']['aprovadores']))

for d in dataset:
    for a in representantes:
        # rep = json.loads(json.dumps(a))
        d.append('X' if d[0] in json.dumps(a['representnates']) else None)

df = pd.DataFrame(dataset)
print(df)

if not os.path.exists(os.path.join(os.path.abspath(os.curdir), 'excel')):
    os.mkdir(os.path.join(os.path.abspath(os.curdir), 'excel'))
base_dir = os.path.join(os.path.abspath(os.curdir), 'excel')

df.to_excel(f'{base_dir}'+ r'\Cenarios.xlsx', sheet_name='001', index=False)

# utilizar da forma abaixo para caso for incluir varias paginas dentro do excel,
# porem para isso precisa de todos os dataframes montados conforme no exemplo
# with pd.ExcelWriter(f'{base_dir}' + r'\Cenarios.xlsx', engine='xlsxwriter') as writer:
#     df.to_excel(writer, sheet_name='001', index=False)
#     df.to_excel(writer, sheet_name='002', index=False)
