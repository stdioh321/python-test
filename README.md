# Flask Echo Server

This is a simple Flask application that echoes any received request. It accepts any HTTP method (e.g., GET, POST, PUT, DELETE, PATCH) and returns the request headers and body.

## Demo
https://python-echo.onrender.com
> Test it with curl
```sh
curl -X POST -H "Content-Type: application/json" -d '{"name": "Mario", "age": 30, "email": "mario.bros@test.com"}' https://python-echo.onrender.com
```
## Requirements

To run the application, you will need:

* Python 3
* `curl` (optional)


## Installation

To install the application and its dependencies, you can use `pip`:
```sh
pip install -r requirements.txt
```

## Usage

To run the server, simply run the following command in the terminal:
```sh
python app.py
```

This will start the Flask application on port 5050. You can then send requests to the server using tools like `curl` or a web browser.

### Example

To send a POST request with some JSON data to the root path, you can use:

```sh
curl -X POST -H "Content-Type: application/json" -d '{"name": "Alice", "age": 30}' http://localhost:5050/
```

This should return a JSON response with the request information, including the URL, headers, and decoded JSON body.

## License
This application is licensed under the MIT License. See the LICENSE file for details.


This version of the README is designed to work with the single-file Flask echo server code that I provided earlier. Feel free to modify it to fit your specific application.

## References
* https://render.com