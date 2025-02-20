from typing import List
from crewai.tools import BaseTool
from huggingface_hub import list_models


class HuggingFaceModelListTool(BaseTool):
    """HuggingFace Model List Tool"""
    
    name: str = "huggingface_model_list_tool"
    description: str = "Tool that lists the most current and popular models on huggingfacehub"

    def _run(self) -> str:
        recent_models = list_models(
        sort="trending_score",
        direction=-1,
        limit=10
        )
       
        result =  [model.id for model in recent_models]
        
        return result

