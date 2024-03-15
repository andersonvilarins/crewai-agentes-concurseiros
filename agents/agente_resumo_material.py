from crewai import Agent
import fitz #PyMuPDF
from transformers import pipeline

## Definindo a classe do Agente de Resumo de Material

class AgenteResumoMaterial:
    def __init__(self, arquivos_pdf):
        """
        Inicializa o agente com uma lista de caminhos para arquivos PDF.
        """
        self.arquivos_pdf = arquivos_pdf
        self.summarizer = pipeline("summarization")

    def extrair_texto_pdf(self, arquivo_pdf):
        """
        Extrai o texto de um arquivo PDF.
        """
        texto = ""
        with fitz.open(arquivo_pdf) as doc:
            for pagina in doc:
                texto += pagina.get_text()
        return texto

    def resumir_texto(self, texto):
        """
        Sumariza o texto extraído do PDF.
        """
        return self.summarizer(texto, max_length=130, min_length=30, do_sample=False)

    def processar_arquivos(self):
        """
        Processa cada arquivo PDF, extraindo e sumarizando seu conteúdo.
        """
        resumos = []
        for arquivo in self.arquivos_pdf:
            texto = self.extrair_texto_pdf(arquivo)
            resumo = self.resumir_texto(texto)
            resumos.append(resumo[0]['summary_text'])
        return resumos
            