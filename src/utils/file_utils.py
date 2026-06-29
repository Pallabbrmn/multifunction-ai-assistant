from pathlib import Path


UPLOAD_DIR = Path("uploads")

UPLOAD_DIR.mkdir(
    exist_ok=True
)


def save_uploaded_file(
    uploaded_file,
) -> Path:

    file_path = UPLOAD_DIR / uploaded_file.name

    with open(
        file_path,
        "wb",
    ) as file:

        file.write(
            uploaded_file.getbuffer()
        )

    return file_path