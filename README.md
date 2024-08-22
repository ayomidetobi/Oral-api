# Oral Disease AI Detection Django Application

This Django application leverages a custom-trained AI model to classify various oral diseases based on JPEG images of teeth. The model can identify conditions such as calculus, caries, gingivitis, hypodontia, tooth discoloration, and ulcers.

## Features

- **Image Upload**: Accepts JPEG images of teeth.
- **Disease Classification**: Classifies the image into one of the predefined oral disease categories.
- **REST API**: Provides a POST endpoint for image upload and classification.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/Oral-api.git
   cd Oral-api
   
## Set Up Virtual Environment

Create a virtual environment with the following command:

```bash
python -m venv venv
```

## Install Dependencies

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

## Download and Prepare the Model

Ensure that your model file `crossVIT_transformer_oral_disease_classifier.pth` is placed in the root directory of the project. This file contains your trained model weights.

1. **Download the Model File**

   Obtain the model file `crossVIT_transformer_oral_disease_classifier.pth` from your source.

2. **Place the Model File**

   Move the `crossVIT_transformer_oral_disease_classifier.pth` file to the root directory of your project. This is the directory where your `manage.py` file is located.

   For example:

   ```plaintext
   your-project-directory/
   ├── manage.py
   ├── crossVIT_transformer_oral_disease_classifier.pth
   ├── your_app/
   └── requirements.txt
## Apply Migrations

Apply database migrations using the following command:

```bash
python manage.py migrate
```

Start the Django development server with:
```bash
python manage.py runserver
```

## Usage

### API Endpoint

- **URL**: `/predict/`
- **Method**: `POST`
- **Content-Type**: `multipart/form-data`
- **Parameters**:
  - `image`: JPEG image file of the teeth condition.

This README provides a complete overview of the Django application, including setup instructions, usage, and how to interact with the API endpoint.
