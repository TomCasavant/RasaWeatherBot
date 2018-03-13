from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weather_nlu')
agent = Agent.load('./models/dialogue', interpreter=nlu_interpreter)

input_channel = SlackInput('###OAUTH-TOKEN###', '###BOT-USER-TOKEN###', '###VERIFICATION-TOKEN###', True)
print (input_channel)
agent.handle_channel(HttpInputChannel(5002, '/', input_channel))
