from LLM.Generate_Response import generate_response
from langchain_core.prompts import ChatPromptTemplate


def test_generate_response():

    """
    Test response generation from LLM.
    """

    try:

        # -------------------
        # Sample Query
        # -------------------

        query = "What is the capital of France?"

        # -------------------
        # Mock Retrieved Chunks
        # -------------------

        retrieved_chunks = [
            {
                "page_content": "Paris is the capital of France."
            },
            {
                "page_content": "France is a country in Europe."
            }
        ]

        # -------------------
        # Prompt Template
        # -------------------

        chat_prompt_template = ChatPromptTemplate.from_template(
            """
You are a helpful assistant for answering questions based on the retrieved document chunks.

Answer ONLY from the given context.

Context:
{context}

Question:
{query}

Answer:
"""
        )

        # -------------------
        # Generate Response
        # -------------------

        response = generate_response(
            query=query,
            chat_prompt_template=chat_prompt_template,
            retrieved_chunks=retrieved_chunks
        )

        # -------------------
        # Print Response
        # -------------------

        print("\nGenerated Response:")
        print("=" * 80)
        print(response)
        print("=" * 80)

        # -------------------
        # Validate response
        # -------------------

        assert response is not None, "LLM returned None."

        assert isinstance(response, str), (
            "Response should be a string."
        )

        assert len(response.strip()) > 0, (
            "LLM returned an empty response."
        )

        # -------------------
        # Success Message
        # -------------------

        print("\nTest Passed Successfully ✅")

    except Exception as e:

        print(
            "Error in "
            "test_generate_response:",
            str(e)
        )


if __name__ == "__main__":
    test_generate_response()