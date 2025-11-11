from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load pretrained model and tokenizer
MODEL_NAME = "tscholak/cxmefzzi"  # small, text-to-SQL capable

print("Loading model... (this may take a few seconds)")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

def generate_sql(nl_query: str) -> str:
    """Convert natural language into SQL."""
    inputs = tokenizer(nl_query, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=100)
    sql = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return sql
