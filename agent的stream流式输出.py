from langchain.agents import create_agent
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool
from markdown_it.common.html_re import attribute


@tool(description="获取股票价格，传入股票名称，返回字符串信息")
def get_price(name:str)->str:
    return f"股票{name}的价格是20元"

@tool(description="获取股票信息，传入股票名称，返回字符串信息")
def get_info(name:str)->str:
    return f"股票{name}，是一家A股上市公司，专注与IT职业教育。"

agent = create_agent(
    model=ChatTongyi(model="qwen3-max"),
    tools=[get_price, get_info],
    system_prompt="你是一个智能助手，可以回答股票相关问题，记住请告知我思考过程，让我知道你为什么调用某个工具"
)

for chunk in agent.stream({
    "messages": [{"role":"user","content":"传智教育股价多少，并介绍一下"}]
 },stream_mode="values"):
    last_message=chunk['messages'][-1]
    if last_message.content:
        print(type(last_message).__name__,last_message.content)

    try:
        if last_message.tool_calls:
            print(f"工具调用：{[tc['name'] for tc in last_message.tool_calls]}")
    except AttributeError as e:
        pass