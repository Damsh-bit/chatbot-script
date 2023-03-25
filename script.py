import requests
import pyautogui
import webbrowser
from time import sleep

# Reemplaza <YOUR_API_KEY> con tu propia clave de API
api_key = 'RGAPI-d5501d79-572b-474a-94c8-6e710966b4df'
region = 'la2'  # Cambia a tu región de juego si es diferente

while True:

    def check_current_game(summoner_id):
        url = f'https://{region}.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{summoner_id}?api_key={api_key}'
        response = requests.get(url)

        if response.status_code == 200:
            game_data = response.json()
            #webbrowser.open(
            #    'https://web.whatsapp.com/send?phone=549116880-7712', new=1)
            pyautogui.hotkey('ctrl', '3')
            sleep(2)
            # Obtener las coordenadas de la posición del chat que deseas seleccionar
            pos = pyautogui.locateOnScreen('./chat.png')
            if pos is not None:
            # Mover el mouse a la posición del chat y hacer clic en él
                pyautogui.moveTo(pos.left + 10, pos.top + 10)
                pyautogui.click()
            else:
                print("La imagen no fue encontrada en la pantalla")
            sleep(2)
            # Mover el mouse a la posición del chat y hacer clic en él
            sleep(5)
            pyautogui.typewrite(
                f'Empezo la partida: {game_data["gameMode"]}')
            pyautogui.press('enter')
            sleep(5)
            print('Acaba de empezar a jugar la siguiente partida:')
            print(f'Tipo de juego: {game_data["gameMode"]}')


# Pide tu ID de invocador
    summoner_name = "adc11"
    url = f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        summoner_data = response.json()
        summoner_id = summoner_data['id']
        check_current_game(summoner_id)
    else:
        print('No se pudo obtener información del invocador.')

    sleep(30)
