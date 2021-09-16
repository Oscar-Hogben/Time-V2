# Oscar's Time 2 Module
## About
* A simple replacement of the common `time` module
## How to install
* 1: Type `pip install OscarsTime2` in your shell
* 2: Type `from time2 import time2` at the top of your script
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
* Gets the current time or the time of a unix timestamp
* 1st argument (optional): unix timestamp
### `time2.unix()`
* Gets the current uix timestamp