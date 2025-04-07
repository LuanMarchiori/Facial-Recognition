import cv2 ## OpenCV 
import mediapipe as mp ## MediaPipe

webcam = cv2.VideoCapture(0)
solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecimento_rosto = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils

while True:
    ## LER INFORMAÇÕES DA CAMERA
    conectado, frame = webcam.read()
    if not conectado:
        break
    
    # RECONHECER O ROSTO
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultados = reconhecimento_rosto.process(frame_rgb)
    if resultados.detections:
        for rosto in resultados.detections:
            
            # DESENHAR O ROSTO
            desenho.draw_detection(frame, rosto)
            
    cv2.imshow("Reconhecimento de rosto", frame)
    
    if cv2.waitKey(5) == ord("q"):
        break

webcam.release()
cv2.destroyAllWindows()
