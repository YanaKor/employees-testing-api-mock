import requests


class Employees:

    def __init__(self, url: str, session: requests.Session, token):
        self.session = session
        self.url = url
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}

    def fetch_single_employee(self, employee_id):
        employee_url = f'{self.url}/{employee_id}'
        response = self.session.get(employee_url, headers=self.headers)

        assert response.status_code == 200, f'Actual status code: {response.status_code}'
        assert response.json() == {
            "employeeId": 1,
            "name": "Jack",
            "organization": "IT",
            "role": "Junior"
        }, f'Actual: {response.json()}'

    def fetch_all_employees(self):
        response = self.session.get(self.url, headers=self.headers)
        assert response.status_code == 200, f'Actual status code: {response.status_code}'
        assert response.json() == [{'employeeId': 1, 'name': 'Jack', 'organization': 'IT', 'role': 'Junior'},
                                   {'employeeId': 2, 'name': 'Mary', 'organization': 'Accounting', 'role':
                                       'Bank Analytic'}], f'Actual: {response.json()}'

    def create_employee(self, data):
        response = self.session.post(self.url, headers=self.headers, json=data)
        assert response.status_code == 200, f'Actual status code: {response.status_code}'
        assert response.json() == {
            'employeeId': 1,
            "name": "Jack",
            "organization": "IT",
            "role": "Junior"
        }

    def create_new_employee(self, data):
        response = self.session.post(self.url, headers=self.headers, json=data)
        assert response.status_code == 200, f'Actual status code: {response.status_code}'
        assert response.json() == {
            'employeeId': 2,
            "name": "Mary",
            "organization": "Accounting",
            "role": "Bank Analytic"
        }

    def update_single_field(self, employee_id, data):
        employee_url = f'{self.url}/{employee_id}'
        response = self.session.patch(employee_url, headers=self.headers, json=data)

        assert response.status_code == 200, f'Actual status code: {response.status_code}'
        assert response.json() == {'message': 'Employee updated'}

    def update_entire_data(self, employee_id, data):
        employee_url = f'{self.url}/{employee_id}'
        response = self.session.put(employee_url, headers=self.headers, json=data)

        assert response.status_code == 200, f'Actual status code: {response.status_code}'
        assert response.json() == {'message': 'Employee updated'}

    def delete_employee(self, employee_id):
        employee_url = f'{self.url}/{employee_id}'
        response = self.session.delete(employee_url, headers=self.headers)

        assert response.status_code == 200
        assert response.json() == {
            "message": "Employee deleted"
        }
