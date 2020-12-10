# 2020 Netflix Wrapped :computer:

This is my version of the Spotify wrapped but using my Cousin and I's Netflix account. It displays a summary of our Netflix history since movies/tv series are mostly only watched once we focus more on the duration of seconds watched on days and the number of episodes watched within a series.

![Overview](https://drive.google.com/file/d/1sqfCThs2LUixkuk0BmStOvoFlHzEFsz4/view?usp=sharing)

### Step :one:

The first step was to locate the data within Netflix. 

![Login](https://drive.google.com/file/d/1BgoUncD_ymp_VDPmbC7r7d1ic05-yDXd/view?usp=sharing)

I was able to use Chrome's Inspect tools to find the data within My Account on the Viewing Activity  page. You will notice that every time you click the "Show More" button additional pages are generated within the network panel. You can also notice the links are the same other than "pg=n" where n starts at 0 and increments by 1 every time the button was clicked. I then choosed random numbers to see where 2020 started and 2019 ended. I found it to be on page 101. 

![Networking in Inspector Tools](https://drive.google.com/file/d/1Yv88aOXIAvWO82hKuV1DT3D_N5Nv1BWp/view?usp=sharing)

### Step :two:

The next step was to automate this task so I wouldn't have to do it 101 times. Therefore, I used the selenium in python to accomplish this. You will notice within the code. I open a new page for each link this is because you have to be logged in to Netflix to access the needed information. Opening new tabs was the easiest way to ensure this happened within 1 session. All this information was then dumped into a txt file.

![Automating Task](https://drive.google.com/file/d/1dxYtEzCPQHX-tZecgDlpAljQ5IYxYlkX/view?usp=sharing)

### Step :three:

**Note:** This step could've been done in python using JSON; however, it was quicker for me to use Excel as I was on a time crunch. 

Using the txt file from step 2, the following steps took place within excel:
* Data was loaded
* Data was separated on the "{" delimiter
* Data was transposed into a column
* Data was filtered to remove information such as profile name etc.
* Data was separated on the "," delimiter
* Inserted headers to each column
* Rows were then manually checked as series had more information than movies. In addition, if names had a comma within them the spacing for this row would be off; therefore, it would be manually fixed.
* Used find all to remove "dateStr:" and other titles within the row 
* Removed unwanted columns
* Data saved in CSV

![Cleaning Data](https://drive.google.com/file/d/1gLgpSR1p-gXe0JZbG-JyjVgNkF28p6ZN/view?usp=sharing)

### Step :four:

Then, used the cleaned CSV to gain useful information from the data using pandas. 
I was able to derive the following information:
* Movies vs TV Series Count
* Top 10 Series Watched and Number of Episodes Watched
* Top 5 Days of Viewing and Durations
* Number of Unique Series Watched
* First Watch for the Year
* First Watch for Quarantine
* Watch Duration for the Year (Seconds)

![Data Visualization](https://drive.google.com/file/d/1nAzDJIn8Y1vi1Ng_5StnG-4b9q02oB0H/view?usp=sharing)
