
# Text Extract App

🔍 This is a simple web application that combines a Flask backend and a React frontend to provide endpoints for text extraction from images. The extracted text is processed using Tesseract OCR and stored in a PostgreSQL database.

## Overview

This application offers the following features:

1. **Text Extraction**: Upload an image to extract text using Tesseract OCR and store it in the database.

2. **Get Extracted Text**: Retrieve the extracted text from the database.

## Getting Started

To use this app, make sure you have the following tools and resources ready:

- [Python 3.10+](https://www.python.org/downloads/) 🐍
  - Required for development.
  
- [Postman](https://www.postman.com/downloads/) or preferred API testing platform 🚀
  - Useful for testing and interacting with endpoints.
  
- [Tesseract](https://github.com/tesseract-ocr/tesseract) 📄
  - Optical Character Recognition (OCR) engine for text extraction.
  
- [PostgreSQL](https://www.postgresql.org/download/) 🐘
  - Open-source relational database for storing extracted text.

## API Reference

Explore the available endpoints for interacting with the API:

### Extract Text

Extract text from an uploaded image through a POST request.

```http
POST /extract
```

Attach the image you want to extract as the request payload.

### Get Extracted Text

Retrieve extracted text using a GET request.

```http
GET /extract
```

## Usage

Follow these steps to run the Flask server and the React server:

1. **Run the Flask Server**:

   - Navigate to the directory containing your Flask application.
   - Open a terminal and run the following command:

     ```bash
     python app.py
     ```

   The Flask server will start and listen on `http://localhost:5000`.

2. **Run the React Server**:

   - Navigate to the directory containing your React frontend.
   - Open a terminal and run the following commands:

     ```bash
     npm install
     npm start
     ```

   The React server will start and open in your default web browser at `http://localhost:3000`. You can interact with the app and perform text extraction.