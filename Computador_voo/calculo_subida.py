def calcular_subida():
    while True:
        try:
            elevacao = int(input('Elevação do aeródromo, em pés: '))
            fl = int(input('Nível de cruzeiro, em FL: '))
            if fl < 0:
                print()
                raise ValueError
            temperatura = float(input('Temperatura, em graus Celsius: '))
            razao_subida = int(input('Informe a razão de subida (ft/min): '))
            if razao_subida <= 0:
                print()
                print('A razão de subida não pode ser negativa ou nula. Sua mula. -- olha, até rimou!')
                raise ValueError
            velocidade = float(input('Entre com a velocidade indicada, em nós: '))
            if velocidade <= 0:
                print()
                print('A velocidade não pode ser nula ou negativa. Tem certeza que você quer voar?')
                raise ValueError
            # direcao_vento = float(input('Entre com a direção do vento, em graus: '))
            # if direcao_vento < 0 or direcao_vento > 360:
            #     print()
            #     print('O valor informado é em graus. Pegue uma bússola. Entre 0 e 360. Você consegue.')
            #     raise ValueError
            # velocidade_vento = float(input('Entre com a velocidade do vento de subida, em nós: '))
            # if velocidade_vento <0:
            #     print()
            #     print('Tá de sacanagem, né? Vento com valor negativo, igual seu Q.I.')
                raise ValueError

            fl = fl * 100
            delta_altura = fl - elevacao                # Variacao de altura
            fator = (fl + elevacao) * 0.00001           
            tempo = delta_altura / razao_subida         # Tempo
            delta_temp = (delta_altura * 2) / 1000      # Variação de temperatura
            temp_fl = temperatura - delta_temp          # Temperatura do FL
            ams = (fl + elevacao) / 2                   # Altitude média de subida
            tms = (temp_fl + temperatura) / 2           # Temperatura média de subida
            vams = velocidade * (1 + fator)             # Velocidade média aerodinâmica de subida

            print()
            print('Variação de altura: {} pés'.format(delta_altura))
            print('Tempo: {:.1f} minutos'.format(tempo))
            print('Variação de temperatura: {} °C'.format(delta_temp))
            print('Temperatura no FL: {:.1f} °C'.format(temp_fl))
            print('Altitude média de subida: {} pés'.format(ams))
            print('Temperatura média de subida: {:.1f} °C'.format(tms))
            print('Velocidade média aerodinâmica de subida: {:.1f} nós'.format(vams))

        except ValueError:
            print('Valor informado é inválido...')

        print()
        replay = input('Pressione qualquer tecla para calcular novamente, N para sair: ')
        print()
        if replay == 'N' or replay == 'n':
            break