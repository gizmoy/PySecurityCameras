# PySecurityCameras

### Introduction

PySecurityCameras is an application which finds optimal arrangement of cameras located in collection od rooms. Cameras and rooms are difined as shapes on 2D plane - camera being a circle and room being a rectangle. Search of the best coordinates is performed using Simulated Annealing algorithm.

### Configuration

Process of optimization can be configured through the _./config.json_ file which has following structure:

<pre>
{
  "boxes": [
    {
      "vertex": {
        "x": 0.0,
        "y": 0.0
      },
      "width": 0.3,
      "height": 1.0
    },
    {
      "vertex": {
        "x": 0.3,
        "y": 0.3
      },
      "width": 0.7,
      "height": 0.6
    }
  ],
  "cooling": {
    "type": "lin",
    "base": 0.001,
    "tau": 20.0
  },
  "camera_range": 0.15,
  "max_cameras": 10,
  "max_iterations": 20000,
  "distance": 0.02,
  "sigma": 0.1,
  "alpha": 1.0,
  "beta": 150.0,
  "h_exp": 1.0,
  "n_exp": 1.0,
  "verbose": true
}
</pre>

where:
* **"boxes"** - list of rooms' representations.
    * **"vertex"** - box's bottom left vertex.
        * **"x"** - vertex's x coordinate.
        * **"y"** - vertex's y coordinate.
    * **"width"** - box's width.
    * **"height"** - box's height.

* **"cooling"** - configuration of cooling.
    * **"type"** - cooling type (three possibilites: "log", "lin" & "exp").
    * **"base"** - initial baseline (see "Cooling" section).
    * **"tau"** - tau (see "Cooling" section).

* **"camera_range"** - camera's range of vision.
* **"max_cameras"** - maximum number of cameras.
* **"max_iterations"** - maximum number of iterations.
* **"distance"** - distance between checkpoints.
* **"sigma"** - standard deviation of new coordiantes (exploration).
* **"alpha"** - linear factor which scales loss component related to unobserved checkpoints (see "Loss function" section).
* **"beta"** - linear factor which scales loss component related to cameras number (see "Loss function" section).
* **"h_exp"** - exponent which scales loss component related to unobserved checkpoints (see "Loss function" section),
* **"n_exp"** - linear factor which scales loss component related to cameras number (see "Loss function" section).
* **"verbose"** - when true provides additional details about initialization and optimization.

### Loss function

![loss function](https://i.imgur.com/AOgwlkH.png)

where:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;h - number of unobserved checkpoints,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n - number of cameras.

### Cooling

To do...

### Input

* _./config.json_

### Run

<pre>
cd PySecurityCameras
python main.py
</pre>

### Output

After optimization following files are generated:
1. _./init.png_ - image with initial camera's arrengment.
2. _./out.png_ - image with final cameras' arrengment.
3. _./cost.png_ - image with value of cost function during optimization.

### Examples of results

On the left are final arrengments of cameras and on the right are values of loss functions during optimization.

![results](https://i.imgur.com/NBmmBjR.png)

### Hyperparameters tuning 

To do...