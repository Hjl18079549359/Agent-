"""
yaml
k: v
"""
import yaml
from Agent智能体.agent项目.utils.path_tool import get_abs_path

def load_rag_config(config_path:str=get_abs_path("config/rag.yml"),encoding: str="utf-8"):
    with open(config_path,"r",encoding=encoding) as f:
        rag_config = yaml.load(f, Loader=yaml.FullLoader)
        return rag_config

def load_agent_config(config_path:str=get_abs_path("config/agent.yml"),encoding: str="utf-8"):
    with open(config_path,"r",encoding=encoding) as f:
        agent_config = yaml.load(f, Loader=yaml.FullLoader)
        return agent_config

def load_prompts_config(config_path:str=get_abs_path("config/prompts.yml"),encoding: str="utf-8"):
    with open(config_path,"r",encoding=encoding) as f:
        prompts_config = yaml.load(f, Loader=yaml.FullLoader)
        return prompts_config

def load_chroma_config(config_path:str=get_abs_path("config/chroma.yml"),encoding: str="utf-8"):
    with open(config_path,"r",encoding=encoding) as f:
        chroma_config = yaml.load(f, Loader=yaml.FullLoader)
        return chroma_config

rag_config=load_rag_config()
agent_config=load_agent_config()
prompts_config=load_prompts_config()
chroma_config=load_chroma_config()

if __name__ == '__main__':
    print(rag_config["chat_model_name"])
