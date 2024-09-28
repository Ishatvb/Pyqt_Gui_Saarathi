import json
import os
import requests

class DataManager:
    def __init__(self, filename='data.json'):
        self.api_url = "https://pleasantly-winning-bluebird.ngrok-free.app/patients/search_patient"
        self.prescription_url = "https://pleasantly-winning-bluebird.ngrok-free.app/patients/assign_prescription"
        self.filename = filename
        self.patients = []
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):  # Check if the file already exists
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)  # Return the loaded data directly
            except (FileNotFoundError, json.JSONDecodeError):
                print("Error loading JSON data, initializing with default values.")
                return {
                    "medicines": [],
                    "tests": [],
                    "diet": []
                }
        else:
            return {
                "medicines": [],
                "tests": [],
                "diet": []
            }

    def update_medicines(self, medicines):
        self.data['medicines'] = medicines
        self.save_data()

    def update_tests(self, tests):
        self.data['tests'] = tests
        self.save_data()

    def update_diet(self, diet):
        self.data['diet'] = diet
        self.save_data()

    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=4)

    def get_medicines(self):
        return self.data['medicines']

    def get_tests(self):
        return self.data['tests']

    def get_diet(self):
        return self.data['diet']

    def get_patients(self, phone_no):
        try:
            response = requests.get(f"{self.api_url}?phone_no={phone_no}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            return []

    def assign_prescription(self):
        try:
            response = requests.post(self.prescription_url, json=self.data)
            response.raise_for_status()  # Raise an exception for HTTP errors
            print(f"Prescription assigned successfully: {response.json()}")
        except requests.RequestException as e:
            print(f"Error assigning prescription: {e}")
