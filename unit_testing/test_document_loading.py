from Data_Ingestion.Document_Loader import (
    extension_detector,
    load_document
)


def test_pdf_extension():
    assert extension_detector(
        "sample.pdf"
    ) == "pdf"


def test_docx_extension():
    assert extension_detector(
        "sample.docx"
    ) == "docx"


def test_txt_extension():
    assert extension_detector(
        "sample.txt"
    ) == "txt"


def test_csv_extension():
    assert extension_detector(
        "sample.csv"
    ) == "csv"


def test_xlsx_extension():
    assert extension_detector(
        "sample.xlsx"
    ) == "xlsx"


def test_access_card_doc_load():

    docs = load_document(
        r"C:\Users\BRADSOL\Downloads\Sridhar_Files_Outsource\End_to_End_Rag\Policy_Documents\Access Card Policy.docx"
    )

    assert len(docs) > 0


def test_business_doc_load():

    docs = load_document(
        r"C:\Users\BRADSOL\Downloads\Sridhar_Files_Outsource\End_to_End_Rag\Policy_Documents\Business Continuity Policy - Bradsol.docx"
    )

    assert len(docs) > 0