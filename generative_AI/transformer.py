from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Dialogue
dialogue = """
Alice: Hey, did you finish the project?
Bob: Not yet, I'm still working on it.
Alice: Do you need any help?
Bob: That would be great, thanks!
Alice: No problem. Let me know if you get stuck anywhere.
"""

# Load model + tokenizer
model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# ---- Encoding ----
tokens = tokenizer(dialogue, return_tensors="pt")
print("TOKENS IDs:\n", tokens["input_ids"][0])

# ---- Decoding ----
decoded = tokenizer.decode(tokens["input_ids"][0], skip_special_tokens=True)
print("\nDECODED TEXT:\n", decoded)

# ---- Model Generation ----
prompt = "Summarize this conversation:\n" + dialogue

inputs = tokenizer(prompt, return_tensors="pt")
generated_ids = model.generate(inputs["input_ids"], max_new_tokens=50)

summary = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
print("\nMODEL SUMMARY:\n", summary)


#zero_shot
examples = [
    {
        "dialogue": "Hi, how are you?\nI'm good, thanks!",
        "summary": "Two friends are greeting each other."
    },
    {
        "dialogue": "What time is it?\nIt's 5 PM.",
        "summary": "Someone asks for the time."
    }
]

prompt0 = f'''
dialouge:
{dialogue}

what was going on?
'''
input2 = tokenizer(prompt0,return_tensors="pt")

gen = model.generate(input2["input_ids"],max_new_tokens=50)

output2 = tokenizer.decode(gen[0],skip_special_tokens = True)
print(output2)

#few _shot
for ex in examples:
    prompt_few_shot += f"Dialogue:\n{ex['dialogue']}\nWhat was going on?\n{ex['summary']}\n\n"

prompt_few_shot += f"Dialogue:\n{dialogue}\nWhat was going on?\n"

input3 = tokenizer(prompt_few_shot,return_tensors="pt")

gen1 = model.generate(input3["input_ids"],max_new_tokens=50)

output3= tokenizer.decode(gen1[0],skip_special_tokens = True)
print(output3)
