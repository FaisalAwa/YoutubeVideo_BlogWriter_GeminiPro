from dotenv import load_dotenv
load_dotenv()
import os
from tools import yt_tool
from crewai import Agent

load_dotenv()

os.environ["OPEN_API_KEY"] = os.getenv("OPEN_API_KEY")
os.environ["OPEN_MODEL_NAME"] = 'gpt-4-0125-preview'

# Placeholder for llm, adjust accordingly
llm = None

# Create a Senior Blog Content Researcher
blog_researcher = Agent(
    role='Blog Researcher From Youtube Videos',
    goal='get the relevant video content for the topic {topic} from Yt Channel',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in Understanding videos in AI Data Science, Machine Learning and GEN AI and providing suggestions"
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True
)

# Creating a senior blog writer agent with YT tool
blog_writer = Agent(
    role="Blog Writer",
    goal='Narrate Compelling Tech Stories about the video {topic} from YT Channel',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=False
)
