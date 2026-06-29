import streamlit as st

from src.utils.file_utils import save_uploaded_file
from src.services.knowledge_base_service import (
    KnowledgeBaseService,
)


def render_upload():

    st.subheader(
        "📄 Upload Documents"
    )

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"],
    )

    if uploaded_file:

        st.success(
            f"{uploaded_file.name} selected."
        )

        if st.button(
            "Build Knowledge Base"
        ):

            file_path = save_uploaded_file(
                uploaded_file
            )

            with st.spinner(
                "Building vector database..."
            ):

                KnowledgeBaseService.build(
                    str(file_path)
                )

            st.success(
                "Knowledge Base Created!"
            )