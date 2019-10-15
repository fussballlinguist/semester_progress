# semester_progress
This perl script creates a tsv-file for automatized scheduling of tweets to run a bot like [Semester Progress](https://twitter.com/sem_progress/). Just adjust the beginning and end date of the semester (or any other period) you want to display in the script.

The script calculates the length of the period in seconds, divides it in 100 parts and creates a tweet with a progress bar for exactly the point in time at which a further percentage step is reached.

The format of the ouput is compatible with [autoChirp](https://autochirp.spinfo.uni-koeln.de/home), a small and easy-to-use webapplication to ease the scheduled publication of the tweets. Just create a new twitter account, log in at autoChirp, upload the tsv-file and there you go.

As you can see, this bot is inspired by the wonderful [Year Progress](https://twitter.com/year_progress).
