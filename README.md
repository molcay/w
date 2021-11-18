# w

w is a CLI for learning the city that you gave will be rainy or not tomorrow.

## Instruction to Setup and Run
* You can create a virtual environment.
```shell
python3 -m venv venv
```

* You can activate it the venv.
```shell
. ./venv/bin/activate 
# or in PowerShell
.\venv\Scripts\activate
```

* You can use the `requirements.txt` file to install dependencies.
```shell
pip install -r requirements.txt
```

* Now, you can run the cli and get the answer:
```shell
python -m w is-rainy Warsaw
# or 
python -m w is-rainy Tokyo
```

* or, you can run the tests:
```shell
python -m pytest .
```
