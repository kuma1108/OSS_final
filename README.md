# 2021_Spring OSS FINAL

##Study Planner
##What Does This Project Do
This program helps you to study better. According to your class schedule and school's academic calendar, this program creates a schedule for when to review your lectures.

##Why is This Project Useful?
This program suggests to review a lecture at least three times(a day, a week, and a month after you first listened to a lecture). It would encourage your academic achievement by ensuring the material stays in your (relatively) long term memory.

### Contribution
This project is from https://github.com/vitchyr/StudyPlanner

The original project creates a semester-long schedule with corresponding dates. I selected the schedules for a day, so that the user could easily recognize the day planner

I also made a webpage for checking daily schedule, in order to easily access. It automatically updates the schedule according to the current day.

To do this, I modified some codes to make the data appropriate for extracting, and for printing on a webpage, and created a makefile to make it easier. 

### Install Requirements
Python

Every requisites are written in 'requirements.txt'
You can simply install them by
```
pip install -r requirements.txt
```

### How to Use
Edit classes.json and calendar.json and then run:
```
make
```


### classes.json
`classes.json` represents your class schedule. It's a dictionary from a class
name to the day of the week that you have that class. Here is an example:

```
{
  "ECE 4730": ["M", "W"],
  "ECE 3400": ["M", "W", "F"],
  "CS 4670": ["M", "W", "F"],
  "CS 4752": ["M", "W", "F"],
  "ECE 4250": ["T", "R"]
}
```

Days of the week are: M = Monday, T, W, R, F, S, U.

### calendar.json

`calendar.json` represents the school's academic calendar. Namely, the start
date, the end date, and vacation days. The provided calendar.json is the
Cornell Spring 2015 calendar. Here it is with some comments:
```
{
  "start": "1/21/2015",       <- first day of class
  "end": "5/6/2015",          <- last day of class
  "vacations": [
    {
      "start": "2/14/2015",
      "end": "2/17/2015"      <- this should be the last day you're on vacation
    },
    {
      "start": "3/28/2015",
      "end": "4/5/2015"
    },
    {
      "start": "4/27/2015",   <- have the same start and end dates to indicate
      "end": "4/27/2015"         that only one day was off
    }
  ]
}
```

###Where Can I Get More Help, If I NEED?
Please contact me 21900055@handong.edu
