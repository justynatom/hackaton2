# names = input("podaj imie: ").title().split(",")
# tasks = input("podaj zadanie: ").split(",")
# grades = input("Podaj ocene: ").split(",")
#
# message = "Hi {},\n\nThis is a reminder that you have {} tasks left to \
# submit before you can graduate. You're current grade is {} and can increase \
# to {} if you submit all assignments before the due date.\n\n"
#
# for name, task, grade in zip(names, tasks, grades):
#     print(message.format(name, task, grade, int(grade)+1))




def read_file_csv(filename):
    with open(filename) as f:
        lines = f.readlines()
        print(lines)
        return lines

def separate_value_to_list(lines):
    imiona_nazwiska = []
    zadania = []
    ocena = []
    for line in lines:
        student_data = line.strip().split(",")
        print(student_data)
        imie_nazwisko = student_data[1] + " " + student_data[2]
        imiona_nazwiska.append(imie_nazwisko.title())
        zadania.append(student_data[3])
        ocena.append(student_data[4])
    print(imiona_nazwiska)
    print(zadania)
    print(ocena)
    return imiona_nazwiska, zadania, ocena

def return_possible_grade(sugested_grade):
    highest_grade = 6
    lowest_grade = 1
    if sugested_grade <= highest_grade and sugested_grade >= lowest_grade:
        return sugested_grade
    elif sugested_grade > highest_grade:
        return highest_grade
    else:
        return lowest_grade



def generate_message(message_template, names, tasks, grades, due_date):
    for name, task, grade in zip(names, tasks, grades):
        print(message_template.format(name, task, grade, return_possible_grade(int(grade)+1), due_date))

def get_due_date():
    date = "20.01.2023"
    return date


def get_message_template():
    message = "Hi {},\n\nThis is a reminder that you have {} tasks left to \n\
submit before you can graduate. You're current grade is {} and can increase \n\
to {} if you submit all assignments before the due date {}.\n\n"
    return message

def read_message_template(filename):
    try:
        with open(filename) as f:
            template = f.read()
            print(template)
    except FileNotFoundError:
        print("File ", filename, " is not found. Returning default message template.")
        return get_message_template()
    return template

def main():
    student_data_file = 'student.csv'
    message_template_file = 'messagej.txt'
    try:
        lines_file = read_file_csv(student_data_file)
        names, tasks, grades = separate_value_to_list(lines_file)
        generate_message(read_message_template(message_template_file), names, tasks, grades, get_due_date())
    except FileNotFoundError:
        print("File ", student_data_file, " is not found. Terminating program.")


if __name__ == '__main__':
    main()