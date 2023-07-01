# BusyBee
> Do not disturb notifier using Circuit Playground Express
> 

[![CyPI-image]][CyPI-uf2]

This is a very simple (even so I am becoming a Python Master :-)) implementation utilizing CircuitPy. It uses the slide switch as input to set the Do Not Disturb mode either ON (Flash the NeoPixels RED) or OFF.

![](header.png)

## Installation

See the [Install or Update Circuit Python](https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-quickstart) quickstart!

![Adafruit Circuit Playground Express](/images/circuitplayground_express.jpg)

They recommend using Mu, but I prefer VSCode and copying my busyBee.py to CIRCUITPY/code.py.
I wrote updateACE.py to automate this.

```sh
./updateACE.py
```

## Usage example

Extremely simple - merely slide the D7 switch to the left (with the USB oriented in a North fashion).

## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
make install
npm test
```

## Release History

* 0.1.0
    * first working implementation
    * CHANGE: Simple 1 sec flash of RED neopixels
* 0.0.1
    * Work in progress

## Meta

Timothy McMahon – [@timmac1962](https://twitter.com/timmac1962)

Distributed under the XYZ license. See ``LICENSE`` for more information.

[https://github.com/timmac62](https://github.com/timmac62/)


<!-- Markdown link & img dfn's -->
[CyPI-image]: https://circuitpython.org/assets/images/logo@2x.png
[CyPI-uf2]: https://downloads.circuitpython.org/bin/circuitplayground_express/en_US/adafruit-circuitpython-circuitplayground_express-en_US-8.1.0.uf2
[CyPI-url]: https://circuitpython.org/board/circuitplayground_express/
[CyPI-installation]: hhttps://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-quickstart

[GreatREADME]: https://dbader.org/blog/write-a-great-readme-for-your-github-project
