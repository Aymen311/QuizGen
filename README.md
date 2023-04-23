# QuizGen

QuizGen is a simple quiz generator that uses OpenAI's GPT-3 language model, fine-tuned on stack-exchange Q/As, to create unique questions and answers.

the complete pipeline for this project can be seen in this diagram

![Architecture-INFRA drawio](https://user-images.githubusercontent.com/59454072/233842471-93cf82f5-117a-4ca9-b974-9e7b0157d702.png)


## Getting Started

To get started with QuizGen, you can follow the steps below:

1. Clone the QuizGen repository using the following command:

```shell
git clone git@github.com:Aymen311/QuizGen.git
```` 
2. Install the required dependencies using the following commands:
```shell
cd QuizGen
pip install virtualenv
python3 -m venv
source /bin/activate
pip install -r requirements.txt
```
3. Create a profile on the OpenAI platform and generate an API key by following the following link 
here: https://platform.openai.com/account/api-keys

4. Export your API key as an environment variable using the following command:
```shell
export OPENAI_API_KEY="YOUR_KEY_HERE"
````
5. Run the QuizGen application using the following command
```shell
cd app
streamlit run Main.py
```

Enjoy using QuizGen! If you have any questions or feedback, feel free to create an issue on the repository or reach out to the project owner.
