from Similarity_Retrieval.Vector_Search import (
    vector_search
)

import pytest


def test_vector_search():

    """
    Test vector search
    returns top-k chunks.
    """

    try:

        # -------------------
        # Query
        # -------------------
        query = (
            "Who is the CEO "
            "of Bradsol company?"
        )

        top_k = 3

        results = (
            vector_search(
                query=query,
                top_k=top_k
            )
        )

        # -------------------
        # Validate response
        # -------------------
        assert (
            results is not None
        ), (
            "Vector search "
            "returned None."
        )

        assert (
            isinstance(
                results,
                list
            )
        ), (
            "Results should "
            "be a list."
        )

        assert (
            len(results) > 0
        ), (
            "Vector search "
            "returned no "
            "results."
        )

        # -------------------
        # Validate top-k
        # -------------------
        assert (
            len(results)
            <= top_k
        ), (
            f"Expected max "
            f"{top_k} chunks, "
            f"got "
            f"{len(results)}"
        )

        print(
            f"\nRetrieved "
            f"{len(results)} "
            f"chunks"
        )

        # -------------------
        # Print chunks
        # -------------------
        for i, chunk in enumerate(
            results
        ):

            print(
                f"\nChunk "
                f"{i+1}:"
            )

            print(chunk[:300])

    except Exception as e:

        pytest.fail(
            f"Vector search "
            f"test failed: {e}"
        )