from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader

from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader

def carregar_documentos(caminhos):
    documentos = []
    for caminho in caminhos:
        if caminho.lower().endswith('.pdf'):
            loader = PyPDFLoader(caminho)
        elif caminho.lower().endswith('.docx'):
            loader = Docx2txtLoader(caminho)
        elif caminho.lower().endswith('.txt'):
            loader = TextLoader(caminho)
        else:
            raise ValueError('Formato de arquivo não suportado: ' + caminho)
        docs = loader.load()
        # Adiciona referência ao arquivo em cada documento
        for doc in docs:
            doc.metadata = doc.metadata or {}
            doc.metadata["origem_arquivo"] = caminho
        documentos.extend(docs)
    return documentos
