# Calendar App WORKED EXAMPLE



Learning to interact with files, to read, write and understand the file system is the most important thing as no matter what you face in the future, if your understanding is limited you can always perform the equivelant functions by reading and writing to files.

## Objectives  sudo code
  
1. Create a text file, populate that file with a list of activities and the date
2. Make sure the format is machine readable i.e. 
```shell
05-01-2022, pay council tax
06-01-2022, buy birthday present for mum
```
Format notes:
- each line is a activity
- each line has a date and a task seperated by a comma
    - So the program will read each line
    - it will split items based on comma
    - first item is the date, second item is the activity
    - If there is a problem, skip the line and return error


# Architecture

![image.png](attachment:image.png)

# Date

python has a library called datetime, we can use this to get the currenttime using `datetime.now()` its a complex object with lots to learn, so the easiest thing for us is to simply convert it to a string, so we can use todays date to compare with dates in the file.


```python
import datetime

# this gets the date as a complex object 
now = datetime.datetime.now()

# this converts that object (we called now) to a string called todaysDate
todaysDate = now.strftime("%d-%m-%Y")
```


```python
now = datetime.datetime.now()
print(now)
```

    2022-01-15 18:55:39.306905



```python
print(todaysDate)
```

    15-01-2022


# learning notes 

- We used a program to draw out the rough architecture of our `calendar service` we called `calendarApp`
    https://www.draw.io/   
- We used notepad++ and opened the folder as a project. 
    - Sublime is a good and better program
    - but we decided pycharm is too complex and not really good for beginners

# command line 
by entering `cmd` in the search we can open command line, this is the proper way to interact with python.  

```shell
# change directory with cd
cd
# example, lets change directory to desktop
cd Desktop 

# get a list of files in current directory with dir

dir

# create a new folder with mkdir 

mkdir adamsNewFolder

# echo something to the screen 

echo hi

# create a file 

echo '' > myNewFile.txt

```

# working with Lists 

- we sometimes use the word `arrays` and `matrix` interchangably.   
- A list is just a grouping of items *strings, ints or other stuff*
- we use lists because we can group lots of items together and iterate them in a `for loop`, this lets us `process large volumes of data`

```
myFruit = ['apple','banana','grape','pear']
```



```python
myFruit = ['apple','banana','grape','pear']
```

### delete an item
```
myFruit.pop(0)
````


```python
myFruit.pop(0)
```




    'apple'




```python
myFruit
```




    ['banana', 'grape', 'pear']




```python
!export PATH=/Library/TeX/texbin:$PATH

```


```python

```
