def test_create_employee(employees_endpoint):
    employees_endpoint.create_employee({
        "name": "Jack",
        "organization": "IT",
        "role": "Junior"
    })


def test_create_new_employee(employees_endpoint):
    employees_endpoint.create_new_employee({
        "name": "Mary",
        "organization": "Accounting",
        "role": "Bank Analytic"
    })


def test_fetch_single_employee(employees_endpoint):
    employees_endpoint.fetch_single_employee('1')


def test_all_employees(employees_endpoint):
    employees_endpoint.fetch_all_employees()


def test_update_single_field(employees_endpoint):
    employees_endpoint.update_single_field('1', {'organization': 'Accounting'})


def test_update_entire_data(employees_endpoint):
    employees_endpoint.update_entire_data('2', {
        "name": "Ann",
        "organization": "Analytic",
        "role": "BA"
    })


def test_delete_employee(employees_endpoint):
    employees_endpoint.delete_employee('1')

