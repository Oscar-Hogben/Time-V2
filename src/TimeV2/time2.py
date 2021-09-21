import threading, time

def timer(time_length = False, message = False, variable = False):
  try:
    time_length = int(time_length)
  except:
    exit("FATAL ERROR: Expected intager with 'timer()''")
  global completed_message
  global timer_length
  timer_length = time_length
  completed_message = message
  def sub_timer():
    global timer_length
    global completed_message
    time.sleep(timer_length-1)
    time.sleep(0.5)
    if completed_message:
      print(completed_message)
    if variable:
      file = open(variable, "w")
      file.write("True")
      file.close()
  t = threading.Thread(target=sub_timer)
  t.start()
def wait(time_length = False, message = False):
  try:
    time_length = int(time_length)
  except:
    exit("FATAL ERROR: Expected intager with 'wait()'")
  time.sleep(time_length)
  if message:
    print(message)
def time_now(time_to_convert = time.time()):
  try:
    time_to_convert = int(time_to_convert)
  except:
    exit("FATAL ERROR: argument with 'time()' has to be a unix timestamp")
  return time.ctime(time_to_convert)
def unix():
  return int(time.time())

def stopwatch_start():
  global stopwatchStartTime
  stopwatchStartTime = time.time()
  return "Started!"
def stopwatch_stop():
  stopwatchLength = time.time()- stopwatchStartTime
  return stopwatchLength

