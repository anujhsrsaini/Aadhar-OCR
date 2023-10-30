<p align="center">
  <a href="https://github.com/ShaanCoding/ReadME-Generator">
    <img src="Aadhaar.png" alt="Logo" height="80">
  </a>

  <h3 align="center">Aadhaar OCR using Tesseract</h3>

  <p align="center">
    
  </p>
</p>

## Table Of Contents

- [Table Of Contents](#table-of-contents)
- [About The Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Authors](#authors)

## About The Project

This project is a Python-based tool designed to extract and digitize text information from Aadhar Cards, the unique identification cards issued by the Government of India. This project aims to facilitate the automation of data extraction from Aadhar Cards, making it easier to integrate Aadhar Card data into various applications, databases, and systems.

Developers and data analysts often need to test and develop Redash features, plugins, and customizations in a local environment before deploying to a production server. While Linux is the recommended platform for hosting Redash, this project aims to make it more accessible to Windows users for local testing and development.

### Features

* Aadhar Card Text Extraction: The project includes OCR capabilities that can accurately extract text from Aadhar Cards, including important information such as the Aadhar number, holder's name, date of birth, and address. This OCR functionality is powered by Tesseract, an open-source OCR engine known for its accuracy and versatility in text recognition.

* Customization: Users have the flexibility to customize the OCR process to accommodate variations in Aadhar Card formats and designs.

* Open Source: This project is open source and can be freely used, modified, and extended by the community.

## Getting Started

### Prerequisites

1. Ensure you have Windows 10 or later with [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) installed and configured.
2. [Python 3.7.9](https://www.python.org/downloads/release/python-379/) Make sure you have Python 3.7.9 installed on your system. You can download and install Python from the official Python website.
3. [Git](https://git-scm.com/download/win)
4. [Tesseract OCR](https://github.com/tesseract-ocr/tessdoc/blob/main/Downloads.md): Tesseract is used for text extraction. Install Tesseract for your operating system by following the instructions on the Tesseract GitHub repository.

### Installation

1. Clone the repo

```sh
git clone https://github.com/anujhsrsaini/redash.git
```

*You can change the environment variables if you want but there isn't much need for it.*

2. Build and Run the docker container using the below command to run Redash it in detached mode.

```sh
docker-compose up -d
```

3. Run the below command to create a DB to store necessary information of Redash in PostgreSQL within the container.

```sh
docker-compose run — rm server create_db
```

4. Use the browser to navigate to localhost:5000 to setup redash initially.

5. Now, you can explore different functionalities of redash by setuping up different connections and building reports/dashboards.


## Authors

- **[Anuj Saini](https://www.linkedin.com/in/anuj-saini-7230a0257/)**