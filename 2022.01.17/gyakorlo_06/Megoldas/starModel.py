# File: starModel.py
# Author: Kriston Attila
# Copyright: 2021, Kriston Attila
# Group: Infra I/N
# Date: 2022-01-17
# Github: https://github.com/kristonattila
# Licenc: GNU GPL


class StarModel:
    def __init__(self, name, constellation, distance, mass, temperature, age):
        self.name = name
        self.constellation = constellation
        self.distance: float = distance
        self.mass = mass
        self.temperature = temperature
        self.age = age

