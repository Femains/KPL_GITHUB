from enum import Enum

class studentStatusState(Enum):
    TERDAFTAR = "Terdaftar"
    CUTI = "Cuti"
    AKTIF = "Aktif"
    LULUS = "Lulus"

# Trigger input
class triggerInputState(Enum):
    CETAK_KSM = "Cetak KSM"
    MENYELESAIKAN_CUTI = "Menyelesaikan Cuti"
    LULUS = "Lulus"
    MENGAJUKAN_CUTI = "Mengajukan Cuti"

state_trantition = {
    studentStatusState.TERDAFTAR:{
        triggerInputState.CETAK_KSM: studentStatusState.AKTIF,
        triggerInputState.MENGAJUKAN_CUTI: studentStatusState.CUTI
    },

    studentStatusState.CUTI:{
        triggerInputState.MENYELESAIKAN_CUTI : studentStatusState.TERDAFTAR
    },

    studentStatusState.AKTIF:{
        triggerInputState.LULUS: studentStatusState.LULUS,
        triggerInputState.MENGAJUKAN_CUTI:studentStatusState.CUTI
    }
}

def change_state(current_state, trigger_input):
    cond_1 = current_state in state_trantition # return True or False 
    cond_2 = trigger_input in state_trantition[current_state] # return True or False 
    if cond_1 and cond_2:
        # TERDAFTAR, AKTIF, LULUS ATAU CUTI
        return state_trantition[current_state][trigger_input]
    return "TRANSISI TIDAK VALID"

current_state = studentStatusState.TERDAFTAR
trigger_input = triggerInputState.MENGAJUKAN_CUTI

next_state = change_state(current_state, trigger_input)
print(next_state)

