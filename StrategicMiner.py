
from gooey import Gooey, GooeyParser
from StratLogic import StratMine

@Gooey(program_name="StratMiner - By: Najjad")
def get_data():

    parser = GooeyParser(description="V1")

    parser.add_argument( #needless but the library refuses to work without it :/
        "text",
        metavar="Type whatever you'd like in the below box to get your mining started!", #temporary statement because making buttons is rocket science
        help="To close, just close the window!",
        type=str,
        default="",
    )
    
    return parser.parse_args()

def main():
    args = get_data() #needless but the library refuses to work without it :/
    StratMine()


if __name__ == "__main__":
    main()
