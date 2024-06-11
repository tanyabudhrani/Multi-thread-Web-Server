# Multi-thread-Web-Server

## Overview

This project is a multi-threaded web server implemented in Python, designed to handle concurrent connections efficiently. It leverages Python's socket and threading modules to manage and serve HTTP requests.

## Features

- **Concurrent Connections**: Utilizes multithreading to handle multiple client requests simultaneously.
- **HTTP Request Handling**: Parses HTTP requests, fetches requested files, and sends appropriate HTTP responses.
- **Customizable Configuration**: Allows customization of host IP, port number, and the directory from which files are served.
- **Error Handling**: Includes error handling for file not found scenarios.
- **Logging**: Logs client requests for monitoring and diagnostic purposes.

## Libraries Used

- **Socket Library**: Manages network connections.
- **Threading Library**: Enables concurrent handling of client requests.
- **OS Library**: Interacts with the file system.
- **Datetime Library**: Records timestamps for logging activities.

## How It Works

1. **handle_client Function**: Manages incoming client requests, parses HTTP requests, serves files, and constructs HTTP responses.
2. **log_request Function**: Logs client requests with details such as IP address, requested file, response status code, and timestamp.
3. **main Function**: Initializes the server, binds it to the specified host and port, and listens for incoming connections, spawning a new thread for each connection.

## Running the Server

To run the server, use the following command:

```sh
python3 server.py
