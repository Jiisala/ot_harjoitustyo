from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/launch.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage report -m; coverage html") 

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src")

@task
def dbinit(ctx):
    ctx.run("python3 src/init_db.py")
