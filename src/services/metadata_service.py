import json
import hashlib

from pathlib import Path
from datetime import datetime

METADATA_PATH = Path(
    "storage/metadata/indexed_files.json"
)


class MetadataService:

    @staticmethod
    def _ensure_file():

        METADATA_PATH.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if not METADATA_PATH.exists():

            METADATA_PATH.write_text("{}")

    @staticmethod
    def load():

        MetadataService._ensure_file()

        with open(
            METADATA_PATH,
            "r",
            encoding="utf-8",
        ) as f:

            return json.load(f)

    @staticmethod
    def save(data):

        MetadataService._ensure_file()

        with open(
            METADATA_PATH,
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
            )

    @staticmethod
    def calculate_hash(file_path):

        sha = hashlib.sha256()

        with open(
            file_path,
            "rb",
        ) as f:

            while True:

                chunk = f.read(8192)

                if not chunk:
                    break

                sha.update(chunk)

        return sha.hexdigest()

    @staticmethod
    def already_indexed(file_path):

        metadata = MetadataService.load()

        file_hash = MetadataService.calculate_hash(
            file_path
        )

        return any(
            item["hash"] == file_hash
            for item in metadata.values()
        )

    @staticmethod
    def add_file(file_path):

        metadata = MetadataService.load()

        metadata[
            Path(file_path).name
        ] = {

            "hash":
            MetadataService.calculate_hash(
                file_path
            ),

            "indexed_at":
            datetime.now().isoformat()

        }

        MetadataService.save(metadata)