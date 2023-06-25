# EDIT THE FILE WITH YOUR SOLUTION
import copy
import re
import collections
from itertools import product


def get_sentence(file_contents):
    file_contents = re.split(r'[?!.]', file_contents)
    phrases = file_contents
    return phrases


def get_sir_name_from_sentence(param_sentence):
    result_name = []
    for row in param_sentence:
        row = row.replace(',', '')
        row = row.replace(':', '')
        row = row.replace('"', '')
        row = row.split()
        for names in range(len(row)):
            if row[names] == 'Sir':
                result_name.append(row[names + 1])
            if row[names] == 'Sirs':
                x = names
                while True:
                    x = x + 1
                    if row[x] != 'and':
                        result_name.append(row[x])
                    if row[x] == 'and':
                        result_name.append(row[x + 1])
                        break
    return result_name


def analyze_sentence(name_records, propositions, participants):
    # Type 1, at least one of.
    if 'least' in propositions and 'Knight' in propositions:

        for a in name_records:
            for b in participants:
                if a[0] == b and a[1] == 1:
                    return True
    if 'least' in propositions and 'Knave' in propositions:

        for a in name_records:
            for b in participants:
                if a[0] == b and a[1] == 0:
                    return True

    # Type 2, at most one of.
    if 'most' in propositions and 'Knight' in propositions:

        count = 0
        for a in name_records:
            for b in participants:
                if a[0] == b and a[1] == 1:
                    count += 1
        if count <= 1:
            return True
    if 'most' in propositions and 'Knave' in propositions:

        count = 0
        for a in name_records:
            for b in participants:
                if a[0] == b and a[1] == 0:
                    count += 1
        if count <= 1:
            return True

    # Type 3, exactly/Exactly.
    if 'exactly' in propositions or 'Exactly' in propositions:

        if 'Knight' in propositions:
            count = 0
            for a in name_records:
                for b in participants:
                    if a[0] == b and a[1] == 1:
                        count += 1
            if count == 1:
                return True
    if 'exactly' in propositions or 'Exactly' in propositions:

        if 'Knave' in propositions:
            count = 0
            for a in name_records:
                for b in participants:
                    if a[0] == b and a[1] == 0:
                        count += 1
            if count == 1:
                return True

    # Type 4, All/all.
    if 'All' in propositions or 'all' in propositions:

        if 'Knights' in propositions:
            count = 0
            for a in name_records:
                for b in participants:
                    if a[0] == b and a[1] == 1:
                        count += 1
            if count == nb_of_person:
                return True
    if 'All' in propositions or 'all' in propositions:

        if 'Knaves' in propositions:
            count = 0
            for a in name_records:
                for b in participants:
                    if a[0] == b and a[1] == 0:
                        count += 1
            if count == nb_of_person:
                return True

    # Type 5, I am.
    if propositions[0] == 'I' and propositions[1] == 'am':

        if 'Knight' in propositions:
            for a in name_records:
                for b in participants:
                    if a[0] == b and a[1] == 1:
                        return True
    if propositions[0] == 'I' and propositions[1] == 'am':

        if 'Knave' in propositions:
            for a in name_records:
                for b in participants:
                    if a[0] == b and a[1] == 0:
                        return True

    # Type 6, Sir XXX is a
    if propositions[0] == 'Sir' and propositions[2] == 'is':

        if 'Knight' in propositions:
            for a in name_records:
                for b in participants:
                    if a[0] == b and a[1] == 1:
                        return True
    if propositions[0] == 'Sir' and propositions[2] == 'is':

        if 'Knave' in propositions:
            for a in name_records:
                for b in participants:
                    if a[0] == b and a[1] == 0:
                        return True

    # Type 7, (Disjunction) Sir XXX or Sir XXX is a
    if 'or' in propositions and 'Knight' in propositions:

        count = 0
        for a in name_records:
            for b in participants:
                if a[0] == b and a[1] == 1:
                    count += 1
        if count >= 1:
            return True
    if 'or' in propositions and 'Knave' in propositions:

        count = 0
        for a in name_records:
            for b in participants:
                if a[0] == b and a[1] == 0:
                    count += 1
        if count >= 1:
            return True

    # Type 8, (Conjunction) Sir XXX and Sir XXX are
    if 'all' not in propositions and 'all' not in propositions and propositions[-2] == 'are':

        if 'Knights' in propositions:
            count = 0
            for a in name_records:
                for b in participants:
                    if a[0] == b and a[1] == 1:
                        count += 1
            if count == len(participants):
                return True
    if 'all' not in propositions and 'all' not in propositions and propositions[-2] == 'are':

        if 'Knaves' in propositions:
            count = 0
            for a in name_records:
                for b in participants:
                    if a[0] == b and a[1] == 0:
                        count += 1
            if count == len(participants):
                return True

    return False


def find_participant(said_sir, sentence_and_name, all_people):
    participator = []
    if 'us' in sentence_and_name:
        return all_people
    if 'I' in sentence_and_name:
        participator.append(said_sir)
    for s in range(len(sentence_and_name)):
        if sentence_and_name[s] == 'Sir':
            participator.append(sentence_and_name[s + 1])
    return participator


def all_situations(sirs):
    all_list = list(product((0, 1), repeat=len(sirs)))
    for a in all_list:
        all_possible = []
        b = 0
        for names in sirs:
            all_possible.append((names, a[b]))
            b += 1
        truth_table.append(all_possible)
    return truth_table


# file_name = "test_3.txt"
file_name = input('Which text file do you want to use for the puzzle? ')
with open(file_name) as open_file:
    file_content = open_file.read()
    file_content = file_content.replace('\n', ' ')
    all_text = copy.deepcopy(file_content)
    all_sirs = []
    sentence = get_sentence(file_content)
    # print(sentence)
    all_sirs.extend(get_sir_name_from_sentence(sentence))
    all_sirs = list(set(all_sirs))
    all_sirs = sorted(all_sirs)
    print('The Sirs are: ', end='')
    print(' '.join(symbol for symbol in all_sirs))

truth_table = []
nb_of_person = len(all_sirs)
case_table = all_situations(all_sirs)
# print(case_table)
clues = collections.defaultdict(list)
# print(all_text)

all_text = all_text.replace('."', '".')
all_text = all_text.replace('!"', '"!')
all_text = all_text.replace('?"', '"?')
# print(all_text)
all_text = get_sentence(all_text)
# print(all_text)
for line in all_text:
    # remove all marks and replace (")  with (quotation_mark)
    line = line.replace(',', '')
    line = line.replace(':', '')
    line = line.replace('"', ' quotation_mark ')
    # print(line)
    line = line.split()
    # print(line)

    temporary = ''
    statement = []
    claims = []
    for i in range(len(line) - 2):
        if line[i] == 'quotation_mark':
            first_quotation = i
            j = i
            while True:
                j += 1
                if line[j] != 'quotation_mark':
                    temporary += ' ' + line[j]
                if line[j] == 'quotation_mark' or j == len(line) - 1:
                    second_quotation = j
                    statement.append(temporary)
                    for claims in statement:
                        claims = claims.split()
                    for k in range(len(line)):
                        if k < first_quotation or k > second_quotation:
                            if line[k] == 'Sir':
                                clues[line[k + 1]].append(claims)
                    del line[first_quotation]
                    del line[second_quotation - 1]
                    break
# print(clues)
num_statements = 0
for key in clues.keys():
    num_statements += len(clues[key])

result = []
participant = []

for i in case_table:
    name_record = i
    # print(name_record)
    temp_Result = []
    for key in clues:
        for value in clues[key]:
            sentences = value
            # find all participants
            participant = find_participant(key, sentences, all_sirs)
            # print(participant)
            for j in name_record:
                # if one person is Knight and his/her statements is True, add this situation to the temp
                if j[0] == key and analyze_sentence(name_record, sentences, participant) == 1 and j[1] == 1:
                    temp_Result.append(name_record)
                # if one person is Knave and his/her statements is False, add this situation to the temp
                if j[0] == key and analyze_sentence(name_record, sentences, participant) == 0 and j[1] == 0:
                    temp_Result.append(name_record)

    if len(temp_Result) == num_statements:
        result.append(name_record)

# print the final result
# print(result)
if len(result) == 0:
    print('There is no solution.')
elif len(result) == 1:
    print('There is a unique solution:')
    for i in result:
        for j in i:
            if j[1] == 1:
                print(f'Sir {j[0]} is a Knight.')
            if j[1] == 0:
                print(f'Sir {j[0]} is a Knave.')
else:
    print(f'There are {len(result)} solutions.')
