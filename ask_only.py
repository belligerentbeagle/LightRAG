from lightrag import LightRAG, QueryParam
from lightrag.llm import gpt_4o_mini_complete


WORKING_DIR = "./knowledge"

rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=gpt_4o_mini_complete,  # Use gpt_4o_mini_complete LLM model
    # llm_model_func=gpt_4o_complete  # Optionally, use a stronger model
)

# Insert LKY Transcript into the graphml knowledge base
# with open(WORKING_DIR + '/LKYTranscript.txt', "r", encoding="utf-8") as f:
#     rag.insert(f.read())

# Perform local search
print(
    rag.query("Who is the 'she' referring to?", param=QueryParam(mode="local"))
)

# Perform hybrid search
print(
    rag.query("Who is the 'she' referring to?", param=QueryParam(mode="hybrid"))
)

# print(
#     rag.query("Who taught Lee Kuan Yew meditation?", param=QueryParam(mode="hybrid"))
# )