from shared import hello as shared_hello

def hello() -> str:
    print(shared_hello()) 
    return "Hello from agents!"
