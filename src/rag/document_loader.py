from langchain_community.document_loaders import PyMuPDFLoader


class DocumentLoader:
    """
    Loads PDF documents using PyMuPDF.
    """

    @staticmethod
    def load_document(file_path: str):

        loader = PyMuPDFLoader(file_path)

        return loader.load()