from collections import namedtuple

Box = namedtuple("Box", "id name height width length")
Container = namedtuple("Container", "id occupied_volume")
Freight = namedtuple("Freight", "id container_id box_id")
