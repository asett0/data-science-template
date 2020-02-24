from explore import run_explore
from clean import run_clean
from model import run_model

# Add command line arguments that you can then use as an 
# argument to docker container
if __name__ == "__main__":

    run_explore()