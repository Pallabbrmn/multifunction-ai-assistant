from src.ingestion.file_detector import FileDetector
from src.ingestion.pdf_loader import PDFLoader
from src.ingestion.image_loader import ImageLoader


class LoaderFactory:

    @staticmethod
    def get_loader(
        file_path: str,
    ):

        extension = FileDetector.get_extension(
            file_path
        )

        if extension == ".pdf":
            return PDFLoader()

        if extension in [
            ".png",
            ".jpg",
            ".jpeg",
        ]:
            return ImageLoader()

        raise ValueError(
            f"Unsupported file type: {extension}"
        )