# PySecurityCameras

## Introduction

PySecurityCameras is an application which finds optimal arrangement of cameras located in collection od rooms. Cameras and rooms are difined as shapes on 2D plane - camera being a circle and room being a rectangle. Search of the best coordinates is performed using Simulated Annealing algorithm.

## Configuration

### Configuration file

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

Type of cooling is configured through property "type" of object "cooling" in _./config.json_ file. There are three types of cooling (where i is a number of iteration):

1. Logarithmic - set "type" to "log"

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://www.codecogs.com/eqnedit.php?latex=T_i&space;=&space;\frac{\tau}{1&plus;log(1&plus;i)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_i&space;=&space;\frac{\tau}{1&plus;log(1&plus;i)}" title="T_i = \frac{\tau}{1+log(1+i)}" /></a>

2. Linear - set "type" to "lin",

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://www.codecogs.com/eqnedit.php?latex=T_i&space;=&space;\tau&space;-&space;bi" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_i&space;=&space;\tau&space;-&space;bi" title="T_i = \tau - bi" /></a>


3. Exponential - set "type" to "exp"

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://www.codecogs.com/eqnedit.php?latex=T_i&space;=&space;\tau&space;-&space;b^i" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_i&space;=&space;\tau&space;-&space;b^i" title="T_i = \tau - b^i" /></a>

## Execution

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

## Hyperparameters fine-tuning 

### Configuration

Hyperparameters can be found using experiments which can be performed by running the _./experiments/main.py_ file. In configuaraion file _./experiments/experiment_config.json_ user can select examined parameter as well as intervals from which values are sampled. Experiment configuration file has a following structure:

<pre>
{
  "problem": {
    /*
      object from _./config.json_ file
    */
  },
  "interval": {
    "beg": 0.5,
    "end": 1
  },
  "num_values": 10,
  "num_tries": 10,
  "param": "beta",
  "tested": "cost"
}
</pre>

where:

* **"problem"** -  object from _./config.json_ file.

* **"interval"** - numerical interval from which values of examined parameter are sampled.
    * **"beg"** - beginnig of the interval.
    * **"end"** - end of the interval.

* **"num_values"** -  number of samples.

* **"num_tries"** -  number of tries on one sample.

* **"param"** - name of parameter which is a independent variable.

* **"tested"** -  name of parameter which is a dependent variable with 5 possible values:
    * **"cost"** - value of cost function.
    * **"num_cameras"** - value of cameras' number.
    * **"unobserved_fraction"** - fraction of unobserved checkpoints to observed ones.
    * **"exec_time"** - execution time.

## Execution

### Input

* _./experiments/experiment_config.json_

### Run

<pre>
cd PySecurityCameras/experiments
python main.py
</pre>


### Output

In a result a _./experiments/{param}\_test\_on\_{tested}.png_ is generated.

### Examples of experiments results

![example of experiment](https://i.imgur.com/kC7MJ3T.png)