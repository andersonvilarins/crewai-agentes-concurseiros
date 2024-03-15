from agente_resumo_material import AgenteResumoMaterial

# Substitua os caminhos abaixo pelos caminhos reais dos seus arquivos PDF
caminhos_pdf = ['D:\\DOWNLOADS\\engenharia-de-software-aula-01', 'D:\\DOWNLOADS\\engenharia-de-software-aula-02']

agente = AgenteResumoMaterial(arquivos_pdf=caminhos_pdf)
resumos = agente.processar_arquivos()

for resumo in resumos:
    print("Resumo:", resumo)
    print("-------")