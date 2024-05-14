import uvicorn


def run_server(
    host: str = '0.0.0.0',
    port: int = 8000,
    reload: bool = False,
    log_level: str = 'info',
) -> None:
    uvicorn.run(
        'config.fastapi:fastapi',
        host=host,
        port=port,
        reload=reload,
        log_level=log_level,
    )
