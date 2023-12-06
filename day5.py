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
    print(soil_maps)

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

    soils, fertilizers, waters, lights, temperatures, humidities, locations = defaultdict(list), defaultdict(list), defaultdict(list), defaultdict(list), defaultdict(list), defaultdict(list), defaultdict(list)
    for seed in tqdm(seeds):
        for (dest_start, src_start, range_len) in tqdm(soil_maps):
          for j, i in enumerate(range(src_start, src_start + range_len)):
              if seed == i and dest_start + j:
                soils[seed].append(dest_start + j)
                break
        if not seed in soils:
          soils[seed].append(seed)

        for (dest_start, src_start, range_len) in tqdm(fertilizer_maps):
          for j, i in enumerate(range(src_start, src_start + range_len)):
              if soils[seed][-1] == i:
                fertilizers[seed].append(dest_start + j)
                break
          if not seed in fertilizers:
            fertilizers[seed].append(soils[seed][-1])

        for (dest_start, src_start, range_len) in tqdm(water_maps):
          for j, i in enumerate(range(src_start, src_start + range_len)):
              if fertilizers[seed][-1] == i:
                waters[seed].append(dest_start + j)
                break
          if not seed in waters:
            waters[seed].append(fertilizers[seed][-1])
        
        for (dest_start, src_start, range_len) in tqdm(light_maps):
          for j, i in enumerate(range(src_start, src_start + range_len)):
              if waters[seed][-1] == i:
                lights[seed].append(dest_start + j)
                break
          if not seed in lights:
            lights[seed].append(waters[seed][-1])
        
        for (dest_start, src_start, range_len) in tqdm(tempareture_maps):
          for j, i in enumerate(range(src_start, src_start + range_len)):
              if lights[seed][-1] == i:
                temperatures[seed].append(dest_start + j)
                break
          if not seed in temperatures:
            temperatures[seed].append(lights[seed][-1])
        
        for (dest_start, src_start, range_len) in tqdm(humidity_maps):
          for j, i in enumerate(range(src_start, src_start + range_len)):
              if temperatures[seed][-1] == i:
                humidities[seed].append(dest_start + j)
                break
          if not seed in humidities:
            humidities[seed].append(temperatures[seed][-1])
        
        for (dest_start, src_start, range_len) in tqdm(location_maps):
          for j, i in enumerate(range(src_start, src_start + range_len)):
              if humidities[seed][-1] == i:
                locations[seed].append(dest_start + j)
                break
          if not seed in locations:
            locations[seed].append(humidities[seed][-1])
        
    print(min(locations.values()))
        
            
          