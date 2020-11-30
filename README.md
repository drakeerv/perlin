# perlin
======

Create perlin noise in 1D, 2D, and 3D!

## Features

- 1D perlin noise
- 2D perlin noise
- 3D perlin noise
- Seed capability
- Tested
- Completly written in python
- No dependencies

## Usage

This library can be used for generating random terrain for games or getting perlin noise. This library also supports octaves.

## Example

import perlin

p = perlin.Perlin(6789)

```python
print(p.one(0))
print(p.two(0, 0))
print(p.three(0, 0, 0))
```

## Know limitations

Slower than noise library
Slower with octaves (Work in progress)
Some bugs on different seeds

## New Features

Now has octave support!
