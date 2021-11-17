from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/launch.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage_report(ctx):
    ctx.run("coverage run --branch -m pytest src; coverage report -m; coverage html")
