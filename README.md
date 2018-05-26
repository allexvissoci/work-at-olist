# Work at Olist

## Description

This project is a HTTP REST API, that receives call details and generate monthly bills for a given telephone number.
The call details is the initial call record and the end call record.

## Installing

* Start application

	Open the command line and run the next commands

```console
	git clone git@github.com:allexvissoci/work-at-olist.git
```
```console
	cd work-at-olist/
```
```console
	python3 -m venv env
```
```console
	pip install -r requirements.txt
```
```console
	source env/bin/activate
```
```console
	pip install -r requirement.txt
```
```console
	python manage.py migrate
```
```console
	python manage.py runserver
```

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

## List Bill

* List bill without reference:

	`https://work-at-olist-call-api.herokuapp.com/bill/?subscriber=<number>`

* List bill with reference:

	`https://work-at-olist-call-api.herokuapp.com/bill/?subscriber=<number>&reference=02/2018`

* Response:

```
	[
	    {
	        "destination": "41999814483",
	        "started_date": "2018-05-25",
	        "started_time": "11:00:00",
	        "duration": "3600.0",
	        "call_price": "1.00"
	    },
			...
	]
```
