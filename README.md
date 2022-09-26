# Instalation
## 1. Kedro-tutorial
``` python kedro new --starter=spaceflights ```

``` python pip install -r "/src/requirements.txt" ```

``` python kedro pipeline create data_engineering ```

``` python python -m venv env ```

``` python .\Scripts\activate.ps1 ```

## 2. Kedro-hooks
### What are hooks?
Pieces of code that allow us to inject our own code into the framework.
[Documentation](https://kedro.readthedocs.io/en/stable/hooks/introduction.html)

#### Hooks specification:
after_catalog_created

before_node_run

after_node_run

on_node_error

before_pipeline_run

after_pipeline_run

on_pipeline_error

before_dataset_loaded

after_dataset_loaded

before_dataset_saved

after_dataset_saved

after_context_created


### Instruction
1. Create a python file
2. Go to settings.py and add hooks
