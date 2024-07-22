# Random Data Generator

This is a Django project that generates random numbers and provides them via both REST API and WebSocket connections.

## Features

- Generate random numbers and store them in the database
- Retrieve the latest generated number
- Retrieve all generated numbers
- WebSocket support for real-time updates
- User authentication with GitHub OAuth
- Scheduled tasks to generate random numbers periodically

## Requirements

- Python 3.8+
- Django 3.2+
- Daphne
- Node.js (for building frontend assets if needed)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/shirozuo/random_data.git
   cd random_data
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up the Django project:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser  # Follow the prompts to create a superuser
   ```
5. Configure GitHub OAuth:
   ```sh
   {
     "GITHUB_CLIENT_ID": "your-client-id",
     "GITHUB_CLIENT_SECRET_KEY": "your-client-secret"
   }
   ```
6. Run the development server:
   * Start the Daphne development server:
   ```sh
   daphne -b 0.0.0.0 -p 8000 random_data.asgi:application
   ```
   * In a new terminal, start the Daphne server:
   ```sh
   python manage.py runserver
   ```
   * In another terminal, start the scheduler for generating random numbers:
   ```sh
   python manage.py run_scheduler
   ```
   * Alternatively, you can use the provided batch files for convenience (QoL):
   ```sh
   ./start_all.bat
   ./stop_all.bat
   ```
## Usage
* Access the application at http://127.0.0.1:8000/
* Use the provided API endpoints to generate and retrieve random numbers
* WebSocket URL: ws://127.0.0.1:8000/ws/number/

## API Endpoints
* GET /generator/ - Index page (requires login)
* GET /generator/login/ - Login page
* GET /generator/logout/ - Logout
* GET /generator/generate/ - Generate a new random number
* GET /generator/latest/ - Get the latest generated number
* GET /generator/all/ - Get all generated numbers

## Running Tests
To run the tests for this project, use the following command:
   ```sh
      python manage.py test
   ```

## Batch Files
The project includes batch files to start and stop services:

* start_all.bat: Starts all necessary services for the project.
* stop_all.bat: Stops all running services related to the project.

These files can be executed in the command line to manage your services easily.

## Deployment
To deploy this project, you will need to configure a production server with the necessary dependencies. You can use services like Heroku, AWS, or DigitalOcean for deployment.

## Contributing
If you would like to contribute to this project, please open an issue or submit a pull request. Contributions are welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for details.
