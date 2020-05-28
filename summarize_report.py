#!/usr/bin/env python
import csv
import sys


def main():
    csv_file = parse_args()
    questions = dict()

    with open(csv_file) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            num_cells = len(row)

            # first question is in column 4. zoom always adds an empty cell/additional comma.
            if num_cells <= 5:
                continue

            for i in range(4, num_cells - 1, 2):
                question = row[i]
                answer = row[i + 1]

                if question not in questions:
                    questions[question] = Question(question)
                questions[question].record_answer(answer)

    for question in questions.values():
        question.print()


def parse_args():
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: %s <zoom poll report csv file>\n" % (sys.argv[0]))
        sys.stderr.flush()
        sys.exit(1)
    return sys.argv[1]


class Question:
    def __init__(self, question):
        self.question = question
        self.answers = dict()

    def record_answer(self, answer):
        if answer not in self.answers:
            self.answers[answer] = 0
        self.answers[answer] += 1

    def print(self):
        print(self.question)
        for answer in sorted(list(self.answers.keys())):
            print("%s: %s" % (answer, self.answers[answer]))
        print()


if __name__ == '__main__':
    main()
