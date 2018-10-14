from modules import *
from meta_commands import *
import parse_sensor_data
import time

# Decide Which Module To Run
def run_modules(sensors, modules, run_meta, module_state):
  high_command = None
  last_state = None

  # Run Each Module & Store Corresponding Meta Command Of Module With Highest Priority
  for module in reversed(modules):
    result = module({
      'sensors': sensors,
      'is_running': module == module_state
    })
    has_command = result['has_command']

    if has_command:
      meta_id = result['meta_id']
      data = result['data']

      high_command = (meta_id, data)
      last_state = module

  # Run Meta Command With Highest Module Priority, Return Prior Module
  if high_command:
    run_meta(*high_command)
    return last_state

  return None

# Run Meta
def run_meta(meta_id, data):
  meta_commands[meta_id](data)

# Main Loop
def main():
  state = None
  for i in range(30):
    time.sleep(1)
    state = run_modules(parse_sensor_data.encodedata(), modules, run_meta, state)

  parse_sensor_data.drone.land()
  parse_sensor_data,drone.halt()