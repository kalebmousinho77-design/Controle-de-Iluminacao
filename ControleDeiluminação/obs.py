import obsws_python as obs


class OBS:

    def __init__(self, host, port, password):

        self.callback_inicio = None
        self.callback_fim = None

        # Conexão para receber eventos
        self.event_client = obs.EventClient(
            host=host,
            port=port,
            password=password
        )

        # Conexão para enviar comandos
        self.req_client = obs.ReqClient(
            host=host,
            port=port,
            password=password
        )

        self.event_client.callback.register([
            self.on_media_input_playback_started,
            self.on_media_input_playback_ended
        ])

    def conectar(self):
        print("OBS CONECTADO!")

    def evento_inicio(self, callback):
        self.callback_inicio = callback

    def evento_fim(self, callback):
        self.callback_fim = callback

    def on_media_input_playback_started(self, evento):

        if self.callback_inicio:
            self.callback_inicio(evento)

    def on_media_input_playback_ended(self, evento):

        if self.callback_fim:
            self.callback_fim(evento)

    def obter_cena_program(self):
        resposta = self.req_client.get_current_program_scene()
        return resposta.current_program_scene_name

    def colocar_preview(self, nome_cena):
        self.req_client.set_current_preview_scene(nome_cena)

    def fazer_transition(self):
        self.req_client.trigger_studio_mode_transition()