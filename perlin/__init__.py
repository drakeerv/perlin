# -*- coding: utf-8 -*-
"""
# perlin
======

Create perlin noise in 1D, 2D, and 3D!

## Features

- 1D perlin noise
- 2D perlin noise
- 3D perlin noise
- Octaves
- Seed capability
- Tested
- Completly written in python
- No dependencies

## Usage

This library can be used for generating random terrain for games or getting perlin noise. This library also supports octaves. It outputs a number from -10 to 10.

## Example

import perlin

p = perlin.Perlin(6789) #6789 is the seed

print(p.one(0)) #1D, 0 is the X value
print(p.two(0, 1)) #2D, 0 is the X value and 1 is the Y value
print(p.three(0, 1, 2)) #3D,  0 is the X value, 1 is the Y value, 2 is the Z value

print(p.one_octave(0)) #Use this for octaves, you can ajust the octave variables but this gives you 2 octaves

## Known limitations

Slower than noise library
Slower with octaves (Work in progress)
Some bugs on different seeds

## New Features

Now has octave support!
"""

import math, random, statistics

class Perlin:
	def one(self,x):
                return int(sum(self.noise(x*s)*h for s,h in self.perlins)*self.avg)

	def one_octave(self,x,octaves=2,octave=1):
		noise = []

		for i in range(octaves):
			noise.append(int(sum(self.noise(x*s)*h for s,h in self.perlins)*self.avg))
			octave /= 10

		if octave > 1:
			return(round(statistics.mean(noise)))
		elif octave > 0:
			return(int(noise[0]))
		return 0

	def two(self,x,y):
		return int(sum(self.noise(x*s,y*s)*h for s,h in self.perlins)*self.avg)

	def two_octave(self,x,y,octaves=2,octave=1):
		noise = []

		for i in range(octaves):
			noise.append(int(sum(self.noise(x*s*octave,y*s*octave)*h for s,h in self.perlins)*self.avg))
			octave /= 10

		if octaves > 1:
			return round(statistics.mean(noise))
		elif octaves > 0:
			return int(noise[0])
		return 0

	def three(self,x,y,z): 
		return int(sum(self.noise(x*s,y*s,z*s)*h for s,h in self.perlins)*self.avg)

	def three_octave(self,x,y,z,octaves=2,octave=1):
		noise = []

		for i in range(octaves):
			noise.append(round(int(sum(self.noise(x*s*octave,y*s*octave,z*s*octave)*h for s,h in self.perlins)*self.avg)))
			octave /= 10

		if octaves > 1:
			return round(statistics.mean(noise))
		elif octaves > 0:
			return int(noise[0])
		return 0

	def __init__(self, seed):
		random.seed(seed)
		
		self.m = seed; p = list(range(self.m)); random.Random(seed).shuffle(p); self.p = p+p
		p = self.perlins = tuple((1/i,i) for i in (16,20,22,31,32,64,512) for j in range(2))
		self.avg = 8*len(p)/sum(f+i for f,i in p)

	def fade(self,t):
		return t*t*t*(t*(t*6-15)+10)

	def lerp(self,t,a,b):
		return a+t*(b-a)

	def grad(self,hash,x,y,z):
		h = hash&15; u = y if h&8 else x
		v = (x if h==12 or h==14 else z) if h&12 else y
		return (u if h&1 else -u)+(v if h&2 else -v)

	def noise(self,x=0,y=0,z=0):
		p,fade,lerp,grad = self.p,self.fade,self.lerp,self.grad
		xf,yf,zf = math.floor(x),math.floor(y),math.floor(z)
		X,Y,Z = xf%self.m,yf%self.m,zf%self.m
		x-=xf; y-=yf; z-=zf
		u,v,w = fade(x),fade(y),fade(z)
		A = p[X  ]+Y; AA = p[A]+Z; AB = p[A+1]+Z
		B = p[X+1]+Y; BA = p[B]+Z; BB = p[B+1]+Z
		return lerp(w,lerp(v,lerp(u,grad(p[AA],x,y,z),grad(p[BA],x-1,y,z)),lerp(u,grad(p[AB],x,y-1,z),grad(p[BB],x-1,y-1,z))),
					lerp(v,lerp(u,grad(p[AA+1],x,y,z-1),grad(p[BA+1],x-1,y,z-1)),lerp(u,grad(p[AB+1],x,y-1,z-1),grad(p[BB+1],x-1,y-1,z-1))))

class perlin(Perlin):
    pass
