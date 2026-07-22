from dataclasses import dataclass
import math
import numpy as np 

@dataclass
class config :

    Bore:float=0.127
    stroke_length:float=0.127
    connecting_rod_length:float=0.1524

    cylinders=4
    compression_ratio:float=10.5
    valves_per_cylinder=2

    intake_pressure=101325
    intake_temp=300
    exhaust_pressure=101325
    wall_temperature=450

    fuel:str="gasoline"

    no_active_cylinder=4

    spark_initiation=None
    combustion_range=None

    start_angle=0
    end_angle=720

