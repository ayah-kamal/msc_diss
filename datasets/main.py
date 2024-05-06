# Merge json files of filered datasets for Active Learning task and initial 
# Machine learning training.
'''
import json


def merge_json_files(file_paths):
    merged_contents = []

    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file_in:
            merged_contents.extend(json.load(file_in))

    with open('dataset_merged_all.json', 'w', encoding='utf-8') as file_out:
        json.dump(merged_contents, file_out)


paths = [
    "all_data\project-4-all-data.json",
    "all_data\project-5-all-data.json", 
    "all_data\project-6-all-data.json",
    "all_data\project-7-all-data.json",
    "all_data\project-8-all-data.json", 
    "all_data\project-9-all-data.json",
    "all_data\project-10-all-data.json", 
    "all_data\project-11-all-data.json",
    "all_data\project-12-all-data.json", 
    "all_data\project-13-all-data.json",
]

merge_json_files(paths)
'''

# Clean up data for prompt fine tuning
import json

taxonomy_map = {
  'NA': 'NA',
  'Structured': 'Structured',
  'Shapeless': 'Shapeless'  
}

shapelessness_map = {
  'Long Subject': 'Long Subject',
  'Long Intro Phrase': 'Long Intro Phrase',
  'Interruptions': 'Interruptions',
  'Sprawling Ending': 'Sprawling Ending',
  'Coordination': 'Coordination'
}

with open('project-15-min.json') as f:
  data = json.load(f)

formatted_data = []
for item in data:
  text = item['text']
  
  taxonomy = item['taxonomy'][0]['taxonomy'][0][0]
  classification = taxonomy_map[taxonomy]
  
  if classification == 'Shapeless':
    # print(len(item['taxonomy'][0]['taxonomy']))
    shapelessness = []
    for i in range(1, len(item['taxonomy'][0]['taxonomy'])):
      tag = item['taxonomy'][0]['taxonomy'][i][1]
      shapelessness.append(shapelessness_map[tag])

    # shapelessness = item['taxonomy'][0]['taxonomy'][1][1]

    # classification += ': ' + shapelessness_map[shapelessness]
    classification += ': ' + ', '.join(shapelessness)

#   formatted_text = {"text": f"[Content]: {text}\n[Classification]: {classification}"}
    
#   formatted_data.append(formatted_text)

# with open('formatted_data_new.json', 'w') as f:
#   json.dump(formatted_data, f, indent=2)

  # formatted_data.append(formatted_text)

  # with open('instruction_data.jsonl', 'a') as f:
  #     json.dump(formatted_text, f, indent=2)
  formatted_text = {"instruction": "Classify the following sentence as one of the following labels: 'NA,' 'Structured,' or 'Shapeless'. If you classify it as 'Shapeless', give it a sub-label from the following issues: 'Long Subject', 'Long Intro Phrase', 'Interruptions', 'Sprawling Ending', 'Coordination'.","input": text,"output": classification}
  # formatted_data.append(formatted_text)
  with open('instruction_data.jsonl', 'a') as f:
      json.dump(formatted_text, f, indent=1)












