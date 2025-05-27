<a id="readme-top"></a>
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<h3 align="center">Customer Product Review analyzer</h3>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This Project estimates star ratings for products using sentiment analysis on fake user reviews. It pulls product data from the FakeStoreAPI, generates simulated customer feedback, analyzes sentiment using natural language processing (NLP), and visualizes the results. 
## Features
-  Fetches product data via API
-  Generates 3-5 fake reviews on each product based on keywords or category
-  Uses VADER to analyze sentiment
-  Converts sentiment scores to a 1-5 star rating
-  Visualizes product ratings using a bar chart
-  Outputs a sorted CSV file with all product star ratings
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

– Python: Core Programming language

– pandas: Data manipulation and analysis

– NLTK: Natural Language Toolkit for VADER sentiment scoring

– matplotlib: Data visualization

– seaborn: Enhanced data visualization 

– requests: REST API consumption

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

Make sure you have Python 3.8 or higher installed <br />
Install the required Python libraries:
* Python
  ```sh
  pip install requests pandas matplotlib seaborn nltk
  ```
VADER sentiment lexicon used by NLTK is needed and can be downloaded by: <br />
* Python
   ```sh
   import nltk
   nltk.download('vader_lexicon')
    ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/github_username/Customer-product-review-analyzer.git
   cd Customer-product-review-analyzer
   ```
2. Run the script:
   ```sh
   python main.py

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

This project can be used for:
- Simulating product review sentiment when real reviews are unavailable
- Testing recommendation or ranking algorithms with sentiment-based star ratings
- Practicing NLP and sentiment analysis using VADER and fake data
- Learning data visualisation with seaborn and matplotlib

<!-- LICENSE -->
## License
Distributed under the MIT license. See `LICENSE.txt` for more information.

<!-- CONTACT -->
## Contact

David Balogun: davebalogun2015@gmail.com

Project Link: https://github.com/Chlasp/Customer-product-review-analyzer

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[license-shield]: https://img.shields.io/github/license/github_username/Customer-product-review-analyzer.svg?style=for-the-badge
[license-url]: https://github.com/github_username/Customer-product-review-analyzer/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: www.linkedin.com/in/david-balogun-428a0b329
[product-screenshot]: images/screenshot.png
