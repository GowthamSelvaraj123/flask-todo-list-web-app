 <h1>Flask Todo List Web App</h1>
 <img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/0198c54c-120d-44e4-b8ec-2aace1236947" />
 <img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/a91b5c17-59a0-44eb-85ef-fd267392d863" />
 <img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/5044f61c-0eee-49c4-947a-1c9535d0ea69" />
   <h2>Project Description</h2>
    <p>
        This project is a full-stack Todo List application built using <strong>Flask</strong>. 
        It includes <strong>user authentication</strong> (register, login, logout), and allows users to <strong>add, view, and delete tasks</strong>. 
        SQLite is used as the database with SQLAlchemy as the ORM.
    </p>
    <h2>Features</h2>
    <ul>
        <li>User registration and login/logout system.</li>
        <li>Add new tasks with a title and description.</li>
        <li>Delete tasks.</li>
        <li>Tasks are stored in a SQLite database.</li>
        <li>Simple and responsive HTML interface.</li>
    </ul>
    <h2>Project Structure</h2>
    <ul>
        <li><code>app/</code> - Contains Flask app code and Blueprints.</li>
        <li><code>app/templates/</code> - HTML templates for the app.</li>
        <li><code>app/static/</code> - CSS, JS, and static assets.</li>
        <li><code>run.py</code> - Entry point to run the Flask application.</li>
        <li><code>mydatabase.db</code> - SQLite database file.</li>
    </ul>
    <h2>Technologies Used</h2>
    <ul>
        <li>Python 3</li>
        <li>Flask</li>
        <li>Flask-Login</li>
        <li>Flask-SQLAlchemy</li>
        <li>SQLite</li>
        <li>HTML/CSS</li>
    </ul>
    <h2>Setup Instructions</h2>
    <ol>
        <li>Clone the repository: <code>git clone &lt;your-repo-url&gt;</code></li>
        <li>Create a virtual environment: <code>python -m venv venv</code></li>
        <li>Activate the environment: <code>source venv/bin/activate</code> (Linux/Mac) or <code>venv\Scripts\activate</code> (Windows)</li>
        <li>Install dependencies: <code>pip install -r requirements.txt</code></li>
        <li>Run the application: <code>python run.py</code></li>
        <li>Open <code>http://127.0.0.1:5000</code> in your browser.</li>
    </ol>
    <h2>Reflection</h2>
    <p>
        Building this project helped me understand Flask's routing, templates, and database integration with SQLAlchemy. 
        The hardest part was managing user authentication and database relationships. 
        Adding and deleting tasks dynamically was easy with Flask and SQLAlchemy. 
        Next time, I would improve by adding features like task categories, deadlines, and drag-and-drop for task management. 
        The biggest learning today was integrating Flask-Login with SQLAlchemy and creating a modular folder structure.
    </p>
    <h2>GitHub Repository</h2>
    <p>
        Check the project on GitHub: <a href="&lt;your-repo-url&gt;">Flask Todo List Web App</a>
    </p>
