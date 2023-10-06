# Big Query Processor (BQP)

This project is an implementation of an Advanced Database Systems project that focuses on analyzing scholarly data from the DBLP dataset using a Neo4j graph database and a Python Flask-based frontend.

## Overview

In this project, we have implemented the following functionalities:

1. **Keyword Discovery (Q1)**: Allows users to enter a research topic and retrieves a list of authors working on that topic along with relevance and score. This functionality helps in identifying experts in a given research field.

2. **Researcher Profiling (Q2)**: Allows users to enter the name of a researcher and retrieves a list of topics they have worked on, along with keyword similarities and other researchers working on those topics. This functionality helps in profiling researchers and discovering related research fields.

3. **Influencing Author (Q3)**: Allows users to enter a research topic and retrieves a list of influential authors working on that topic using the PageRank algorithm. This functionality helps in identifying influential researchers in a specific research area.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- Flask
- Neo4j database (configured and running)

## Setup

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/jitendrajitu0563/Big-Query-Processor-.git

## Installation

1. Install Python dependencies:

```bash
  pip install Flask neo4j

```
2. Configure Neo4j:

Install Neo4j on your system and ensure it's running.
Update the Neo4j connection settings in the app.py file (uri, username, and password variables).
Download and import the DBLP dataset:

3. Download the DBLP dataset (version v10) in JSON format from https://www.aminer.org/citation.
Write a script to parse and import the data into your Neo4j database, creating nodes for authors and publications, and establishing CO_AUTHOR relationships. You may need to customize this script based on your dataset structure.
    
## Usage/Examples

1. Run the Flask application:

python app.py

2. Access the application in your web browser at http://localhost:5000.

3. Use the provided forms to perform the following tasks:

* Keyword Discovery (Q1)
* Researcher Profiling (Q2)
* Influencing Author (Q3)

  
## Functionalities

* Keyword Discovery

Users can enter a research topic, and the tool returns a list of authors working on that topic with relevance and score estimates.
* Researcher Profiling

Users can enter the name of a researcher, and the tool extracts all the topics on which the researcher has been working, along with a list of keyword similarities for each topic.
* Influencing Author

Users can enter a research topic, and the tool extracts a list of more influential authors working on that topic using the PageRank algorithm.

## Customization
Feel free to customize the project according to your specific requirements. You can update the HTML templates, enhance the frontend design, and modify the Cypher queries in the DB class to suit your dataset and research objectives.
## Acknowledgements

 The project uses the Neo4j graph database and the Flask web framework.


