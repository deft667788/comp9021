# Written by *** for COMP9021
#
# Uses the file cardio_train.csv downloaded from
# https://www.kaggle.com/sulianova/cardiovascular-disease-dataset
#
# Implements a function analyse(gender, age)
# where gender is one of 'F' (for female) or 'M' (for male),
# and where age is any integer for which we have data in the file
# (nothing needs to be done if that is not the case).
#
# We assume that all years have 365 days;
# in particular, someone who is 365 days old is 0 year old,
# and someone who is 366 days old is 1 year old.
#
# We ignore records for which at least one of these conditions holds:
# - height < 150 or height > 200
# - weight < 50 or weight > 150
# - ap_hi < 80 or ap_hi > 200
# - ap_lo < 70 or ap_lo > 140
#
# For each of both classes "cardio problem" and "no cardio problem"
# (as given by the cardio attribute), we create 5 bins/categories for
# height, weight, ap_hi, ap_lo, of equal width,
# that span between smallest value and largest value
# for the attribute in the category.
# For instance, suppose that gender is 'F' and age is 48.
# - Suppose that for the category "cardio problem",
#   the shortest woman aged 48 is 150cm tall, and
#   the tallest woman aged 48 is 200cm tall.
#   Then each of the 5 categories for the class "cardio problem"
#   and for the attribute "height" spans 10cm.
# - Suppose that for the class "no cardio problem",
#   the shortest woman aged 48 is 158cm tall, and
#   the tallest woman aged 48 is 193cm tall.
#   Then each of the 5 categories for the class "no cardio problem"
#   and for the attribute "height" spans 7cm.
# To avoid boundary issues, add 0.1 to the maximum value
# (so with the previous example, the maximum heights would be
# considered to be 200.1 and 193.1, respectively).
# This applies to each of the 4 attributes height, weight,
# ap_hi and ap_lo.
#
# For each attribute and for each of its possible values,
# we compute the ratio of
# - the frequency of people under consideration with a "cardio problem"
#   having that value for that attribute, with
# - the frequency of people under consideration with "no cardio problem"
#   having that value for that attribute.
# Continuing the previous example:
# - Suppose that that there are 100 woman aged 48
#   who have a "cardio problem" and 20 of those are at most 160cm tall.
# - Suppose that that there are 150 woman aged 48
#   who have "no cardio problem" and 50 of those are at most 165cm tall.
# Then the ratio for the value "category 1" of the attribute "height"
# is 0.2 / 0.3...3...
#
# We keep only ratios that are strictly greater than 1 and order them
# from largest to smallest.
# A ratio might be infinite (see second sample test).
# In case two ratios are exactly the same, their order is determined
# by the order of the corresponding attributes in the csv file
# (first is height, last is being active or not), and in case the
# attributes are the same, their order is determined by the rank of
# the category (first is 1, last is 5; for booleans, False comes
# before True).
#
# We format ratios with 2 digits after the decimal point.
# After a ratio, the output is one of:
# - Height in category [1-5] (1 lowest, 5 highest)
# - Weight in category [1-5] (1 lowest, 5 highest)
# - Systolic blood pressure in category [1-5] (1 lowest, 5 highest)
# - Diastolic blood pressure in category [1-5] (1 lowest, 5 highest)
# - Cholesterol in category [1-3] (1 lowest, 3 highest)
# - Glucose in category [1-3] (1 lowest, 3 highest)
# - Smoking/Not smoking
# - Drinking/Not drinking
# - Not being active/Being active
#
# You are NOT allowed to use pandas. If you do, then your submission
# will NOT be assessed and you will score 0 to the quiz.

import csv
from collections import defaultdict


def check_span_data(data_record, result, key, headline):
    no_cardio_problem_numbers = defaultdict(int)
    cardio_problem_numbers = defaultdict(int)
    cardio_problem = data_record[key + '1']
    no_cardio_problem = data_record[key + '0']
    #
    if no_cardio_problem:
        min_value, max_value = min(no_cardio_problem), max(no_cardio_problem) + 0.1
        span = (max_value - min_value) / 5
        for item in no_cardio_problem:
            no_cardio_problem_numbers[int((item - min_value) // span)] += 1
    #
    if cardio_problem:
        min_value, max_value = min(cardio_problem), max(cardio_problem) + 0.1
        span = (max_value - min_value) / 5
        for item in cardio_problem:
            cardio_problem_numbers[int((item - min_value) // span)] += 1

    keys = set(list(cardio_problem_numbers.keys()) + list(no_cardio_problem_numbers.keys()))

    for i in sorted(keys):
        if cardio_problem_numbers[i] == 0:
            ratio = 0
        elif no_cardio_problem_numbers[i] == 0:
            ratio = float('inf')
        else:
            cardio_ratio = cardio_problem_numbers[i] / len(cardio_problem)
            no_cardio = no_cardio_problem_numbers[i] / len(no_cardio_problem)
            ratio = cardio_ratio / no_cardio

        result.append((ratio, i, f"{headline} in category {i + 1} (1 lowest, 5 highest)"))


def check_another_data(data_record, result, key, title, plotting):
    no_cardio_problem_numbers = defaultdict(int)
    cardio_problem_numbers = defaultdict(int)
    cardio_problem = data_record[key + '1']
    no_cardio_problem = data_record[key + '0']
    for item in no_cardio_problem:
        no_cardio_problem_numbers[item] += 1
    for item in cardio_problem:
        cardio_problem_numbers[item] += 1
    keys = set(list(cardio_problem_numbers.keys()) + list(no_cardio_problem_numbers.keys()))
    for i in sorted(keys):
        if cardio_problem_numbers[i] == 0:
            ratio = 0
        elif no_cardio_problem_numbers[i] == 0:
            ratio = float('inf')
        else:
            cardio_ratio = cardio_problem_numbers[i] / len(cardio_problem)
            no_cardio = no_cardio_problem_numbers[i] / len(no_cardio_problem)
            ratio = cardio_ratio / no_cardio
        if plotting:
            result.append((ratio, i, plotting[i]))
        else:
            result.append((ratio, i, f"{title} in category {i} (1 lowest, 3 highest)"))


def analyse(gender, age):
    data_records = defaultdict(list)
    result = []
    with open('cardio_train.csv') as csvfile:
        record = csv.DictReader(csvfile, delimiter=';')
        for row in record:

            csv_gender = 'F' if row['gender'] == '1' else "M"
            if csv_gender != gender:
                continue

            csv_age = (int(row['age']) - 1) // 365
            if csv_age != age:
                continue

            csv_height = int(row['height'])
            if csv_height < 150 or csv_height > 200:
                continue

            csv_weight = float(row['weight'])
            if csv_weight < 50 or csv_weight > 150:
                continue

            csv_ap_hi = int(row['ap_hi'])
            if csv_ap_hi < 80 or csv_ap_hi > 200:
                continue

            csv_ap_lo = int(row['ap_lo'])
            if csv_ap_lo < 70 or csv_ap_lo > 140:
                continue

            data_records['height' + row['cardio']].append(csv_height)
            data_records['weight' + row['cardio']].append(csv_weight)
            data_records['ap_hi' + row['cardio']].append(csv_ap_hi)
            data_records['ap_lo' + row['cardio']].append(csv_ap_lo)
            data_records['cholesterol' + row['cardio']].append(int(row['cholesterol']))
            data_records['gluc' + row['cardio']].append(int(row['gluc']))
            data_records['smoke' + row['cardio']].append(int(row['smoke']))
            data_records['alco' + row['cardio']].append(int(row['alco']))
            data_records['active' + row['cardio']].append(int(row['active']))

        check_span_data(data_records, result, 'height', 'Height')
        check_span_data(data_records, result, 'weight', 'Weight')
        check_span_data(data_records, result, 'ap_hi', 'Systolic blood pressure')
        check_span_data(data_records, result, 'ap_lo', 'Diastolic blood pressure')
        check_another_data(data_records, result, 'cholesterol', 'Cholesterol', None)
        check_another_data(data_records, result, 'gluc', 'Glucose', None)
        check_another_data(data_records, result, 'smoke', '', {0: 'Smoking', 1: 'Not smoking'})
        check_another_data(data_records, result, 'alco', '', {0: 'Drinking', 1: 'Not Drinking'})
        check_another_data(data_records, result, 'active', '', {0: 'Not being active', 1: 'Being active'})

        if gender == 'F':
            print(f"The following might particularly contribute to cardio problems for females aged {age}:")
        else:
            print(f"The following might particularly contribute to cardio problems for males aged {age}:")

        result.sort(key=lambda x: x[0], reverse=True)
        for i, j, k in result:
            if i > 1:

                print(f"   {i:.2f}: {k}")


