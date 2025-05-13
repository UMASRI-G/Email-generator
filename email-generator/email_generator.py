import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# Get API key from .env
api_key = os.getenv("OPENAI_API_KEY")

# Initialize LangChain OpenAI Model
llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=api_key)

# Define the prompt template for email generation
template = PromptTemplate(
    input_variables=["subject", "tone"],
    template="""
    Write an email with the subject "{subject}" in a {tone} tone. Be polite and professional, and include all necessary details.
    """
)

def generate_email(subject, tone):
    """Generate an email using LangChain and OpenAI."""
    chain = LLMChain(llm=llm, prompt=template)
    response = chain.invoke({"subject": subject, "tone": tone})
    return response['text']