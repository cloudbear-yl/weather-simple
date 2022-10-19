# weather-simple

Goal:
Create a simple rainfall app that generates real-time data rainfall data when user inputs area name.
Data is extracted from data.gov.sg

This project is a technical assessment.

# Initial thoughts when recieved task:

Step 1: Figure out how to write the application
Step 2: When keying in the application, end result to have a log. Input and outputs
Step 3: What does http://localhost.8080 means?
Step 4: How does it work?
Step 5: Read on how to containerize the work and run minikube

Being a beginner in this field, I went with the only coding language which I had learn during my 3-months bootcamp and decided to use Python.
With my limited knowledge, this task gave me a chance to explore this coding langauge by myself.

# Step 0: How to start with only an URL?

> API Url provided in the task sheet. What can I do with it to retrieve the details?
> Through my 3-months bootcamp, I have interatcted with API_url and API key before. My instructor have touch and go on this topic which I barely rememeber.
> At this point, I was focusing on how to get the API key since URL was provided.
> Many hours was spent on this topic and there was no answer. I was looking around data.gov.sg Developers site for a portal to generate an API key. Thinking the process would be similar to many openWeather API tutorials.
> Gave up looking for the key.
> Instead re-look into the URL provided and went to the website itself.
> Observed the different options by toggling with the "Execution" button on the website. At this point, realised that the URL changes dependent on the date and time.
> It clicks that I do not need a key. Instead, having the date and time is crucial.

# Step 1: How to write the application?

My step-by-step process.

1. Get out the codes
2. Try to get the outputs that the assessment needs
3. Figure out how to host on port 8080

## Getting out the codes

First, figure out the correct URL to get the correct real-time update.
Second, I have the correct URL. How to retrieve the data via Python codes? - I remembered in my 3-months bootcamp. I changed the data into a JSON file - Hence, I did the same thing.
Third, JSON file opened and analyzed the data. - Realised the file is either a nested dictionary or nested list. - Analyzed that to get to the rainfall_value. I need to get the area name > retrieve device_id > Go to another list compare to station_id > obtain rainfall_value
Fourth, so I kept going back and forth figuring out how to loop through list and dictionaries to get the final value
Fifth,
