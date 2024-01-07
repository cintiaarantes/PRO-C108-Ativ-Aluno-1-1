import cv2
import mediapipe as mp

# Passo 1: Captar de quadros do vídeo da webcan 
cap = cv2.VideoCapture(0)

# Passo 2: Módulos da biblioteca MediaPipe 
mp_hands = mp.solutions.hands  #Detecta 1º a palma da mão e, depois, os 21 pontos de referência na palma da mão.
mp_drawing = mp.solutions.drawing_utils  #Desenha as linhas de conexão entre os 21 pontos de referência.

# Passo 3: Método Hands - usa 2 parâmetros: min_detection_confidence(confiança mínima de detecção) e min_tracking_confidence (confiança mínima de rastreamento)
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)

tipIds = [4, 8, 12, 16, 20]

# Defina uma função para contar os dedos
def countFingers(image, hand_landmarks, handNo=0):
    print()
           
    ####################################################

        # ADICIONE O CÓDIGO AQUI

    ####################################################

# Passo 6: Definir uma função para desenhar as conexões nos pontos de referência da mão, para mostrar a detecção da mão.
def drawHandLanmarks(image, hand_landmarks): #drawHandLanmarks - desenhar pontos de ref. da mão (imagem, pontos de ref.)

    # Desenhar as conexões entre os pontos de referência
    if hand_landmarks: #Verificação SE estamos obtendo o valor de hand_landmarks, só será retornado se as mãos estiverem visiveis

      for landmarks in hand_landmarks: #Faremos um loop por esses pontos para desenhar conexões
               
        mp_drawing.draw_landmarks(image, landmarks, mp_hands.HAND_CONNECTIONS) #usando o método mp_drawing.draw_landmark(imagem, lista valores ref., props HAND_CONNECTIONS da solução de mãos do MediaPipe.)


while True:
    success, image = cap.read()

    # Passo 5: Este método converte a imagem invertida da mão - Sintáxe tem parâmetros: imagem que estamos trabalhando; a direção para a qual queremos inverter a imagem (0: vertical; 1:horizontal)
    image = cv2.flip(image, 1)
    
    # Passo 4: Detecte os pontos de referência das mãos - Detecta as mãos
    results = hands.process(image)

    # Passo 6.1: Obtenha a posição do ponto de referência do resultado processado. Props: multi_hand_landmarks retorna as posições x, y e z (dist webcam) dos pontos de referência.
    hand_landmarks = results.multi_hand_landmarks

    # Passo 6.2: Chamada da função para desenhar os pontos de referência
    drawHandLanmarks(image, hand_landmarks)

    # Obtenha a posição dos dedos da mão        
    #########################
    # ADICIONE O CÓDIGO AQUI
    #########################

    cv2.imshow("Controlador de Midia", image)

    # Saia da tela ao pressionar a barra de espaços
    key = cv2.waitKey(1)
    if key == 32:
        break

cv2.destroyAllWindows()
