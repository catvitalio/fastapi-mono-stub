# FastAPI stub

This repository is intended as a template for future projects with a monolithic architecture. The stub uses the following libraries and technologies:
- FastAPI
- SQLAlchemy
- FastAPI JWT (jwt auth)
- taskiq (background/periodic tasks)
- FastAPI Mail (emails sending)
- Ruff (code linter and formatter)
- Typer (CLI)

## Running the Server
To start the server, use Docker Compose::
```
docker compose up
```

You can also run the server in debug mode with debugpy running on port 5679:
```
docker compose -f docker-compose.debug.yml up
```

# TODO

- [ ] justfile / makefile
- [ ] translations
- [ ] admin constants
- [ ] ansible
