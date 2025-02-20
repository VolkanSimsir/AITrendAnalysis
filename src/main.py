from crew import TrendAnalysis

def run():
    inputs = {
        "topic": "artificial intelligence"
    }
    ta = TrendAnalysis()
    ta.crew().kickoff(inputs = inputs)


if __name__ == "__main__":
    run()
