import time
from enum import Enum

# Automata => State
class trafficLigt(Enum):
    MERAH = "Merah"
    HIJAU = "Hijau"
    KUNING = "Kuning"

# Automata => state atau perubahan Atau transisi

# Map<key, Value>
# key => state Awal
# Value => state Tujuan

state_trantition = {
    trafficLigt.MERAH: trafficLigt.HIJAU,
    trafficLigt.HIJAU: trafficLigt.KUNING,
    trafficLigt.KUNING: trafficLigt.MERAH
}
state_duration = {
    trafficLigt.MERAH: 6,
    trafficLigt.HIJAU: 4,
    trafficLigt.KUNING: 1
}
curren_State = trafficLigt.MERAH
# next_state = state_trantition[curren_State] # Hijau, kuning atau Merah
# print(next_state)

while True:
    print(f"Traffic Light ::{curren_State.value}")
    time.sleep(state_duration[curren_State])
    curren_State = state_trantition[curren_State]
