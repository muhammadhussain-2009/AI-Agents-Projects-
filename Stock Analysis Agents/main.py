import sys
from crew import StockAnalysisCrew

def run():
    inputs = {
        'query': 'What is the company you want to analyze?',
        'company_stock': 'AMZN',
    }
    return StockAnalysisCrew().crew().kickoff(inputs=inputs)

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'query': 'What is last years revenue',
        'company_stock': 'AMZN',
    }

    if len(sys.argv) < 2:
        raise ValueError("Please provide the number of training iterations as a command line argument.")

    try:
        n_iterations = int(sys.argv[1])
        StockAnalysisCrew().crew().train(n_iterations=n_iterations, inputs=inputs, filename=__file__)
    except ValueError:
        raise ValueError("The training iterations argument must be an integer.")
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
    
if __name__ == "__main__":
    print("## Welcome to Stock Analysis Crew")
    print('-------------------------------')
    result = run()
    print("\n\n########################")
    print("## Here is the Report")
    print("########################\n")
    print(result)