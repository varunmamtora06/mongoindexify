# Export Indexes
The main use of this script is to export indexes of one collection to other. The reason for creating this was: I had encountered a situation at my work where in I had to manually create indexes on my local mongo servers collection which were there on production mongodb server. So to reduce manual work, this script was written.

## Senerio to use this script
- Took a data dump of a source collection on a destination db's collection but indexes were not included.
- Used ```mongoimport``` command to create a collection on destination db to import documents from a ```json``` type of dump.

## Usage
- Clone the repo and change current working directory to it.
- Create an env and activate it.
- Install the requirements: ```pip install -r requirements.txt```
- Run following
```
python main.py -src="<source_conn_str>" -srcdb="<source_db>" -srccoll="<source_collectn>" -dest="<dest_conn_str>" -destdb="<dest_db>" -destcoll="<dest_collectn>"
```