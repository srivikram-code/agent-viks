"""Step A: plain LangChain one-way chains.

Each chain is: prompt -> Gemini -> text parser.
These chains know nothing about LangGraph, so they can be reused anywhere.
"""

from pathlib import Path

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Load GOOGLE_API_KEY and LANGSMITH_* from learning/agents/.env
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

CATEGORIES = ["Learning", "Work", "Personal", "Health", "Finance"]
PRIORITIES = ["High", "Medium", "Low"]

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

# Chain 1: task -> category
classify_prompt = ChatPromptTemplate.from_template(
    "Classify the task into exactly one category from: {categories}.\n"
    "Reply with only the category word.\n\n"
    "Task: {task}"
)
classify_chain = (
    classify_prompt.partial(categories=", ".join(CATEGORIES))
    | llm
    | StrOutputParser()
)

# Chain 2: task + category -> priority
priority_prompt = ChatPromptTemplate.from_template(
    "Decide the priority of this task: {priorities}.\n"
    "Consider urgency (deadlines like 'today' or 'tomorrow') and importance.\n"
    "Reply with only the priority word.\n\n"
    "Task: {task}\n"
    "Category: {category}"
)
priority_chain = (
    priority_prompt.partial(priorities=", ".join(PRIORITIES))
    | llm
    | StrOutputParser()
)
