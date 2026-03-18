from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

def criar_base_vetorial(documentos, modelo="llama3", tamanho_chunk=400, sobreposicao_chunk=100):
    separador = RecursiveCharacterTextSplitter(
        chunk_size=tamanho_chunk,
        chunk_overlap=sobreposicao_chunk
    )
    chunks = separador.split_documents(documentos)
    embeddings = OllamaEmbeddings(model=modelo)
    base = Chroma.from_documents(chunks, embeddings)
    return base
