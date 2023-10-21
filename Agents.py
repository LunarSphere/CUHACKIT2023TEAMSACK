'''
pip install wolframalpha
pip install pyowm
pip install opencv-python scikit-image
pip install langchain
'''

import os
from langchain.agents import AgentType
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.utilities.wolfram_alpha import WolframAlphaAPIWrapper
from langchain.llms import OpenAI
os.environ["OPENAI_API_KEY"] = "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"
os.environ["WOLFRAM_ALPHA_APPID"] = "X6TXQJ-KYXJ4V82JE"
os.environ["OPENWEATHERMAP_API_KEY"] = "ec19bf77a134b62f592e67be39a2b4d1"

class Agents:
    def wolf(self, instring):
        wolfram = WolframAlphaAPIWrapper()
        wolfram.run(instring)

    def weather(self, instring):
        llm = OpenAI(temperature=0)
        tools = load_tools(["openweathermap-api"], llm)

        agent_chain = initialize_agent(
        tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
        )
        agent_chain.run(instring)

    def dalle(self, instring):
        tools = load_tools(['dalle-image-generator'])
        agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
        output = agent.run(instring)
