## Pybstts

- A fairly simple tts library in python.

> [!Warning]
> library is not yet finished.

usage :

```python
from pybstts import Engine

engine = Engine('_espeak')
engine.init()
engine.speak('Hello, World!')

```

### Supported tts

- espeak

### Supported platform 

- Termux

requirements:

```sh
~$ pkg install espeak espeak-static
```
### Build instructions

reqirements:
```sh
~$ pip install build wheel 
```
To build:
```sh
~$ bash build.sh
```
