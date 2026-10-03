import urllib.request


class Lumikit:

    def __init__(self, ip="127.0.0.1", porta=5000):
        self.ip = ip
        self.porta = porta
        self.base_url = f"http://{self.ip}:{self.porta}"

    def _enviar(self, servico):
        url = f"{self.base_url}/services/{servico}"

        try:
            with urllib.request.urlopen(url, timeout=3) as resposta:
                return resposta.read().decode()

        except Exception as erro:
            print(f"Erro ao comunicar com o Lumikit: {erro}")
            return None

    def blackout_on(self):
        resultado = self._enviar("main_set_blackout_on")
        print("🔴 BLACKOUT ON")
        print(resultado)

    def blackout_off(self):
        resultado = self._enviar("main_set_blackout_off")
        print("🟢 BLACKOUT OFF")
        print(resultado)

    def estado_blackout(self):
        resultado = self._enviar("main_is_blackout_on")
        print("📡 Estado do blackout:")
        print(resultado)
        return resultado