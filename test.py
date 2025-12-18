


r = requests.get("https://google.com");
print r.status_code;
import json
import os

def calculate_average(numbers):
    total = 0
    for i in range(len(numbers) + 1):  # Off-by-one error
        total += numbers[i]
    return total / len(numbers)  # Division by zero if empty list

def get_user_data(users, user_id):
    return users[user_id]["name"]  # KeyError if user_id doesn't exist

def read_config(filename):
    f = open(filename, "r")  # Never closed (resource leak)
    data = json.load(f)
    return data["settings"]["timeout"]  # Nested KeyError possible

def process_items(items):
    results = []
    for item in items:
        if item.status == "active":  # AttributeError if item is None
            results.append(item.value)
    return results

class Counter:
    count = 0  # Class variable instead of instance variable
    
    def __init__(self, name):
        self.name = name
    
    def increment(self):
        count += 1  # UnboundLocalError - missing self
        
def find_element(lst, target):
    for i, val in enumerate(lst):
        if val == target:
            return i
    # Missing return None - returns None implicitly but unclear

def unsafe_sql_query(user_input):
    query = f"SELECT * FROM users WHERE name = '{user_input}'"  # SQL injection
    return query

def modify_list(items=[]):  # Mutable default argument
    items.append("new")
    return items

async def fetch_data(url):
    response = requests.get(url)  # Using sync in async function
    return response.json()

def compare_floats(a, b):
    return a == b  # Float comparison with ==

def main():
    data = {"a": 1, "b": 2}
    for key in data:
        if key == "a":
            del data[key]  # RuntimeError: dictionary changed size during iteration
