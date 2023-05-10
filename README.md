# az-func-python-gpt
Chat API using Python 3.9.16, OpenAI API, Azure Function

**Use Case:**

Build an API that leverages openAI API (chatGPT API) and displays the response in JSON format. 

**Technology stack:** Python 3.9.16, Azure Function, openAI API

**openAI API:** We need an API key from openAI from here. https://platform.openai.com/account/api-keys

Azure Function:

Azure functions currently don't support the version above 3.10. You need to test it locally before deploying it to Azure.

Create an Azure HTTP trigger function in the local workspace and test it using Postman to make sure the Azure function is running without any issues. 

![image](https://github.com/aarkatta/az-func-python-gpt/assets/6164192/c5bbfd8f-0a20-484b-bd52-144855521933)

![image](https://github.com/aarkatta/az-func-python-gpt/assets/6164192/8696cb20-2b6b-4401-916f-fb20fcc290a3)

![image](https://github.com/aarkatta/az-func-python-gpt/assets/6164192/0db00340-4841-458e-9b0f-43e086a28d7a)

Login to https://portal.azure.com to get the function API URL.

![image](https://github.com/aarkatta/az-func-python-gpt/assets/6164192/833eff2b-db4d-47f3-aa8a-ef724a7e806a)


![image](https://github.com/aarkatta/az-func-python-gpt/assets/6164192/3c4235a9-6464-43dc-9226-191667af49a6)

![image](https://github.com/aarkatta/az-func-python-gpt/assets/6164192/484300e5-0cdb-4173-b6ba-d4adbe65fb19)


**Python: **

We need to add all the required modules to requirements.txt file. 

It also sets the OpenAI API secret key, which is stored in an environment variable named openai_secret_key.

The request body must have the following keys: model, prompt, max_tokens, temperature.

Model: This parameter specifies the name of the language model that OpenAI should use to generate the response. 
Prompt: The prompt is the initial text that the model uses to generate its response. Be specific and start with instruction. 
Max_tokens: This parameter controls the length of the response that the model generates, measured in the number of tokens.
Temperature: This parameter controls the creativity of the response.
Reference: https://platform.openai.com/docs/api-reference/completions/create

RequestBody:
 {
 
            "model": "text-davinci-003",
            
            "prompt": "Tell me a story about Yellow stone national park?",
            
            "max_tokens": 100,
            
            "temperature": 0.5
            
    }
    
Response Body:

"Once upon a time, there was a family who decided to take a trip to Yellowstone National Park. They had heard about the amazing wildlife and breathtaking scenery, and wanted to experience it all for themselves.

The family arrived in the park and were immediately overwhelmed by the beauty of the landscape. They spent days exploring the geysers and hot springs, watching the bison and elk roam the plains, and admiring the views from the top of the mountains."



