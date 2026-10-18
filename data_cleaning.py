students = [
    {'name': '  John Doe ', 'age': '17', 'score': '85'},
    {'name': 'mary jane', 'age': 16, 'score': '72'},
    {'name': 'Peter Brown', 'age': None, 'score': '91'},
    {'name': 'JOHN DOE', 'age': '17', 'score': '85'},
    {'name': '  Sarah Williams', 'age': '15', 'score': '105'},
    {'name': '', 'age': '16', 'score': '67'},
    {'name': 'David Lee ', 'age': 'sixteen', 'score': '74'},
    {'name': 'Mary Jane', 'age': 16, 'score': '72'},
]
def inspect_students(students):
    to_do_dict = {'total students': len(students), 'missing names': 0, 'missing ages': 0,
                  'missing score': 0, 'invalid scores': 0, 'name with spaces': 0
                  }
    for student in students:
        student['score'] = int(student['score'])
        if student['name'] == None or student['name'].strip() == '':
            to_do_dict['missing names'] += 1
        if student['age'] == None or student['age'] == '':
            to_do_dict['missing ages'] += 1
        if student['score'] < 0 or student['score'] > 100:
            to_do_dict['invalid scores'] += 1
        if (student['name'] is not None and student['name'] != student['name'].strip()):
            to_do_dict['name with spaces'] += 1
    return to_do_dict
inspection = inspect_students(students)
print(inspection)
# testing
scores = ['85', 'seventy', '105', None, '0']
for score in scores:
    try:
        if score is None:
            print('score is empty')
            continue
        else:
            score = int(score)
        if (0<=score <= 100):
            print('valid score')
        else:
            print('invalid score')
            continue
    except ValueError:
        print('score is not numeric')
        #testing data
        customers = [
            {'name': 'Amina', 'email': 'amina@example.com'},
            {'name': '', 'email': 'tunde@example.com'},
            {'name': 'Chidi', 'email': None},
            {'name': '   ', 'email': 'ada@example.com'},
            {'name': 'Tunde', 'email': '   '}
        ]
        # inspecting missing values
def inspect_missing_values(customers):
    missing_dict = {'total customers': len(customers), 'missing names': 0, 'missing emails': 0}
    for customer in customers:
        if customer['name'] is None or customer['name'].strip() == '':
            missing_dict['missing names'] += 1
        if customer['email'] is None or customer['email'].strip() == '':
            missing_dict['missing emails'] += 1
    return missing_dict

missing_info = inspect_missing_values(customers)
print(missing_info)

#inspect employee
def inspect_employee_data(employees):
    missing_info = {'total employees': len(employees), 'missing names': 0, 'missing departments': 0,
                    'invalid names': 0, 'invalid departments': 0}
    for employee in employees:
        if employee['name'] is None:
            missing_info['missing names'] += 1

        elif isinstance(employee['name'], str):
            if employee['name'].strip() == '':
                missing_info['missing names'] += 1
        else:
            missing_info['invalid names'] += 1
        if employee['department'] is None:
            missing_info['missing departments'] += 1
        elif isinstance(employee['department'], str):
            if employee['department'].strip() == '':
                missing_info['missing departments'] += 1
        else:
            missing_info['invalid departments'] += 1
    return missing_info
employees = [
    {'name': 'Kunle', 'department': 'Sales'},
    {'name': '   ', 'department': 'IT'},
    {'name': 'Ngozi', 'department': ''},
    {'name': None, 'department': 'Finance'},
    {'name': 'Bola', 'department': None},
    {'name': 'Tunde', 'department': '   '}
]
employee_info = inspect_employee_data(employees)
print(employee_info)

#using isinstance()
name = 123

if isinstance(name, str):
    if name.strip() == '':
        print('Name is missing')
    else:
        print('Name is not missing')
else:
    print('Name is not a string')
employees = [
    {'name': 'Kunle', 'department': 'Sales'},
    {'name': None, 'department': 'IT'},
    {'name': 123, 'department': 'Finance'},
    {'name': 'Bola', 'department': None}
]
missing_info = inspect_employee_data(employees)
print(missing_info)

# clean name
employees = [
    {'name': '  kunle adebayo ', 'department': 'sales'},
    {'name': 'AMINA JOHNSON', 'department': 'IT'},
    {'name': '  chidi okafor', 'department': 'finance'},
    {'name': 'BOLA ADE', 'department': 'sales'}
]

# clean name and department
def clean_name(employees):
    for employee in employees:
        if isinstance(employee['name'], str):
            employee['name'] = employee['name'].strip().title()
    return employees
clean_name = clean_name(employees)
print(clean_name)
employees = [
    {'name': 'Kunle', 'department': ' sales '},
    {'name': 'Amina', 'department': 'IT'},
    {'name': 'Chidi', 'department': 'FINANCE'},
    {'name': 'Bola', 'department': 'Sales'}
]
def clean_departments(employees):
    for employee in employees:
        if isinstance(employee['department'], str):
            employee['department'] = employee['department'].strip().upper()
    return employees
departments = clean_departments(employees)
print(departments)
def clean_employee_data(employees):
    for employee in employees:
        if isinstance(employee['name'], str):
            employee['name'] = employee['name'].strip().title()
        if isinstance(employee['department'], str):
            employee['department'] = employee['department'].strip().upper()
    return employees
employees = [
    {'name': '  kunle adebayo ', 'department': ' sales '},
    {'name': 'AMINA JOHNSON', 'department': 'IT'},
    {'name': None, 'department': ' FINANCE '},
    {'name': '  chidi okafor', 'department': None},
    {'name': 123, 'department': 'sales'}
]
clean_employee_info = clean_employee_data(employees)
print(clean_employee_info)

#count duplicates entries
def count_duplicate_employees(employees):
    count = 0
    employee_list = []
    for employee in employees:
        if isinstance(employee['name'], str):
            name = employee.get('name')
            department = employee.get('department')
            if (name, department) in employee_list:
                count += 1
            else:
                employee_list.append((name, department))
    return count
employees = [
    {'name': 'Kunle', 'department': 'SALES'},
    {'name': 'Amina', 'department': 'IT'},
    {'name': 'Kunle', 'department': 'SALES'},
    {'name': 'Chidi', 'department': 'FINANCE'},
    {'name': 'Amina', 'department': 'IT'}
]
duplicates = count_duplicate_employees(employees)
print(duplicates)
# remove duplicate employees
def remove_duplicate_employees(employees):
    seen_employees = []
    clean_employees = []
    for employee in employees:
        if isinstance(employee['name'], str):
            name = employee.get('name')
            department = employee.get('department')
            if (name, department) not in seen_employees:
                seen_employees.append((name, department))
                clean_employees.append(employee)
    return clean_employees
updated_employees = remove_duplicate_employees(employees)
print(updated_employees)
# valid age and score
employees = [
    {'name': 'Kunle', 'age': 25, 'score': 85},
    {'name': 'Amina', 'age': -5, 'score': 72},
    {'name': 'Chidi', 'age': 30, 'score': 150},
    {'name': 'Sarah', 'age': 0, 'score': 65},
    {'name': 'David', 'age': 40, 'score': -10},
    {'name': 'Tola', 'age': 60, 'score': 100},
    {'name': 'Bola', 'age': 17, 'score': 50}
]
# counting duplicates
def count_invalid_ages(employees):
    count = 0
    employee_list = []
    for employee in employees:
        if isinstance(employee['age'], int):
            age = employee.get('age')
            valid_age = (18 <= age <= 60)
            if not valid_age:
                count += 1
    return count
invalid_ages = count_invalid_ages(employees)
print(invalid_ages)
# invalid scores
def get_invalid_scores(employees):
    count = 0
    for employee in employees:
        if isinstance(employee['score'], int):
            score = employee.get('score')
            valid_score = (0 <= score <= 100)
            if not valid_score:
                count += 1
    return count
invalid_scores = get_invalid_scores(employees)
print(invalid_scores)
# valid score and age
def get_valid_age_score(employees):
    valid_employees = []
    for employee in employees:
        age = employee.get('age')
        score = employee.get('score')
        valid_age =  isinstance(employee['age'], int) and (18 <= age <= 60)
        valid_score = isinstance(employee['score'], int) and (0 <= score <= 100)
        if valid_age and valid_score:
            valid_employees.append(employee)
    return valid_employees
updated_list = get_valid_age_score(employees)
print(updated_list)
 # count invalid ages and scores
def get_invalid_age_score(employees):
    invalid_ages = 0
    invalid_scores = 0
    for employee in employees:
        if isinstance(employee['age'], int):
            age = employee.get('age')
            valid_age = (18 <= age <= 60)
            if not valid_age:
                invalid_ages += 1
        if isinstance(employee['score'], int):
            score = employee.get('score')
            valid_score = (0 <= score <= 100)
            if not valid_score:
                invalid_scores += 1
    return {'invalid ages': invalid_ages, 'invalid scores': invalid_scores}
invalid_age_score = get_invalid_age_score(employees)
print(invalid_age_score)
#counting the missing values
employees = [
    {'name': 'Kunle', 'age': 25, 'score': 85},
    {'name': 'Amina', 'age': None, 'score': 72},
    {'name': 'Chidi', 'age': 30, 'score': None},
    {'name': 'Sarah', 'age': 'twenty', 'score': 65},
    {'name': 'David', 'age': 40, 'score': 150},
    {'name': '', 'age': 22, 'score': 75},
    {'name': 'Tola', 'age': 17, 'score': 50},
    {'name': 'Bola', 'age': 35, 'score': 'eighty'}
]
def get_invalids(employees):
    invalid_names = 0
    invalid_ages = 0
    invalid_scores = 0
    for employee in employees:
        name = employee.get('name')
        if not isinstance(name, str) or name is None or name.strip() == '':
            invalid_names += 1
        age = employee.get('age')
        if not isinstance(age, int):
            if age is None:
                invalid_ages += 1
        score = employee.get('score')
        if not isinstance(score, int):
            if score is None:
                invalid_scores += 1
    return{'invalid names': invalid_names, 'invalid ages': invalid_ages, 'invalid scores': invalid_scores}
invalid_records = get_invalids(employees)
print(invalid_records)
employees = [
    {'name': '  kunle adebayo ', 'age': '25', 'score': '85'},
    {'name': 'AMINA JOHNSON', 'age': 'twenty', 'score': '72'},
    {'name': None, 'age': '30', 'score': '105'},
    {'name': 'Chidi Okafor', 'age': '22', 'score': None},
    {'name': 'Kunle Adebayo', 'age': '25', 'score': '85'},
    {'name': '  ', 'age': '-4', 'score': 'sixty'}
]
 # data cleaning project
def clean_employee_text(employees):
    cleaned_employees = []
    for employee in employees:
        cleaned_employee = employee.copy()
        if isinstance(employee['name'], str):
            name = employee.get('name')
            valid_name = name.strip().title()
            cleaned_employee['name'] = valid_name
        cleaned_employees.append(cleaned_employee)
    return cleaned_employees
valid_names = clean_employee_text(employees)
print(valid_names)

# cleaning age key
def get_number_age(employees):
    for number, employee in enumerate(employees, start=1):
        try:
            age_num = int(employee['age'])
            if (18 <= age_num <= 60):
                print(f"Record {number} {employee['name']}: Valid age")
            else:
                print(f"Record {number} {employee['name']}: Age out of range")
        except TypeError:
            print(f"Record {number} {employee['name']}: Age is missing or has unsupported format")

        except ValueError:
            print(f"Record {number} {employee['name']}: Invalid age")

get_number_age(employees)
# another cleaning
def clean_employee_data(employees):
    cleaned_employees = []
    issues = []
    for number, employee in enumerate(employees, start=1):
        cleaned_employee = employee.copy()
        if employee['name'] is None:
            issues.append(f"Record {number} {employee['name']}: Name is missing")

        elif isinstance(employee['name'], str):
            cleaned_name = employee['name'].strip().title()
            cleaned_employee['name'] = cleaned_name
            if cleaned_name == '':
                issues.append(f"Record {number}: {employee['name']} Name is missing")
        else:
            issues.append(f"Record {number}: {employee['name']} Name has unsupported format")

        try:
            if employee['age'] is None:
                issues.append(f"Record {number} {employee['name']}: Age is missing")
            else:
                age_num = int(employee['age'])
                if (18 <= age_num <= 60):
                    cleaned_employee['age'] = age_num
                else:
                    issues.append(f"Record {number} {employee['name']}: Age out of range")
        except TypeError:
            issues.append(f"Record {number} {employee['age']}: Age format not supported")
        except ValueError:
            issues.append(f"Record {number} {employee['name']}: Invalid age")
    #cleaning scores
        try:
            if employee['score'] is None:
                issues.append(f"Record {number}: {employee['score']}: score is missing")
            else:
                score_num = int(employee['score'])
                if (0 <= score_num <= 100):
                    cleaned_employee['score'] = score_num
                else:
                    issues.append(f"Record {number}: {employee['score']}: Score out of range")
        except TypeError:
            issues.append(f"Record {number}: {employee['score']}: Unsupported score format")
        except ValueError:
            issues.append(f"Record {number}: {employee['score']}: Invalid score")
        cleaned_employees.append(cleaned_employee)
    return cleaned_employees, issues
#test the function
cleaned_employees, issues = clean_employee_data(employees)

print("Cleaned employees:")
print(cleaned_employees)

print("\nValidation issues:")
for issue in issues:
    print(issue)
print('Total Records:')
print(len(cleaned_employees))
print('\nTotal Issues:')
print(len(issues))
print('\nRecords Without Issues')

issue = "Record 6: Age out of range"
parts = issue.split()
num = int(parts[1].replace(':', ''))
print(num)
records_with_issues = set()

for issue in issues:
    parts = issue.split()
    num = int(parts[1].replace(':', ''))
    records_with_issues.add(num)

total_records = len(cleaned_employees)
total_issues = len(issues)
total_records_with_issues = len(records_with_issues)
records_without_issues = total_records - total_records_with_issues


print('DATA QUALITY SUMMARY')
print('--------------------')
print(f"Total Records: {total_records}")
print(f"Total Records with issues: {total_records_with_issues}")
print(f"Records Without Issues: {records_without_issues}")

#set practice
customers = [
    'Kunle', 'Amina', 'Chidi', 'Kunle',
    'Amina', 'David', 'Kunle', 'David'
]
unique_customers = set()
for customer in customers:
    unique_customers.add(customer)
print(unique_customers)
print(f"Unique Customers: {len(unique_customers)}")
print(set(customers))
# finding repeated names
repeated_names = set()
seen = set()
for customer in customers:
    if customer in seen:
        repeated_names.add(customer)
    else:
        seen.add(customer)
print(repeated_names)
print(seen)
#counting duplicates
seen = set()
duplicate_count = 0
for employee in cleaned_employees:
    name = employee['name']
    age = employee['age']
    score = employee['score']
    record = (name, age, score)
    if record in seen:
        duplicate_count += 1
        print(f" Duplicate record: {record}")
    else:
        seen.add(record)
print(duplicate_count)

# set exercise involving dictionary
customers = {
    101: {'name': 'Kunle', 'email': 'kunle@gmail.com'},
    102: {'name': 'Amina', 'email': 'amina@gmail.com'},
    103: {'name': 'Chidi', 'email': 'kunle@gmail.com'},
    104: {'name': 'David', 'email': 'david@gmail.com'},
    105: {'name': 'Funke', 'email': 'amina@gmail.com'}
}
seen_emails = set()
duplicate_emails = set()
duplicate_count = 0
duplicate_name_count = 0
seen_names = set()
duplicate_names = set()
for customer_id, customer in customers.items():
    email = customer['email']
    name = customer['name']
    if email in seen_emails:
        duplicate_count += 1
        duplicate_emails.add(email)
    else:
        seen_emails.add(email)
    if name in seen_names:
        duplicate_name_count += 1
        duplicate_names.add(name)
    else:
        seen_names.add(name)
print(duplicate_count)
print(duplicate_emails)
print(duplicate_name_count)
print(duplicate_names)
# customer duplicate function
def detect_customer_duplicates(customers):
    seen_emails = set()
    duplicate_emails = set()
    duplicate_count = 0
    duplicate_name_count = 0
    seen_names = set()
    duplicate_names = set()
    for customer_id, customer in customers.items():
        email = customer['email']
        name = customer['name']
        if email in seen_emails:
            duplicate_count += 1
            duplicate_emails.add(email)
        else:
            seen_emails.add(email)
        if name in seen_names:
            duplicate_name_count += 1
            duplicate_names.add(name)
        else:
            seen_names.add(name)
    return duplicate_emails, duplicate_names
duplicate_emails, duplicate_names = detect_customer_duplicates(customers)
for email in duplicate_emails:
    print(email)
for name in duplicate_names:
    print(name)
def detect_duplicate_employee(cleaned_employees):
    seen_employees = set()
    duplicate_employees = set()
    duplicate_count = 0
    for employee in cleaned_employees:
        name = employee['name']
        age = employee['age']
        score = employee['score']
        record = (name, age, score)
        if record in seen_employees:
            duplicate_employees.add(record)
            duplicate_count += 1
        else:
            seen_employees.add(record)
    return duplicate_employees, duplicate_count
duplicate_employees, duplicate_count = detect_duplicate_employee(cleaned_employees)
for employee in duplicate_employees:
    print(employee)
print(duplicate_count)
 #remove duplicate employees
def remove_duplicate_employees(cleaned_employees):
    unique_employees = []
    seen_employees = set()
    for employee in cleaned_employees:
        name = employee['name']
        age = employee['age']
        score = employee['score']
        record = (name, age, score)
        if record not in seen_employees:
             unique_employees.append(employee)
             seen_employees.add(record)
    return unique_employees
unique_employees = remove_duplicate_employees(cleaned_employees)
print(unique_employees)
#reporting
print('DATA QUALITY REPORT')
print('-------------------')
print(f"Total Records: {len(cleaned_employees)}")
print(f"Unique Records: {len(unique_employees)}")
print(f"Duplicate Employees: {len(duplicate_employees)}")
#data report function
def generate_data_quality_report(cleaned_employees):
    seen_employees = set()
    duplicate_employees = set()
    duplicate_count = 0
    unique_employees = []
    for employee in cleaned_employees:
        name = employee['name']
        age = employee['age']
        score = employee['score']
        record = (name, age, score)
        if record in seen_employees:
            duplicate_employees.add(record)
            duplicate_count += 1
        else:
            unique_employees.append(employee)
            seen_employees.add(record)

    print('DATA QUALITY REPORT')
    print('-------------------')
    report = {'Total Records': len(cleaned_employees), 'Unique Records': len(unique_employees), 'Duplicate Employees': len(duplicate_employees)}
    return report

report = generate_data_quality_report(cleaned_employees)
print(report)
# converting data types
employees = {'name': 'Amina Johnson', 'age': 'twenty', 'score': 72}
{'name': None, 'age': 30, 'score': '105'}
{'name': '', 'age': '-4', 'score': 'sixty'}
def get_number_age(employees):
    issues = []
    cleaned_employees = []
    for number, employee in enumerate(employees, start=1):
        cleaned_employee = employee.copy()
        try:
            if employee['age'] is None or employee['age'] == '':
                issues.append('Age is missing')
            else:
                cleaned_employee['age'] = int(employee['age'])
                if (18 <= cleaned_employee['age'] <= 60):
                    cleaned_employees.append(cleaned_employee)

                else:
                    issues.append(f"Record {number} {employee['name']}: Invalid age")
        except TypeError:
            issues.append(f" Record {number} {employee['name']}: Unsupported age format")
        except ValueError:
            issues.append(f" Record {number} {employee['name']}: Invalid age")
    return cleaned_employees, issues
cleaned_employees, issues = get_number_age(cleaned_employees)
print(cleaned_employees)
print(issues)