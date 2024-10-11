# Todo List App

This is a simple web-based **Todo List App** that allows users to manage their tasks efficiently. It includes user authentication, the ability to add, update, delete, and view tasks, and a clean, responsive UI.

## Features

- **User Authentication**: Users can log in and out. User's profile picture is dynamically generated using the RoboHash API.
- **Task Management**: Users can create, update, view, and delete tasks.
- **Responsive Design**: The layout is responsive and works well on both mobile and desktop devices.
- **Dynamic Table**: Tasks are listed in a table with alternating row colors for better readability.
- **Interactive UI**: Includes hover effects and transitions for buttons and links to enhance the user experience.
- **CSS Styling**: The CSS styling was generated using AI tools, allowing for a visually appealing design while focusing primarily on backend development.

## Technologies Used

- **HTML5**
- **CSS3** (styled using AI)
- **Django** (for the backend and templating)
- **RoboHash API** (for dynamically generated user profile pictures)

## Setup

To get the project running locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repo-name
    ```

3. Install dependencies:

    - Ensure you have Python and Django installed.
    - Install required packages:

    ```bash
    pip install django
    ```

4. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

5. Open your browser and go to `http://127.0.0.1:8000/` to view the app.

## How to Use

1. **Login**: Authenticate yourself if you're an existing user.
2. **Add Tasks**: Click on the "+ Add Task" button to add a new task.
3. **Manage Tasks**: You can view, edit, or delete tasks from the list.
4. **Logout**: Click the "Logout" button to securely sign out.

## Screenshots

### Task List View
![Task List View](screenshots/task_list_view.png)

### Add Task
![Add Task](screenshots/add_task.png)

### Responsive Design
![Login Page](screenshots/login.png)

## Future Improvements

- Add filtering and sorting of tasks.
- Implement a task deadline feature.
- Add categories and priorities for better task management.

## License

This project is licensed under the MIT License. Feel free to modify and use it as per your needs!

---

**Note**: Make sure to replace the repository URL and your GitHub username accordingly in the README file.
