"""
the anki converter
"""
import argparse

def md_to_anki_csv(file):
    pass



def main():
    parser = argparse.ArgumentParser()    
    parser.add_argument('-m', '--mode', help='converter mode')
    parser.add_argument('file', type=str)
    args = parser.parse_args()

    
    if args.mode == 'csv':
        # convert the md to csv falsh card
        file_path = args.file
        md_to_anki_csv(file_path)


if __name__ == '__main__':
    main()