# pcmax-genetic-python

This is a python implementation of genetic algorithm solving simplified PCmax (process scheduling).

## Installation
- install python 3
- install dotenv-python package

## Running
Make sure scripts are executable
```
chmod u+x *.py
```

Then, run them like a shell script
```
./pcmax-genetic.py m10.txt
```

*.txt files are instances. You can also generate your own with 
```
./pcmax-generate <number>
```
where `<number>` is the number of processors.
