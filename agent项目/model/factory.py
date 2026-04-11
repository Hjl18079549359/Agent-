from abc import abstractmethod,ABC
from typing import Optional
from Agent智能体.agent项目.utils.config_handler import rag_config
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.embeddings import Embeddings
from langchain_community.chat_models.tongyi import  BaseChatModel

class BaseModelFactory(ABC):
    @abstractmethod
    def generator(self)->Optional[Embeddings|BaseChatModel]:
        pass

class ChatModelFactory(BaseModelFactory):
    def generator(self)->Optional[Embeddings|BaseChatModel]:
        return ChatTongyi(model=rag_config["chat_model_name"])

class EmbeddingsFactory(BaseModelFactory):
    def generator(self)->Optional[Embeddings|BaseChatModel]:
        return DashScopeEmbeddings(model=rag_config["embedding_model_name"])

chat_model_factory = ChatModelFactory().generator()
embedding_model_factory = EmbeddingsFactory().generator()
