from langchain.chains.combine_documents.base import BaseCombineDocumentsChain
from langchain.chains.question_answering import load_qa_chain
from langchain_core.vectorstores.base import VectorStoreRetriever
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.domain.LLM.application.interfaces.llm_interfaces import LLMInterface

from dotenv import load_dotenv

load_dotenv()


class LLMHandler(LLMInterface):
    """
    The LLMHandler class is responsible for interacting with a Large Language Model (LLM).

    It acts as an interface for processing queries and performing actions related to
    the language model. This handler could interact with various models or AI
    services and simulate or execute queries based on the implementation.

    Attributes:
        None. The class currently doesn't store any state but serves as a handler
        for interaction with an LLM.
    """

    def __init__(self) -> None:
        """
        Initializes the LLM (Large Language Model) handler.

        This handler is responsible for interacting with the language model,
        processing queries, or performing other IA-related operations.
        """
        self.__embeddings_model = OpenAIEmbeddings()
        self.__llm_model = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            max_tokens=200,
        )

    def run(self, question: str, pdf_binary) -> tuple:
        pdf = self.__loader_pdf(pdf_binary)
        chunks = self.__text_spliter(pdf)
        self.__save_chrome(chunks)
        retrieve, chain = self.__load_db()
        answer, context = self.__ask(retrieve, chain, question)
        return answer, context

    def __loader_pdf(self, pdf: bytes) -> PyPDFLoader:
        loader_pdf = PyPDFLoader(pdf, extract_images=False).load()
        return loader_pdf

    def __text_spliter(self, loader_pdf: PyPDFLoader) -> list:
        text_spliter = RecursiveCharacterTextSplitter(
            chunk_size=4000,
            chunk_overlap=20,
            length_function=len,
            add_start_index=True,
        )

        chunks = text_spliter.split_documents(loader_pdf)
        return chunks

    def __save_chrome(self, chunks: list) -> None:
        db = Chroma.from_documents(
            chunks, embedding=self.__embeddings_model, persist_directory="text_index"
        )
        db.persist()

    def __load_db(self) -> tuple[VectorStoreRetriever, BaseCombineDocumentsChain]:
        vectordb = Chroma(
            persist_directory="text_index", embedding_function=self.__embeddings_model
        )

        # Load Retriever
        retriever = vectordb.as_retriever(search_kwargs={"k": 3})

        # Chain - Contrução da cadeira de prompt para chamada do LLM
        chain = load_qa_chain(self.__llm_model, chain_type="stuff")

        return retriever, chain

    def __ask(
        self,
        retriever: VectorStoreRetriever,
        chain: BaseCombineDocumentsChain,
        question,
    ) -> tuple:
        context = retriever.get_relevant_documents(question)
        answer = (
            chain(
                {"input_documents": context, "question": question},
                return_only_outputs=True,
            )
        )["output_text"]
        return answer, context
