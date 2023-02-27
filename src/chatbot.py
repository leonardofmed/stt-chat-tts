import openai
from dotenv import load_dotenv
import os

class ChatBot:
    '''Defines a chatbot that uses OpenAI's GPT models to generate responses to user input.'''
    def __init__(self, prompt="", model="text-davinci-002"):
        load_dotenv()

        openai.api_key = os.getenv("API_KEY") # Set the OpenAI API key
        self.model = model # Set the GPT model to use (default is davinci)
        self.prompt = prompt # Set the prompt that will be used for the chatbot's responses

    def get_response(self, input_str):
        # Use OpenAI's Completion API to generate a response to the user's input
        response = openai.Completion.create(
            engine=self.model, # Use the selected GPT model
            prompt=f"{self.prompt}{input_str}\n", # Add the user's input to the prompt
            temperature=0.7, # Controls the "creativity" of the response (0.0 is very conservative, 1.0 is very creative)
            max_tokens=600, # Maximum number of tokens (words or symbols) in the response
        )

        # Return the generated response text (removing any leading or trailing white space)
        return response.choices[0].text.strip()