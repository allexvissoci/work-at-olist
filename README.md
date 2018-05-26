# Work at Olist

## Description

This project is a HTTP REST API, that receives call details and generate monthly bills for a given telephone number.
The call details is the initial call record and the end call record.

## Installing

## Testing Instructions

	In project root folder, run:

```console
	python manage.py test
```


## Work Environment

|   |    |
|---|---|
|  Computer | Notebook Dell Intel Core i7 8GB 1TB |
|  O.S | Ubuntu 16lts  |
|  Editor | atom  |
|  Django| 2.0 |
|  Python |  3.5.2 |
|  djangorestframework | 3.8.2 |

# API documentation

## Create Call Records

* Start Call Record:

	`https://work-at-olist-call-api.herokuapp.com/startrecord/`

```
	{
	  "type": "start",
	  "timestamp": "2018-05-25T05:00",
	  "call_id":  "1",
	  "source":  "41999999984",
	  "destination": "41999999983"
	}
```

* End Call Record:

	`https://work-at-olist-call-api.herokuapp.com/endrecord/`

```
	{
	   "type": "end"
	   "timestamp": "2018-05-25T05:00"
	   "call_id": "1"
	}
```
