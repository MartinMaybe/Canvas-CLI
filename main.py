import warnings 
warnings.filterwarnings("ignore")

import os
import requests
import argparse
from dotenv import load_dotenv

import warnings 
warnings.filterwarnings("ignore")

# Load environment variables from .env file
load_dotenv()

TOKEN = os.getenv("CANVAS_API_TOKEN")
BASE_URL = os.getenv("BASE_URL")

# Bearer token for authentication
headers = {
    "Authorization": f"Bearer {TOKEN}"
}

def test_connection():
    url = f"{BASE_URL}/users/self"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user = response.json()
        print("Connection successful!")
        print(f"Name: {user['name']}")
        print (f"ID: {user['id']}")
    else:
        print(f"Connection failed with status code: {response.status_code}")
        print(response.text)

def get_courses():
    url = f"{BASE_URL}/users/self/favorites/courses"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        courses = response.json()
        print ("Courses:")
        for course in courses:
            name = course.get("name")
            course_id = course.get("id")
            print(f"- {name} (ID: {course_id})")

def get_assignments(course_id):
    url = f"{BASE_URL}/courses/{course_id}/assignments"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        assignments = response.json()
        print (f"Assignments for {course_id}:")
        for assignment in assignments:
            assignment_name = assignment.get("name")
            due = assignment.get("due_at")
            print(f"- {assignment_name} (Due: {due})")

def get_todo():
    url = f"{BASE_URL}/users/self/todo"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        todo_items = response.json()
        print("ToDo Items:")
        for item in todo_items:
            assignment = item.get("assignment", {})
            name = assignment.get("name")
            course = item.get("context_name")
            print(f"{course} - {name}")


def main():
    parser = argparse.ArgumentParser(description="Canvas CLI Tool")

    # Command argument 
    parser.add_argument("command", help="Command to run")

    args = parser.parse_args()

    if args.command == "test":
        test_connection()
    elif args.command == "courses":
        get_courses()
    elif args.command == "assignments":
        course_id = input("Enter Course ID: ")
        get_assignments(course_id)
    elif args.command == "todo":
        get_todo()
    else:        
        print(f"Unknown command: {args.command}")


if __name__ == "__main__":
    main()