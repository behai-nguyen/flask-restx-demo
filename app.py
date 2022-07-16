"""Flask Application entry point."""

from flask_restx_demo import (
    create_app,
	db,
)	

app = create_app()

@app.shell_context_processor
def shell():
    return {
        "db": db,
    }