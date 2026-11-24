import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


# Load environment variables from .env
load_dotenv()


def create_chain():
    """
    Create a simple LangChain pipeline:

    input -> prompt -> model -> response
    """

    model = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        temperature=0,
    )

    prompt = ChatPromptTemplate.from_template(
        """
You are a helpful teacher.

Teach the following topic to a {level} learner.

Topic: {topic}

Return your answer using exactly these sections:

Definition:
Analogy:
Example:
Quiz Question:
"""
    )

    # LangChain composition:
    # output from prompt is passed into model
    chain = prompt | model

    return chain


def main():
    print("=" * 50)
    print("LangChain Learning Assistant")
    print("=" * 50)

    topic = input("Topic: ").strip()
    level = input("Level (beginner/intermediate/advanced): ").strip()

    if not topic:
        print("Please provide a topic.")
        return

    if not level:
        level = "beginner"

    chain = create_chain()

    try:
        response = chain.invoke(
            {
                "topic": topic,
                "level": level,
            }
        )

        print("\n" + "=" * 50)
        print("AI RESPONSE")
        print("=" * 50)

        print(response.content)

    except Exception as error:
        print("\nSomething went wrong:")
        print(error)


if __name__ == "__main__":
    main()