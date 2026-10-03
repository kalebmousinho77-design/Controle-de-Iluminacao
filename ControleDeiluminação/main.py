from obs import OBS
from lumikit import Lumikit


obs = OBS(
    "127.0.0.1",
    4455,
    "zLFhrTSCTtaoCdkJ"
)

lumikit = Lumikit()


cena_background = obs.obter_cena_program()


def aviso_iniciou(evento):
    print("🎬▶️ AVISO INICIADO")

    obs.fazer_transition()
    lumikit.blackout_on()


def aviso_finalizou(evento):
    print("🏁🎬 AVISO FINALIZADO")

    obs.colocar_preview(cena_background)
    obs.fazer_transition()

    lumikit.blackout_off()


obs.evento_inicio(aviso_iniciou)
obs.evento_fim(aviso_finalizou)


print("🚀 SISTEMA INICIADO")
print("Aguardando avisos...")


while True:
    pass