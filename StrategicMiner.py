
from gooey import Gooey, GooeyParser
from StratLogic import StratMine

@Gooey(program_name="StratMiner - By: Najjad") #defining the GUI window
def get_data(): 

    parser = GooeyParser(description="V.1, Hit the start button to get started!")

    return parser.parse_args()

def main():
    args = get_data() #won't create a new window without this so :/
    StratMine() #running stratmine function when start button is pressed


if __name__ == "__main__": #running main function 
    main()
