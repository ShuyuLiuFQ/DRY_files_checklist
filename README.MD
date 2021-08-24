# Overview

1, Find_Fox: generate a table list to see which is duplicated
2, Fox_Graph: generate the file dependency graph, `import {...} from lowerFile` in the `higherFile`,
then we have `lowerFile -> higherFile` in the graph, a file granularity

# Start

1. clone this repo to your local
2. create a virtual venv in the root folder
3. locates into venv 
   1. in windows: `venv\Scripts\activate`
4. `pip` is used here, run  `(venv) C:\..\..> pip install -r requirements.txt` to install necessary packages
5. run `Find_Fox`, which will generate a `report.csv`