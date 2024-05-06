# Enhancing Clarity and Readability in Scientific Writing: An Automated Approach to Identifying Shapeless Sentences [^1]

This project aims to enhance the readability of scientific writing by automating the identification of "shapeless" sentences, which lack clarity and structure, using a fine-tuned large language model (LLaMA-2). The project utilizes various optimization techniques for efficient model training and includes a comprehensive dataset annotated based on readability principles from the book Style: Lessons in Clarity and Grace by Joseph Bizup and Joseph M. Williams [^2].

## Project Structure

- **Label Studio**: Annotation tool configurations and outputs.
- **Results**: Results and logs from experiments and model evaluations.
- **datasets**: Contains the early stages of the annotated Elsevier OA Corpus used for training and validation.
- **excel_sheets**: Excel files with detailed data analyses.
- **few_shot_demo.py**: A demonstration of few-shot learning capabilities on the final model. Contains the code for creating the few shot learning demonstrations for inference of the model
- **llama_7b_textcat.ipynb**: Jupyter notebook for text classification using LLaMA-2. Contains the main source code for the implementation of the llm finetuning and inference procedures 
- **main.py**: contains the code for creating the cleaned up alpaca format of the dataset obtained from Label Studio.
- **split_train_test_data.py**: contains the code for splitting the train and test data of the annotated dataset.

## Excel Sheets Description

- **loss_convergence.csv**: contain the data for the training and validation loss for the hyperparamter tuning configurations (batch size, epoch number, learning rate, lora_alpha, and lora_r)
- **confusion_mat.csv**: contains the data for the classfication accuracy of the fine tuned model
- **data_stat.csv**: contains the data distribution of the annotated Elsevier dataset across different domains and labels

## Dataset

- **elsevier_data_alpaca_format.json**: the main annotated dataset in alpaca format. This is the dataset used in the train_test split and for fine-tuning


[^1]: https://drepo.sdl.edu.sa/items/07aa9c4f-1661-4a65-9773-87452c53a57b
[^2]: Joseph M. Williams and Joseph Bizup. Style: Lessons in Clarity and Grace. Pearson, 12th edition, 2016.
