# dd-python-utils

This project was setup with Poetry, a dependency management tool for Python: [Poetry docs](https://python-poetry.org/docs/). 
I imported it in PyCharm with the Poetry Plugin installed 
and I am running the code from the IDE, while editing it to my needs. 


To initialize run `setup-work.py`. 
 
This wil create a directory (by default `work`) for storing information (not code) that is needed for the task you are performing, 
but should not be kept in the Git repo. This is important, because we want to avoid that you accidentally share secret information 
by 'committing' and 'pushing' to Github for example. 

In this directory the setup places the configuration in the `config.ini` file. 
Initially this is a copy of the `config.ini.empty` file. 


Fill in the correct values for the Dataverse server URL and the API key if nedeed. 
Also create a `pids_to_process.txt` file or whatever other name you have configured, 
and place the doi's in there with `doi:` prefix and every doi on it's own line. 
After a 'run' the directory tree will look similar to the following: 

```
├── README.md (this file)
├── utils
│   ├── ... code
├── ... other stuff
└── work
    ├── config.ini
    ├── pids_mutated_20211101_174616.txt
    └── pids_to_process.txt
```

