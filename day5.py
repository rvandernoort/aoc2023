from collections import defaultdict
import re
from tqdm import tqdm

def get_soil_map(split):
  soil_maps, fertilizer_maps, water_maps, light_maps, tempareture_maps, humidity_maps, location_maps = [], [], [], [], [], [], []
  for i, soil_map in enumerate(split):
    if soil_map == 'soil-to-fertilizer map':
        fertilizer_maps, water_maps, light_maps, tempareture_maps, humidity_maps, location_maps = get_fertiziler_map(split[i+1:])
        return soil_maps, fertilizer_maps, water_maps, light_maps, tempareture_maps, humidity_maps, location_maps
    soil_map = soil_map.split()
    dest_start = int(soil_map[0])
    src_start = int(soil_map[1])
    range_len = int(soil_map[2])
    soil_maps.append((dest_start, src_start, range_len))

  return soil_maps, fertilizer_maps, water_maps, light_maps, tempareture_maps, humidity_maps, location_maps

def get_fertiziler_map(split):
  fertilizer_maps, water_maps, light_maps, tempareture_maps, humidity_maps, location_maps = [], [], [], [], [], []
  for i, fertilizer_map in enumerate(split):
    if fertilizer_map == 'fertilizer-to-water map':
        water_maps, light_maps, tempareture_maps, humidity_maps, location_maps = get_water_map(split[i+1:])
        return fertilizer_maps, water_maps, light_maps, tempareture_maps, humidity_maps, location_maps
    fertilizer_map = fertilizer_map.split()
    dest_start = int(fertilizer_map[0])
    src_start = int(fertilizer_map[1])
    range_len = int(fertilizer_map[2])
    fertilizer_maps.append((dest_start, src_start, range_len))

  return fertilizer_maps, water_maps, light_maps, tempareture_maps, humidity_maps, location_maps
  
def get_water_map(split):
  water_maps, light_maps, tempareture_maps, humidity_maps, location_maps = [], [], [], [], []
  for i, water_map in enumerate(split):
    if water_map == 'water-to-light map':
        light_maps, tempareture_maps, humidity_maps, location_maps = get_light_map(split[i+1:])
        return water_maps, light_maps, tempareture_maps, humidity_maps, location_maps
    water_map = water_map.split()
    dest_start = int(water_map[0])
    src_start = int(water_map[1])
    range_len = int(water_map[2])
    water_maps.append((dest_start, src_start, range_len))

  return water_maps, light_maps, tempareture_maps, humidity_maps, location_maps
  
def get_light_map(split):
  light_maps, tempareture_maps, humidity_maps, location_maps = [], [], [], []
  for i, light_map in enumerate(split):
    if light_map == 'light-to-temperature map':
        tempareture_maps, humidity_maps, location_maps = get_temperature_map(split[i+1:])
        return light_maps, tempareture_maps, humidity_maps, location_maps
    light_map = light_map.split()
    dest_start = int(light_map[0])
    src_start = int(light_map[1])
    range_len = int(light_map[2])
    light_maps.append((dest_start, src_start, range_len))

  return light_maps, tempareture_maps, humidity_maps, location_maps
  
def get_temperature_map(split):
  tempareture_maps, humidity_maps, location_maps = [], [], []
  for i, tempareture_map in enumerate(split):
    if tempareture_map == 'temperature-to-humidity map':
        humidity_maps, location_maps = get_humidity_map(split[i+1:])
        return tempareture_maps, humidity_maps, location_maps
    tempareture_map = tempareture_map.split()
    dest_start = int(tempareture_map[0])
    src_start = int(tempareture_map[1])
    range_len = int(tempareture_map[2])
    tempareture_maps.append((dest_start, src_start, range_len))

  return tempareture_maps, humidity_maps, location_maps
  
def get_humidity_map(split):
  humidity_maps, location_maps = [], []
  for i, humidity_map in enumerate(split):
    if humidity_map == 'humidity-to-location map':
        location_maps = get_location_map(split[i+1:])
        return humidity_maps, location_maps
    humidity_map = humidity_map.split()
    dest_start = int(humidity_map[0])
    src_start = int(humidity_map[1])
    range_len = int(humidity_map[2])
    humidity_maps.append((dest_start, src_start, range_len))

  return humidity_maps, location_maps
  
def get_location_map(split):
  location_maps = []
  for location_map in split:
    location_map = location_map.split()
    dest_start = int(location_map[0])
    src_start = int(location_map[1])
    range_len = int(location_map[2])
    location_maps.append((dest_start, src_start, range_len))

  return location_maps
   

with open('input.txt') as f:
  content = f.read()
  split = re.split(": |:\n|\n\n|\n", content)

  seeds = []
  for seed in split[1].split():
      seeds.append(int(seed))

  soil_maps, fertilizer_maps, water_maps, light_maps, tempareture_maps, humidity_maps, location_maps = get_soil_map(split[3:])
  
  print(fertilizer_maps)
  
  soils = []
  for seed in seeds:
    mapped = False
    for (dest_start, src_start, range_len) in soil_maps:
      if seed >= src_start and seed < src_start + range_len:
        soils.append(dest_start + (seed - src_start) )
        mapped = True
        break
    if not mapped:
      soils.append(seed)
  print(soils)
    
  fertilizers = []
  for soil in soils:
    mapped = False
    for (dest_start, src_start, range_len) in fertilizer_maps:
      if soil >= src_start and soil < src_start + range_len:
        fertilizers.append(dest_start + (soil - src_start) )
        mapped = True
        break
    if not mapped:
      fertilizers.append(soil)
  print(fertilizers)

  waters = []
  for fertilizer in fertilizers:
    mapped = False
    for (dest_start, src_start, range_len) in water_maps:
      if fertilizer >= src_start and fertilizer < src_start + range_len:
        waters.append(dest_start + (fertilizer - src_start) )
        mapped = True
        break
    if not mapped:
      waters.append(fertilizer)
  print(waters)
  
  lights = []
  for water in waters:
    mapped = False
    for (dest_start, src_start, range_len) in light_maps:
      if water >= src_start and water < src_start + range_len:
        lights.append(dest_start + (water - src_start) )
        mapped = True
        break
    if not mapped:
      lights.append(water)
      
  print(lights)
  
  temperatures = []
  for light in lights:
    mapped = False
    for (dest_start, src_start, range_len) in tempareture_maps:
      if light >= src_start and light < src_start + range_len:
        temperatures.append(dest_start + (light - src_start) )
        mapped = True
        break
    if not mapped:
      temperatures.append(light)
      
  print(temperatures)
  
  humidities = []
  for temperature in temperatures:
    mapped = False
    for (dest_start, src_start, range_len) in humidity_maps:
      if temperature >= src_start and temperature < src_start + range_len:
        humidities.append(dest_start + (temperature - src_start) )
        mapped = True
        break
    if not mapped:
      humidities.append(temperature)
      
  print(humidities)
  
  locations = []
  for humidity in humidities:
    mapped = False
    for (dest_start, src_start, range_len) in location_maps:
      if humidity >= src_start and humidity < src_start + range_len:
        locations.append(dest_start + (humidity - src_start) )
        mapped = True
        break
    if not mapped:
      locations.append(humidity)
      
  print(locations)
  
  print(min(locations))
  