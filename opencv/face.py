import cv2
from deepface import DeepFace

# Функция для распознавания лиц и определения возраста, эмоций и пола
def analyze_face(frame):
    try:
        # Анализируем лицо на кадре
        analysis = DeepFace.analyze(frame, actions=['age', 'gender', 'emotion'], enforce_detection=False)
        age = analysis[0]['age']
        gender = analysis[0]['gender']
        emotion = analysis[0]['dominant_emotion']
        return age, gender, emotion
    except Exception as e:
        print(f"Error: {e}")
        return None, None, None

# Открываем веб-камеру
cap = cv2.VideoCapture(0)

while True:
    # Читаем кадр из веб-камеры
    ret, frame = cap.read()
    if not ret:
        break

    # Анализируем лицо на кадре
    age, gender, emotion = analyze_face(frame)

    if age is not None and gender is not None and emotion is not None:
        # Отображаем возраст, пол и эмоцию на кадре
        cv2.putText(frame, f'Age: {age}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, f'Gender: {gender}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, f'Emotion: {emotion}', (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Отображаем кадр
    cv2.imshow('Face Analysis', frame)

    # Выход по нажатию клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождаем ресурсы
cap.release()
cv2.destroyAllWindows()
