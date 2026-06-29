from pathlib import Path


class FileDetector:
    """
    Detects uploaded file types.
    """

    @staticmethod
    def get_extension(
        file_path: str,
    ) -> str:

        return Path(file_path).suffix.lower()