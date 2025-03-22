from src.ui.app import app

if __name__ == "__main__":
    app.mainloop()


# from src.infra.server.server import create_app

# if __name__ == "__main__":
#     app = create_app()
#     app.run(host="0.0.0.0", port=3000, debug=True)

# from src.infra.composers.linkedin_composer import linkedin_composer
# from src.infra.middlewares.error_handle import error_handler


# @error_handler
# def execute() -> None:
#     """
#     Run Linkedin
#     """
#     linkedin = linkedin_composer()
#     linkedin.execute()


# execute()
