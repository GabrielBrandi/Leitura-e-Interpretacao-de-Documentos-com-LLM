from leitores_documentos import carregar_documentos
from base_vetorial import criar_base_vetorial
from langchain_ollama import OllamaLLM

def main():
    caminhos = input("Digite os caminhos dos arquivos separados por vírgula (PDF, DOCX ou TXT): ").split(',')
    caminhos = [c.strip() for c in caminhos if c.strip()]
    try:
        documentos = carregar_documentos(caminhos)
    except Exception as e:
        print(f"Erro ao carregar arquivos: {e}")
        return

    base_vetorial = criar_base_vetorial(documentos)
    llm = OllamaLLM(model="llama3")

    print("Chat iniciado. Digite 'sair' para encerrar.\n")
    while True:
        pergunta = input("Pergunta: ")
        if pergunta.lower() == "sair":
            break
        resultados = base_vetorial.similarity_search(pergunta, k=10)
        contexto = "\n".join([
            f"[Arquivo: {doc.metadata.get('origem_arquivo', 'desconhecido')}]\n{doc.page_content}" for doc in resultados
        ])
        prompt = f"""
    Use o contexto(assuma que foi fornecido por um arquivo) abaixo para responder a pergunta.

    Contexto:
    {contexto}

    Pergunta:
    {pergunta}
    """
        resposta = llm.invoke(prompt)
        print("\nResposta:", resposta, "\n")

if __name__ == "__main__":
    main()