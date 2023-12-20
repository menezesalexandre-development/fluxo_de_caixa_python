def restart_app(file):
    with open(file) as f:
        exec(f.read())
