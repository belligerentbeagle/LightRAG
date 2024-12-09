import os
import logging
import time
from lightrag import LightRAG, QueryParam
from lightrag.llm import ollama_model_complete, ollama_embedding
from lightrag.utils import EmbeddingFunc

# WORKING_DIR = "/Users/ethanyuxin/Documents/World/intelliExo/data/Lee Kuan Yew"
WORKING_DIR = "/Users/ethanyuxin/Downloads/"

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)

if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)

start_time = time.time()

rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=ollama_model_complete,
    llm_model_name="qwen2.5:latest",
    llm_model_max_async=4,
    llm_model_max_token_size=32768,
    llm_model_kwargs={"host": "http://localhost:11434", "options": {"num_ctx": 32768}},
    embedding_func=EmbeddingFunc(
        embedding_dim=768,
        max_token_size=8192,
        func=lambda texts: ollama_embedding(
            texts, embed_model="nomic-embed-text", host="http://localhost:11434"
        ),
    ),
)

# Add logging to check file content
try:
    # Try different encodings
    encodings = ['utf-8', 'latin-1', 'cp1252']
    content = None
    
    for encoding in encodings:
        try:
            with open('/Users/ethanyuxin/Downloads/atomichabits.txt', "r", encoding=encoding) as f:
                content = f.read()
                logging.info(f"Successfully read file using {encoding} encoding")
                break
        except UnicodeDecodeError:
            continue
    
    if content is None:
        logging.error("Could not read file with any of the attempted encodings")
    elif not content.strip():
        logging.error("File is empty")
    else:
        content = content.replace('|', '\n').replace('*', '\n•')
        logging.info(f"Read {len(content)} characters from file")
        rag.insert(content)
        logging.info("Content inserted successfully")

except FileNotFoundError:
    logging.error(f"File not found at specified path")
except Exception as e:
    logging.error(f"Error processing file: {str(e)}")

end_time = time.time()
logging.info(f"Total execution time: {end_time - start_time:.2f} seconds")

# # Perform naive search
# print(
#     rag.query("Who was Lee Kuan Yew referring to when he mentioned a 'her' turning 92?", param=QueryParam(mode="naive"))
# )

# # Perform local search
# print(
#     rag.query("Who was Lee Kuan Yew referring to when he mentioned a 'her' turning 92?", param=QueryParam(mode="local"))
# )

# # Perform global search
# print(
#     rag.query("Who was Lee Kuan Yew referring to when he mentioned a 'her' turning 92?", param=QueryParam(mode="global"))
# )

# # Perform hybrid search
# print(
#     rag.query("Who was Lee Kuan Yew referring to when he mentioned a 'her' turning 92?", param=QueryParam(mode="hybrid"))
# )
