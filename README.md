# napari_polo

[![License](https://img.shields.io/pypi/l/napari_polo.svg?color=green)](https://github.com/allysonryan/napari_polo/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari_polo.svg?color=green)](https://pypi.org/project/napari_polo)
[![Python Version](https://img.shields.io/pypi/pyversions/napari_polo.svg?color=green)](https://python.org)
[![tests](https://github.com/allysonryan/napari_polo/workflows/tests/badge.svg)](https://github.com/allysonryan/napari_polo/actions)
[![codecov](https://codecov.io/gh/allysonryan/napari_polo/branch/master/graph/badge.svg)](https://codecov.io/gh/allysonryan/napari_polo)
[![Development Status](https://img.shields.io/pypi/status/napari_polo.svg)](https://en.wikipedia.org/wiki/Software_release_life_cycle#Alpha)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari_polo)](https://napari-hub.org/plugins/napari_polo)

A napari Plugin for Polarised Light Microscopy Analysis

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using haesleinhuepf's [cookiecutter-napari-assistant-plugin] template.

## Checklist
After the code for this plugin has been generated, go through this list:
* Write a minimal user guide below. Assume someone finds your plugin online and wonders how to quickly try it on your example data and on their data. Where should they start? What are the minimum necessary steps that need to be listed and explained? 
* Search for "TODO" in this file and the code to make sure all functions are properly documented.
* Make sure the requirements.txt correctly lists all dependencies and installation works as described below.
* Remove this checklist from the documentation.

## Usage

This plugin can be started from the menu `Tools > Segmentation / labeling > Generate clean labeled orientation image `.

TODO: Explain how to use your plugin.
* Tell the user for what kind of data this plugin was developed.
* Provide a link to example data (e.g. on https://zenodo.org) so that new users can apply your plugin to data it has been developed for, before they try it on their own data.
* Tell the user what values to enter and why. E.g. "if the resulting segmentation shows too large objects, enter a smaller sigma value."
* Tell the user how they can validate that your plugin processed their data properly.
* Please put a screenshot here, e.g. a `screenshot.png` in a sub-folder called `docs`. It serves as graphical abstract.

![image](https://github.com/allysonryan/napari_polo//raw/main/docs/screenshot.png)

<!-- TODO: uncomment this as soon as your plugin has been deployed to pypi (see instructions below)
## Installation

You can install `napari_polo` via [pip]:

    pip install napari_polo
-->

## Similar and related plugins

TODO: Use this section to list/link other napari plugins that have similar functionality or are compatible with yours.
* Think of users who wonder what functions to use to convert their data so that it is compatible to this plugin.
* Think of users who wonder what to do with the output of your plugin.
* Think of plugins that do similar things but work in different contexts.

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## Installation instructions for developers

Clone the github repository:

```
conda install git

git clone https://github.com/allysonryan/napari_polo.git

cd napari_polo

pip install -e .
```

## Deployment to collaborators

You can package your plugin as zip file and send it via email to collaborators. They can then install it using pip:

```
pip install napari_polo.zip
```

## Deployment to pypi (instructions for developers)

For deploying the plugin to the python package index (pypi), one needs a [pypi user account](https://pypi.org/account/register/) 
first. For deploying the plugin to pypi, one needs to install some tools:

```
python -m pip install --user --upgrade setuptools wheel
python -m pip install --user --upgrade twine
```

The following command allows us to package the souce code as a python wheel. Make sure that the 'dist' and 'build' folders are deleted before doing this:

```
python setup.py sdist bdist_wheel
```

This command ships the just generated package to pypi:

```
python -m twine upload --repository pypi dist/*
```

[Read more about distributing your python package via pypi](https://realpython.com/pypi-publish-python-package/#publishing-to-pypi).


## License

Distributed under the terms of the [BSD-3] license,
"napari_polo" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/haesleinhuepf/cookiecutter-napari-assistant-plugin
[file an issue]: https://github.com/allysonryan/napari_polo/issues
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
