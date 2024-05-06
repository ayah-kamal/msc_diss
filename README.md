# Excel Sheets

### Loss_convergence.csv: 
contain the data for the training and validation loss for the hyperparamter tuning configurations (batch size, epoch number, learning rate, lora_alpha, and lora_r)

### Confusion_mat.csv: 
contains the data for the classfication accuracy of the fine tuned model

### data_stat.csv
contains the data distribution of the annotated Elsevier dataset across different domains and labels


# Python Files:

### main.py:
contains the code for creating the cleaned up alpaca format of the dataset obtained from Label Studio.

### split_train_test_data.py
contains the code for splitting the train and test data of the annotated dataset.

### few_shot_demo.py
contains the code for creating the few shot learning demonstrations for inference of the model


# Dataset

### elsevier_data_alpaca_format.json
the main annotated dataset in alpaca format. This is the dataset used in the train_test split and for fine-tuning

# Jupyter Notebook

### llama_7b_textcat.ipynb
contains the main source code for the implementation of the llm finetuning and inference procedures 
