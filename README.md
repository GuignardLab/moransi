# Moran's Index

[![License MIT](https://img.shields.io/github/license/GuignardLab/moransi?color=green)](https://github.com/GuignardLab/moransi/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/moransi.svg?color=green)](https://pypi.org/project/moransi)
[![Python Version](https://img.shields.io/pypi/pyversions/moransi.svg?color=green)](https://python.org)
[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-orange.json)](https://github.com/copier-org/copier)

Compute Moran's Index for images or adjacency matrices

----------------------------------

## Installation

You can install `moransi` via [pip]:

```shell
pip install moransi
```

To install latest development version :

```shell
pip install git+https://github.com/GuignardLab/moransi.git
```

## Usage

You can use this code after installing it the following way:

```python
from moransi import morans_i_image

image = ... # opening an image
kernel = ... # A kernel for the weights of the neighbouring pixels

morans_i_image(image, kernel) # Returns the Moran's index
```

```python
from moransi import morans_i_adjacency_matrix

adjacency_matrix = ... # an adjacency matrix of size N by N.
                       # It is either binary or links weights
                       # adjacency_matrix[i, j] is >0 if there is an edge
                       # between i and j
metric = ... # An array of size N where metric[i] is the value of node `i`

morans_i_adjacency_matrix(image, metric) # Returns the Moran's index
```

## Contributing

Contributions are very welcome.

## License

Distributed under the terms of the [MIT] license,
"moransi" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
[tox]: https://tox.readthedocs.io/en/latest/

[file an issue]: https://github.com/GuignardLab/moransi/issues

