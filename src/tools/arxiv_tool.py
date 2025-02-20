import arxiv
from crewai.tools import BaseTool
from pydantic import Field


class ArxivTrendSearchTool(BaseTool):
    """
    A specialized tool to find the most trending AI research papers from ArXiv.
    Focuses on recent, high-impact papers in artificial intelligence, machine learning, 
    and related domains.

    Args:
        query (str): Query text.
        max_results (int): Maximum number of articles to be withdrawn (Default 5).
     Returns:
        str: Returns the query result as text.

    """
    name: str = "ArxivTrendSearch"
    description: str = "Searches for the latest developments in artificial intelligence on archive. Returns results based on the query."
    max_results: int = Field(default=5, description="Maximum number of articles to be withdrawn")
    
    def _run(self, query: str) -> str:
        try:
            search = arxiv.Search(
                query=query,
                max_results=self.max_results,
                sort_by=arxiv.SortCriterion.SubmittedDate
            )
            output = ""
            for result in search.results():
                output += f"Title : {result.title}\nSummary: {result.summary}\nLink: {result.entry_id}\nAuthor: {result.authors}\nDate: {result.published}\n\n"
            return output if output else "No results found."
        except Exception as e:
            return f"An error occurred while querying the archive: {str(e)}"

