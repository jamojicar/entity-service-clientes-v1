# entity-service-clientes-v1

Exámen práctico. Juan Amador Mojica Rodriguez

## Getting Started

Clone this repository for local deploy.

### Prerequisites

- python3.9
- pip
- virtualenv

### Dependencies

Some dependencies are optional according of the requirements.
- zpy-api-core
- zpy-db-core

For more information see requirements.txt file

### Installing

- Create virtual environment, activate it and download all dependencies.

```
  virtualenv venv
```

- Clone repository

```

git clone https://github.com/jamojicar/entity-service-clientes-v1.git

```

## Running the tests

Load env vars

```bash
ENVIRONMENT=
```

Test use cases

```python

from src.di import customer_list

if __name__ == "__main__":
    customer_list_uc.execute(@usecase_repository_dependency)


```

Or test from handler

`````python
from dotenv import load_dotenv

load_dotenv()

from src.handler import handle

if __name__ == "__main__":
    handle({}, {})

`````

Use selenium or cucumber

## Built With

- Python 3.9
- zpy cli

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see
.

## Authors

- **jamojicar 2022** - _[Backend Developer](https://www.linkedin.com/in/jamojicar/)_

## Docker
Create image
- docker build -t miapp:1 .

Create container
- docker create -p5000:5000 --name exam miapp:1

Start container
- docker start exam