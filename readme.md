# Python Mini Projects – Angela Yu's 100 Days of Code

This repository contains Python mini projects I’ve built while following [Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/).

## 📘 About the Course

Angela Yu's course is a comprehensive, beginner-friendly Python bootcamp designed to take you from the basics to advanced programming concepts through hands-on coding challenges. The course covers topics including data types, control flow, functions, object-oriented programming, web scraping, automation, and GUI application development.  

This repository captures my progress during the initial phase of the course, focusing on fundamental Python concepts and practical mini projects.

## 🔧 Setup

To run any of the projects in this repository, first install the required external libraries:

```bash
pip install -r requirements.txt
```

## ✅ Concepts and Skills Covered So Far

### 🧠 Core Python Programming  
- Variables, data types, and string manipulation  
- Conditional statements, logical operators, and control flow  
- Functions, loops, and writing reusable code  
- Lists, dictionaries, sets, and randomization techniques  
- Scope in Python: global, local, and constants  
- Basic algorithmic problem solving  
- Error handling with `try-except` blocks  
- File handling and filesystem operations  

### 🔧 Python Standard Libraries  
- `random` for randomness and simulations  
- `datetime` for working with dates and scheduling  
- `smtplib` for sending emails via SMTP  
- `os` for interacting with the operating system  
- `dotenv` for managing environment variables  
- `requests` for making API calls (GET requests)  
- `time` for delays and timing control  

### 🧪 Debugging and Tools  
- Debugging strategies and clean code practices  
- Using Thonny and IDE debuggers to trace and fix bugs  

### 👨‍🏫 Object-Oriented Programming (OOP)  
- Creating and using classes, methods, and objects  
- Refactoring procedural code into OOP structure  

### 🐢 Graphics and UI  
- Turtle graphics and event listeners  
- GUI applications using Tkinter (buttons, labels, inputs, canvas)  

### 📊 Data and External Libraries  
- Using external libraries like `pandas`, `numpy`, `matplotlib`, `colorgram`, etc.  

### 🌐 APIs and Automation  
- Fetching real-time data from external APIs (`kanye.rest`, ISS API, sunrise-sunset API)  
- Automating workflows such as email alerts, UI updates, and habit tracking using external data  
- Understanding and using common HTTP methods for RESTful API interactions:  
  - `GET`: Retrieve data from APIs (e.g., quote fetchers, weather, space data)  
  - `POST`: Submit new data to servers (e.g., logging habits or workouts)  
  - `PUT`: Update existing resources (e.g., modifying previously logged data)  
  - `DELETE`: Remove resources from external services (e.g., deleting habit log entries)  

### 🕸️ Web Scraping and Parsing
- Extracting structured data using **BeautifulSoup** from static HTML pages (e.g., Empire Online, Hacker News, Billboard Hot 100)  
- Parsing HTML elements using CSS selectors and element attributes  
- Saving scraped data to files (`.txt`) and using it for API-based workflows  

### 🧠 Browser Automation 
- Using **Selenium WebDriver** to automate browser interactions (clicks, form filling, navigation)  
- Handling dynamic content, modal popups, and element detection  
- Automating online games (e.g., Cookie Clicker) and job applications on LinkedIn  
- Collecting real-time speed test results from websites like Speedtest.net  
- Implementing user input workflows and captcha pauses  

## 🚀 Projects Completed

### Day 01
- [Band Name Generator](./Day%2001/bandNameGenerator.py)  
  Generates a band name using the user's city and pet name.

### Day 02
- [BMI Calculator](./Day%2002/bmiCalculator.py)  
  Calculates Body Mass Index (BMI) based on user input.
- [Tip Calculator](./Day%2002/tipCalculator.py)  
  Calculates tip per person based on total bill and number of people.

### Day 03
- [Treasure Island](./Day%2003/treasureHunt.py)  
  Text-based adventure game using conditional logic.
- [Pizza Order Program](./Day%2003/pythonPizzaStore.py)  
  Calculates pizza cost based on user preferences.
- [Roller Coaster Ride Check](./Day%2003/rollerCoaster.py)  
  Checks ride eligibility and calculates ticket price.

### Day 04
- [Coin Toss Game](./Day%2004/coinTossGame.py)  
  Simulates a heads or tails coin flip.
- [Rock Paper Scissors](./Day%2004/rockPaperScissors.py)  
  Classic RPS game: user vs computer.

### Day 05
- [Password Generator](./Day%2005/passwordGenerator.py)  
  Generates random, secure passwords using letters, numbers, and symbols.

### Day 06
- [Maze & Hurdle Problems - Reeborg's World Challenges](./Day%2006/)  
  Solves maze and hurdle courses using loops and logical functions.

### Day 07
- [Hangman Game](./Day%2007/hangman.py)  
  Word-guessing game with lives and ASCII art stages.

### Day 08
- [Caesar Cipher](./Day%2008/customCaesarCipher.py)  
  Encrypts and decrypts messages using Caesar Cipher logic.

### Day 09
- [Blind Auction](./Day%2009/blindAuction.py)  
  Accepts secret bids from users and reveals the highest bidder.

### Day 10
- [Calculator](./Day%2010/calculator.py)  
  Performs arithmetic operations with function-based logic and input loops.

### Day 11
- [Black Jack](./Day%2011/blackJack.py)  
  Simulates a simplified version of the card game Blackjack.

### Day 12
- [Number Guessing Game](./Day%2012/numberGuessingGame.py)  
  User must guess a number chosen by the computer in limited attempts.

### Day 13
- No code – Focused on debugging strategies and tools like Thonny and IDE debuggers.

### Day 14
- [Higher Lower Game](./Day%2014/higherLowerGame.py)  
  Guess which of two accounts has more social followers.

### Day 15
- [Virtual Coffee Machine](./Day%2015/virtualCoffeeMachine.py)  
  Simulates a CLI coffee machine with resource checks and coin processing.

### Day 16
- [Virtual Coffee Machine (OOP)](./Day%2016/main.py)  
  Refactored Day 15 using classes and object-oriented design.

### Day 17
- [True or False Quiz](./Day%2017/main.py)  
  A quiz that pulls questions from an API and tracks score.

### Day 18
- [Spirograph](./Day%2018/spirograph.py)  
  Draws colorful circular spirograph patterns using Turtle graphics.
- [Color Extractor](./Day%2018/color_extractor.py)  
  Extracts dominant colors from an image using `colorgram`.
- [Hirst's Dot Painting](./Day%2018/hirst_dot_painting.py)  
  Generates a dot painting inspired by Hirst using extracted colors.

### Day 19
- [Turtle Sketcher](./Day%2019/turtle_sketcher.py)  
  Draws on the screen using keyboard-controlled turtle.
- [Turtle Race](./Day%2019/turtle_race.py)  
  Simulates a race among turtles with random speeds.

### Day 20 and 21
- [The Snake Game](./Day%2020%20and%2021/snake_game.py)  
  Classic snake game built with Turtle graphics, including collisions and scoring.

### Day 22
- [Pong Battle](./Day%2022/pong_battle.py)  
  Two-player Pong game with bounce physics using Turtle module.

### Day 23
- [Turtle Crossing Game](./Day%2023/turtle_crossing.py)  
  Avoid the traffic and cross the road — a Frogger-style game.

### Day 24
- [Letter Generator](./Day%2024/main.py)  
  Generates personalized letters using name templates and file I/O.

### Day 25
- [U.S. States Quiz](./Day%2025/main.py)  
  Learn U.S. states by guessing names shown on a blank map.

### Day 26
- [NATO Alphabet Converter](./Day%2026/main.py)  
  Converts words into their NATO phonetic alphabet representation.

### Day 27
- [Miles to Kilometers Converter](./Day%2027/main.py)  
  A simple Tkinter GUI to convert miles into kilometers.

### Day 28
- [Pomodoro Timer](./Day%2028/main.py)  
  GUI-based productivity timer implementing the Pomodoro technique.

### Day 29
- [Password Manager](./Day%2029/main.py)  
  A GUI tool to generate and store passwords securely using JSON.

### Day 30
- Focus on error handling using `try-except` blocks.  
  Added JSON management and exception handling in:
  - Password Manager
  - Snake Game

### Day 31
- [French Flashcards App](./Day%2031/main.py)  
  Learn French vocabulary using a GUI flashcard app with flip animations.

### Day 32
- [Weekly Quote Script](./Day%2032/main.py)  
  Sends a motivational quote via email every Monday.  
  📁 **Environment Setup:** See [Day 32 readme.md](./Day%2032/readme.md)

### Day 33
- [Kanye Quotes GUI](./Day%2033/kanye_quotes/)  
  A Tkinter GUI app that fetches random Kanye West quotes from the [kanye.rest](https://api.kanye.rest/) API.

- [ISS Overhead Project](./Day%2033/iss_overhead/)  
  Sends an email alert when the ISS is overhead at night.  
  📁 **Environment Setup:** See [Day 33 readme.md](./Day%2033/readme.md)

### Day 34  
- [Quiz App](./Day%2034/main.py)  
  A GUI-based quiz application using the OpenTrivia API.

### Day 35  
- [Rain Alert System](./Day%2035/main.py)  
  Checks weather and sends SMS if rain is expected using OpenWeather + Twilio APIs.  
  📁 **Environment Setup:** See [Day 35 readme.md](./Day%2035/readme.md)

### Day 36  
- [Stock & News Alert System](./Day%2036/main.py)  
  Monitors stock prices and news; sends alerts via SMS using Alpha Vantage + GNews + Twilio.  
  📁 **Environment Setup:** See [Day 36 readme.md](./Day%2036/readme.md)

### Day 37  
- [Pixela Habit Tracker](./Day%2037/main.py)  
  Track daily progress with Pixela API — supports graph, pixel CRUD.  
  📁 **Environment Setup:** See [Day 37 readme.md](./Day%2037/readme.md)  
  🔗 **Live Graph:** [View on Pixela](https://pixe.la/v1/users/mxlfunction/graphs/graph1.html)

### Day 38  
- [Exercise Tracker](./Day%2038/main.py)  
  Log workouts using Nutritionix + Sheety APIs from natural language input.  
  📁 **Environment Setup:** See [Day 38 readme.md](./Day%2038/readme.md)

### Day 45  
- [Empire's Best Movies Scraper](./Day%2045/Top%20100%20Movies/main.py)  
  Scrapes the top movies list from *Empire Online's* "Greatest Movies" article and saves the titles in reverse order to a text file.  
  📄 **Output:** `movies.txt` containing the movie titles.

- [Hacker News Top Article Finder](./Day%2045/Top%20100%20Movies/main.py)  
  Scrapes the *Hacker News* homepage to identify the article with the highest upvotes, displaying its title, link, and score.

### Day 46  
- [Billboard Time Machine](./Day%2046/main.py)  
  Travel back in time to any Billboard Hot 100 chart date, scrape the top 100 songs, and create a private playlist on your Spotify account with matching tracks.  
  📁 **Environment Setup:** See [Day 46 readme.md](./Day%2046/readme.md)

### Day 47  
- [Amazon Price Tracker](./Day%2047/main.py)  
  Monitors a product’s price on Amazon and sends you an email alert if the price drops below your specified threshold.  
  📁 **Environment Setup:** See [Day 47 readme.md](./Day%2047/readme.md)

### Day 48  
- [Cookie Clicker Bot](./Day%2048/main.py)  
  Automates the Cookie Clicker game using Selenium by repeatedly clicking the cookie and purchasing the best available items over a 5-minute session.  

### Day 49  
- [LinkedIn Easy Apply Bot](./Day%2049/main.py)  
  Automates job applications on LinkedIn using Selenium. It logs in, visits job listings, and applies to all jobs with an "Easy Apply" button.  
  📁 **Environment Setup:** See [Day 49 readme.md](./Day%2049/readme.md)

### Day 51  
- [Internet Speed Bot](./Day%2051/main.py)  
  Uses Selenium to automate Speedtest.net and fetch current download and upload internet speeds. Displays results in the console.  
  
---

## 👩‍🏫 Credits

Course by [Dr. Angela Yu](https://www.udemy.com/user/angela-yu/)  
Udemy: [100 Days of Code – The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)
