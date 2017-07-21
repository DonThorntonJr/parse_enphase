# parse_enphase

Scripts to Parse Enphase Energy System Overview webpage for use in custom sensor for PRTG.

### Requirements

The scripts require the following Python dependencies:

* [requests] - Python HTTP request library.
* [BeautifulSoup] - Python library for pulling data out of HTML and XML files.

### Usage

```
python parse_enphase-json.py "http://<enphase webpage>/"
```

```
{
  "prtg":
  {
      "result": [
        {
          "channel": "Currently Generating (W)",
            "value": "1830"
        },
        {
          "channel": "Number of Microinverters Online",
            "value": "35"
        }
      ]
  }
}
```
