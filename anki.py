"""
the anki converter
first column: the name of the question
second column: the solution (analysis)
third column
"""
import argparse

def md_to_anki_csv(file):
    is_question = False
    is_ans = False
    question = ""
    ans = ""
    csv_line = ""
    with open(file) as in_file, open('out.csv', 'a') as out_file:
        for line in in_file:
            if line.startswith('# '):
                is_question = True
                continue

            if line.startswith('##'):
                is_question = False
                is_ans = False

                if '## Analysis' in line:
                    is_ans = True
                    continue

            if is_question:
                question += line
                is_question = False

            if is_ans:
                ans += line

        csv_line = "\"{}\" , \"{}\"\n".format(question, ans)
        out_file.write(csv_line)




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', help='converter mode')
    parser.add_argument('file', nargs='+', type=str)
    args = parser.parse_args()


    if args.mode == 'csv':
        # convert the md to csv falsh card
        for file_path in args.file:
            md_to_anki_csv(file_path)


if __name__ == '__main__':
    main()