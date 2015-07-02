# coding: utf-8
import json
import requests
from pync import Notifier

def main():
    time = json.loads(requests.get('http://api.cartola.globo.com/time_adv/revil-fc.json').content)['time']
    mercado = json.loads(requests.get('http://api.cartola.globo.com/mercado/status.json').content)

    status = {1: 'Aberto', 2: 'Fechado', '3': 'Em Atualização', 4: 'Liberado para Testes', 5: 'Fim de Jogo'}

    if mercado['mercado']['status'] in [2, 3]:
        msg = "Parcial do seu time: %s" % time['pontuacao']
    else:
        msg = "%s fez %s na rodada e seu patriônio é de %s" % (time['pontuacao'], time['patrimonio'])

    Notifier.notify(msg,
                    title='Cartola FC - Mercado %s' % status[mercado['mercado']['status']],
                    sound='default',
                    contentImage='http://s.glbimg.com/es/ca/escudos/times/f3/ec/escudo_32x32_time_1557408.png',
                    open='http://cartolafc.globo.com',
                    appIcon='http://s.glbimg.com/es/ge/static/live/cartolafc/img/apple-touch-cartola.png')

if __name__ == "__main__":
    main()