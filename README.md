# Canvas-CLI
## Description
The Canvas CLI tool can return your favorited courses, course assignments, and the todo list from the Canvas site. This is great for returning important canvas information straight to the terminal.
An embedded GIF showing the tool running in a terminal. This is not optional; if your project does not include a GIF example, it will result in a substantial grade reduction. 


## Setup Instructions
1. Clone the repository 
```
git clone https://github.com/MartinMaybe/Canvas-CLI.git
cd canvas-cli
```

2. Install python dependencies 
The project requires two Python libraries, request and python-dotenv. Install both with:
```
python3 -m pip install requests python-dotenv
```

3. Create .env file
Open the file and add your Canvas API token and base URL:
```
CANVAS_API_TOKEN=your_token_here
BASE_URL=https://YOUR_SCHOOL.instructure.com/api/v1
```
Example for Boise State:
```
BASE_URL=https://boisestate.instructure.com/api/v1
```

4. Run the CLI tool
The tool is run from the terminal using:
```
./canvas <command>
```
Commands include:
- help        -  Show help message
- test        -  Test connection to Canvas
- courses     -  List favorite courses
- assignments -  List assignments for a course
- todo        -  List Todo items

### Example Usage:

Example 1: View favorite courses
```
./canvas courses    
Courses:
- Sp26 - CS 333 - Network Security and Defense (ID: 44254)
- Sp26 - CS 361 - Intro to Theory of Computation (ID: 46080)
- Sp26 - CS 408 - Full Stack Web Development (ID: 44253)
- Sp26 - ECE 330 - Microprocessors (ID: 46024)
- Sp26 - ECE 330L - Microprocessors Lab (ID: 46026)
```

Example 2: View your Canvas assignment for specific course 
```
./canvas assignments
Enter Course ID: 44253
Assignments for 44253:
- 05.02 - Initial Setup and Configuration  (Due: 2026-02-14T06:59:59Z)
- 8.02 - Mini-Lab Canavs Fun (Due: 2026-03-12T05:59:59Z)
- 06.01 - AWS Setup (Due: 2026-02-21T06:59:59Z)
```

## API Endpoints Used

## Canvas API Endpoints Used

| Endpoint | Description | Data Retrieved |
|----------|-------------|---------------|
| `/api/v1/users/self` | Retrieves information about the Canvas user. | User name and Canvas user ID |
| `/api/v1/users/self/favorites/courses` | Returns the list of the user’s favorited courses. | Course name and course ID |
| `/api/v1/courses/{course_id}` | Retrieves details about a specific course. | Course name |
| `/api/v1/courses/{course_id}/assignments` | Returns assignments for a specific course. | Assignment name and due date |
| `/api/v1/users/self/todo` | Retrieves the user’s upcoming tasks from the Canvas dashboard. | Assignment name, course name, and due date |

## Reflection
This project was a fun experience, especially becuase it was something I could actually find useful in my day to day. The project helped me learn how to interact with a real API and integrate it into my CLI tool. I also gained expereince in using the Python libarries to get HTTP requests, handle token authentication, and parse JSON responses. Then I just had to use argparse to take different commands. 

The biggest challenge was understanding the Canvas API. I would try to get objects or fields and would receive errors or empty attributes. I had to dig through some documentation or just look up how to get to access the fields I wanted. Once I learned how to get one field, it was a pretty easy process to get more implemented. If I had more time I would implement more of the grades, calendar, submission bot, and more. I would also make the output look more appealing and style it. 