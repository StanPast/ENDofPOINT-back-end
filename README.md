# M2X Heroku Python APP


## Introduction

This is an example of a Heroku application written in Python that reports data to [AT&T M2X](https://m2x.att.com). The application reports the current stock price of AT&T's stock (ticker symbol "T") every minute.

Please note that the Heroku machine and M2X are using times in UTC, not in your local time zone. M2X will, however, accept data in any time zone as long as the timestamp is formatted using ISO8601 (e.g. "2015-02-27T18:14:00.000-03:00").

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## License

This library is released under the MIT license. See ``LICENSE`` for the terms.
