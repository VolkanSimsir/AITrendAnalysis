from crewai import Agent, Task, Process, Crew
from crewai.project import agent, output_json, task, crew , CrewBase
from tools.huggingface_tool import HuggingFaceModelListTool
from tools.arxiv_tool import ArxivTrendSearchTool


from pydantic import BaseModel, Field
from typing import Optional



class ArxivOutput(BaseModel):
    Title: Optional[str] = Field(..., description="Arxiv title")
    Link: Optional[str] = Field(..., description="Arxiv link")
    Authors: Optional[str] = Field(..., description="Arxiv authors")
    Date: Optional[str] = Field(..., description="Arxiv date")
    Summary: Optional[str] = Field(..., description="Arxiv summary")

class huggingfaceModel(BaseModel):
    model_name: str = Field(..., description="Model name")



@CrewBase
class TrendAnalysis:

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"


    @agent
    def huggingface_hub_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["huggingface_hub_agent"],
            tools=[HuggingFaceModelListTool()],
            
            
        )
   

    @agent
    def arxiv_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["arxiv_agent"],
            tools=[ArxivTrendSearchTool()],
            
        )


#------------------Task------------------------

    @task
    def huggingface_hub_task(self) -> Task:
        return Task(
            config=self.tasks_config["huggingface_hub_task"],
            agent=self.huggingface_hub_agent(),
            output_json=huggingfaceModel,
            
            
        )

    @task
    def arxiv_task(self) -> Task:
        return Task(
            config=self.tasks_config["arxiv_task"],
            agent=self.arxiv_agent(),
            output_json=ArxivOutput
            
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )