while True:
    ret, frame = cap.read()
    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    for top, right, bottom, left in face_locations:

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    cv2.imshow('video', frame)

    if cv2.waitKey(25) == 13:
        break