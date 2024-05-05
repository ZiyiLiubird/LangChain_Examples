from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models.moonshot import MoonshotChat

template = """
请扮演以为资深的技术博主，您将负责为用户生成适合在微博发布的中文文章。
请把用户输入的内容扩展成140个字左右的文章，并且添加适当的表情符号使内容引人入胜并体现专业性。
"""
prompt = ChatPromptTemplate.from_messages(
    [("system", template), ("human", "{input}")]
)

chat = MoonshotChat()
chain = prompt | chat | StrOutputParser()
response = chain.invoke(
    {"input": "给大家推荐一本新书《LangChain实战》，让我们一起开始学习LangChain吧！"}
)
print(response)