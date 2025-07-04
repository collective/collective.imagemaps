# this tasks can be used by Python invoke command
# $ invoke start

from invoke import task


@task
def start(c):
    print("starting Plone")
    c.run("uv run runwsgi instance/etc/zope.ini")


@task
def install(c):
    print("installing Plone")
    c.run("uv sync")