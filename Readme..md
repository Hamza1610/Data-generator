# Data Generator Web Server

---

Welcome to the Data Generator Web Server application! This server allows you to generate various types of synthetic data for testing, development, or any other purpose you may need. Below are the features and instructions to get started:

### Features:

1. **Customizable Data Generation:**
   - Generate data based on your specifications such as data type, format, quantity, and more.

2. **Multiple Data Types:**
   - Support for generating various data types including integers, floats, strings, dates, and custom patterns.

3. **Flexible API:**
   - Access the data generation functionality through a simple RESTful API.

4. **Easy-to-Use Web Interface:**
   - Interact with the data generation capabilities through a user-friendly web interface.

5. **Real-time Data Preview:**
   - Preview the generated data in real-time before exporting or using it.

### Getting Started:

1. **Installation:**
   - Clone this repository to your local machine.

2. **Dependencies:**
   - Ensure you have Python installed on your system.
   - Install the required Python packages by running:
     ```
     pip install -r requirements.txt
     ```

3. **Starting the Server:**
   - Run the following command to start the server:
     ```
     python app.py
     ```

4. **Accessing the Web Interface:**
   - Open your web browser and navigate to `http://localhost:5000`.
   - You will be greeted with the web interface to interact with the data generation functionalities.

5. **Using the API:**
   - You can also interact with the data generation features programmatically using the provided API endpoints.
   - Refer to the API documentation for details on available endpoints and their usage.

### API Documentation:

- **Endpoint:** `/generate`
  - **Method:** POST
  - **Parameters:**
    - `type` (string): Type of data to generate (e.g., 'integer', 'float', 'string', 'date').
    - `quantity` (integer): Number of data points to generate.
    - Additional parameters based on the data type (e.g., `min_value`, `max_value` for integers).

- **Example:**
  ```json
  {
    "type": "integer",
    "quantity": 10,
    "min_value": 0,
    "max_value": 100
  }
