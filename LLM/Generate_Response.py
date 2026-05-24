from libraries import *
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


# =====================================
# Azure OpenAI Model
# =====================================

Azure_Chat_model = AzureChatOpenAI(
    azure_endpoint=os.getenv(
        "AZURE_OPENAI_ENDPOINT"
    ),
    azure_deployment=os.getenv(
        "AZURE_OPENAI_DEPLOYMENT"
    ),
    api_key=os.getenv(
        "AZURE_OPENAI_KEY"
    ),
    api_version=os.getenv(
        "AZURE_OPENAI_API_VERSION"
    ),
    temperature=0.2
)


# =====================================
# Prompt Template
# =====================================

chat_prompt_template = (
    ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful assistant for answering questions based on the retrieved document chunks. Answer ONLY from the provided context."
            ),

            (
                "human",
                """
Question:
{query}

Retrieved Chunks:
{retrieved_chunks}

Answer:
"""
            )
        ]
    )
)


# =====================================
# Generate Response
# =====================================

def generate_response(
    query,
    retrieved_chunks
):

    try:

        # -------------------------
        # Context Building
        # -------------------------

        context = []

        for chunk in retrieved_chunks:

            # If LangChain Document
            if hasattr(
                chunk,
                "page_content"
            ):

                context.append(
                    chunk.page_content
                )

            # If dictionary
            elif isinstance(
                chunk,
                dict
            ):

                context.append(
                    chunk.get(
                        "page_content",
                        ""
                    )
                )

            # fallback
            else:

                context.append(
                    str(chunk)
                )

        final_context = (
            "\n\n".join(
                context
            )
        )

        # -------------------------
        # Prompt Formatting
        # -------------------------

        formatted_prompt = (
            chat_prompt_template.format_messages(
                query=query,
                retrieved_chunks=
                final_context
            )
        )

        # -------------------------
        # LLM Call
        # -------------------------

        response = (
            Azure_Chat_model.invoke(
                formatted_prompt
            )
        )

        return (
            response.content
        )

    except Exception as e:

        print(
            "Error in "
            "generate_response:",
            str(e)
        )

        return None