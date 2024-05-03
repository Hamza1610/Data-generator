from dotenv import load_dotenv
import google.generativeai as genai
import json
import os

# load model configuration from json
with open('data_generator\model_config.json') as f:
    json_data = f.read()

model_config = json.loads(json_data)

class Model:
    """_summary_ : init gemini mode of communication
    Args:
        mode (str): types of Gemini mode:
            gen (str): for generative text only
            chat (str): for chat session
        text (str): Gemini generated text
        google_api_key (str): google api key 

    Returns:
        text (str): mardown formatted text 
    """
    # Set up the model
    # gemini satefy responce setting

    def __init__(self, key):
       self.key = key
       #configure gemini library
       genai.configure(api_key= self.key)

    def generate(self, data_structure, data_desciption):
        """_summary_

        Args:
            data_structure (_type_): _description_
            data_desciption (_type_): _description_

        Returns:
            _type_: _description_
        """
        self.data_structure, self.data_desciption = data_structure, data_desciption
        # Initialize Generative GEMINI Model with its safety settings
        model = genai.GenerativeModel('gemini-pro', generation_config=model_config["generation_config"], safety_settings=model_config["safety_settings"])
        response = model.generate_content(f'Gnenerate correct data in csv format of [{data_desciption}, with features of {data_structure}]. make sure the data are corrects and structured!. Note these data will be used for training models')
        # generated data
        return response.parts
        try:
            # # Initialize Generative GEMINI Model with its safety settings
            # model = genai.GenerativeModel('gemini-pro', generation_config=model_config.generation_config, safety_settings=model_config.safety_settings)
            # response = model.generate_content()
            # # generated data
            # return response.text
            print('Hello')
        except:
            print('Error occured while generating data!')

    def validate(self, data):
        """_summary_

        Args:
            data (_type_): data to be validated

        Returns:
            _type_: _description_
        """
        self.data = data
        try:
            # Initialize Generative GEMINI Model
            model = genai.GenerativeModel('gemini-pro', generation_config=model_config.generation_config, safety_settings=model_config.safety_settings)
            response = model.generate_content()
            # validated data
            return response.parts
        except:
            print('Error occured while validating data!')
