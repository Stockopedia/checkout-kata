# Simple checkout

A simple checkout which supports the following features:

## Requirements

* Buy n items, save x%, e.g. _"buy 2, save 20%"_
* Buy m items, get one free, e.g. _"buy 2, get one free"_
* Save y% when you spend z, e.g. _"save 5% when you spend £100 (after other discounts applied)"_ 

## How to step-through the work-flow

Each step in the process of writing tests has a git tag of the form `step-n`.

Start with `step-1` and work your way forward to `step-11`:

```bash
git checkout step-1
# ...
git checkout step-2
# etc.
```

To run the tests you will need to build the Docker image associated with the project. This can be done with:

```bash
docker build -t checkout .
docker run --rm -v `pwd`:/opt/checkout checkout
```

You will not need to re-build the image between each step, but a new dependency was added along the way. It's actaully easiest to run the docker build when git is pointing at `HEAD` before checking-out `step-1` as this will have all the requsiste dependencies.
