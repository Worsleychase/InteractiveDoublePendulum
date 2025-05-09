# Interactive Double Pendulum

An interactive double pendulum simulator built with Python and Matplotlib.  
This tool visualizes the chaotic motion of a double pendulum and allows real-time parameter tuning, trail visualization, and data collection.

## Features

- Adjustable parameters: masses, lengths, gravity, and time step via sliders.
- Real-time animation with pause, reset, and trail toggles.
- Data collection and export to CSV for further analysis.
- Built-in verification test to check simulation correctness.
- Minimal dependencies: just `numpy` and `matplotlib`.

## Dependencies
- Python (at least 3.9)
- Numpy
- Matplotlib
- TkAgg
## Recommended Installation: PyPI/pip

Install directly from PyPI:

```bash
pip install CW-DoublePendulum
```

### Usage

Once installed, launch the simulation with a small command:
```bash
CWDoublePendulum
```
This opens the interactive Matplotlib window.


## Alternative Installation: Git

Clone the repository
```bash
git clone https://github.com/Worsleychase/InteractiveDoublePendulum.git
```

### Usage

Navigate to the cloned directory then cd into CWDoublePendulum:
```bash
cd CWDoublePendulum
```
Run manual script/program:
```bash
python manualRun.py
```
or
```bash
python3 manualRun.py
```

## Controls
- Sliders: Adjust masses, lengths, gravity, and time step for the simulation.
- Checkboxes: Enable or disable trails for each pendulum mass.
- Buttons:
  - ```Pause```: Start or stop the simulation, does not change the state.
  - ```Reset```: Reset the _position_ of the simulation, parameters remain unchanged.
  - ```Collect Data```: Begin saving pendulum data to a CSV file.
  - ```Verify/test Simulation```: Run a hash-bashed verification test.

## Output
When data collection is active (by hitting ```Collect Data```), the simulator records:
- Positions (```x1```,```y1```,```x2```, ```y2```)
- Angles and angular velocities (```theta1```,```omega1```,```theta2```, ```omega2```)
- Simulation parameters (```l1```,```l2```,```m1```, ```m2```, ```g```, ```dt```)
- Timestamp (local system time)

## Testing
To verify the integrity of your simulation. Launch the simulation, using either of the methods mentioned above, and click the ```Verify/test Simulation``` button. This button will compute the SHA-256 hash of the state of the simulation after 1000 time steps and compare it to the verified, already working, hash in ```testHash.txt```. The result of the test is printed in the console/terminal.

## Known Issues/Bugs
- Quickly changing length(s). If you rapidly increase and decrease one of the lengths, the pendulums seems to gain energy and velocity. The "fix" to this issue is simply clicking reset so the positions and velocities are reset.
