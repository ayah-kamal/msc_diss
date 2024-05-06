import json

def format_test_dataset(sample):
    instruction = f"""###Instruction:\\n{sample['instruction']}\\n\\n"""
    context = f"""###Input:\\n{sample['input']}\\n\\n""" if len(sample["input"]) > 0 else None
    response = f"""###Response:\\n {sample['output']}"""
    # join all the parts together
    prompt = "".join([i for i in [instruction, context, response] if i is not None])
    return prompt

# Load JSON data from a file
with open("few_shot_demo.json", "r") as json_file:
    data = json.load(json_file)

formatted_prompts = [format_test_dataset(sample) for sample in data]

# Join all the prompts and save as a single string
all_prompts = "\\n\\n".join(formatted_prompts)

# Save the string to a text file
with open("few_shot_demo_formatted.txt", "w") as txt_file:
    txt_file.write(all_prompts)