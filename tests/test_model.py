
from dotenv import get_key
from data_generator.model import Model

api_key = get_key('.env', 'GOOGLE_API_KEY')

data_generator = Model(api_key)

data = data_generator.generate(
    {'cols': ['Instructions', 'Shell commands','funtions of commands', 'secure rate'], 'rows': 100},
    'Generate shell commands for diferent operating systems'
    )

f = open('demofile.csv', 'a')
f.write(data)