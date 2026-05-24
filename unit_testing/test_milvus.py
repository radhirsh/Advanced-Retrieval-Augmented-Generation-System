import pytest

from Vector_Database.Milvus_Vector_DB import (
    vector_store
)


def test_milvus_connection():

    """
    Test Milvus
    connection.
    """

    try:

        assert (
            vector_store
            is not None
        ), (
            "Milvus client "
            "not initialized."
        )

        collections = (
            vector_store
            .list_collections()
        )

        assert (
            collections
            is not None
        ), (
            "Failed to fetch "
            "collections."
        )

        print(
            "\nMilvus "
            "connected "
            "successfully"
        )

        print(
            "Collections:",
            collections
        )

    except Exception as e:

        pytest.fail(
            f"Milvus "
            f"connection "
            f"failed: {e}"
        )