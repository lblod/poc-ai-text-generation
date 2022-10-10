from enum import Enum

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from aitextgen import aitextgen

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"], )


class ModelName(str, Enum):
    gpt2_retrain = "gpt2-retrain"
    dutch_gpt_medium = "dutch-gpt-medium"
    dutch_gpt_neo = "dutch-gpt-neo"


models = {model.split("/")[-1]: aitextgen(tokenizer_file=f"{model.value}/tokenizer.json", model_folder=model.value) for model in
          ModelName}


@app.get("/generate", response_model=list[str])
async def generate(prompt: str, model: ModelName = "dutch_gpt_neo", n: int = 5, max_length: int = 64,
                   temperature: float = 0.7, early_stopping: bool = True):
    """
    Function that takes in a starting prompt and attempts to complete the sentence.
    :param prompt: the sentence to base it on
    :param model: the model that is currently in use
    :param n: number of sentences to generate
    :param max_length: the maximum length for the generated text
    :param temperature: The degree of randomness while exploring separate paths in text generation
    :param early_stopping: toggle that indicates wheter or not to stop sentence after first end of sentence.
    :return: a list of n * [prompts + generated text]
    """
    result = models[model].generate(n=n, prompt=prompt, max_length=max_length, temperature=temperature,
                                    return_as_list=True, early_stopping=early_stopping)
    return result
