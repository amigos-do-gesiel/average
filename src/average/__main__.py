import argparse

def get_parser():
    """
    Creates a new argument parser.
    """
    parser = argparse.ArgumentParser('average')
    version = '%(prog)s ' + "0.0.1" #Pegar versão com __version__
    parser.add_argument('--version', '-v', action='version', version=version)
    return parser

def main(args=None):
    """
    Main entry point for project.

    Args:
        args : list
            A of arguments as if they were input in the command line. Leave it
            None to use sys.argv.
    """

    parser = get_parser()
    args = parser.parse_args(args)
    
    print("Welcome to Average Framework ;)")

if __name__ == '__main__':
    main()