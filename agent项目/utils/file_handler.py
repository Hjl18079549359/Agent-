from langchain_community.document_loaders import TextLoader,PyPDFLoader
import os
from Agent智能体.agent项目.utils.logger_handler import logger
import hashlib
from langchain_core.documents import Document

# 获取文件的md5的十六进制字符串
def get_file_md5_hex(file_path: str):
    if not os.path.exists(file_path):
        logger.error(f"[md5计算]文件{file_path}不存在")
        return
    if not os.path.isfile(file_path):
        logger.error(f"[md5计算]路径{file_path}不是文件")
        return
    md5 = hashlib.md5()
    chunk_size = 4096
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(chunk_size):
                md5.update(chunk)
        md5_hex = md5.hexdigest()
        return md5_hex
    except Exception as e:
        logger.error(f"计算{file_path}md5失败 ，{str(e)}")
        return None

    #返回文件夹内的文件列表（允许的文件后缀）
def listdir_with_allowed_type(path:str ,allowed_types: tuple[str]):
    files = []
    if not os.path.isdir(path):
        logger.error(f"[listdir_with_allowed_type]{path}不是文件夹")
        return None
    for f in os.listdir(path):
        if f.endswith(allowed_types):
            files.append(os.path.join(path, f))

    return tuple(files)

def pdf_loader(file_path: str,password=None)->list[Document]:
    return PyPDFLoader(file_path,password).load()

def text_loader(file_path: str)->list[Document]:
    return TextLoader(file_path).load()