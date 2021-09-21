# Time v2
## About
* A simple replacement of the common `time` module
## How to install
* 1: Type `pip install TimeV2` in your shell
* 2: Type `from TimeV2 import time2` at the top of your script
## Module Features
### `time2.timer()`
* Creates an asynchronous timer
* 1st argument: timer length
* 2nd argument: Finnished message
### `time2.wait()`
* Sartes a simple timer that pauses your script until done
* 1st argument: timer length
* 2nd argument (optional): Finnished message
### `time2.time_now()`
* Returns the current time or the time of a unix timestamp
* 1st argument (optional): unix timestamp
### `time2.unix()`
* Returns the current uix timestamp
### `time2.stopwatch_start()`
* Starts a stopwatch
### `time2.stopwatch_stop()`
* Stops an already started stopwatch
* Returns the length of the stopwatch
