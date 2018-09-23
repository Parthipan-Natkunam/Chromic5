# Chromic5    [![Codacy Badge](https://api.codacy.com/project/badge/Grade/c12c0424f9834197a571a3f1d4011b47)](https://www.codacy.com/app/Parthipan-Natkunam/Chromic5?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Parthipan-Natkunam/Chromic5&amp;utm_campaign=Badge_Grade)
A color theory based color scheme generation library for python 3

## Details
A color scheme generation library for python to simplify the coding of color and color theory based software tools
such as palette generators.

## Video Demo
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b72b4f8f8f81485d9c52ad4a4dcc033b)](https://app.codacy.com/app/Parthipan-Natkunam/Chromic5?utm_source=github.com&utm_medium=referral&utm_content=Parthipan-Natkunam/Chromic5&utm_campaign=Badge_Grade_Settings)
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/Z-Ris04jfjw/0.jpg)](https://www.youtube.com/watch?v=Z-Ris04jfjw)

## Usage
- Please install the library on your machine.
- After installing the library import it to your project source:
```python
    from chromic5 import *
```
#### Generating Monochrome Colors:
To generate monochrome colors the ```monocolors``` method is to be used.
It is available in the ```Monochrome``` class.
The monocolors method accepts two params:
1. The RGB code of the color whose monochrome pallette is to be generated (passing ```None``` will pick a random color).
2. The number of colors to be in the generated pallette.(default is 2)

|param Details| Type | Default|
|---|---|---|
|RGB code string starting with # of The color to start the pallette with|String|None|
|Number of colors to be generated|Integer|2|

##### example:
```python
    colorData = Monochrome()
    colors = colorData.monocolors(None,5)
```
*more usage instructions will be updated soon...*
