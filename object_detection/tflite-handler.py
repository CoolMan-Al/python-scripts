#!/usr/bin/env python3

from datetime import datetime
from ai_edge_litert.interpreter import Interpreter
import cv2
import numpy as np


def detect_objects(frame):
    # Convert frame for model to read
    frame_size  = cv2.resize(frame, (width, height))
    frame_exp = np.expand_dims(frame_size, axis=0)

    # Model run 
    interpreter.set_tensor(input_details[0]['index'], frame_exp)
    interpreter.invoke()

    # Pull results and draw onto frame
    detected_boxes = interpreter.get_tensor(output_details[0]['index'])
    detected_classes = interpreter.get_tensor(output_details[1]['index'])
    detected_scores = interpreter.get_tensor(output_details[2]['index'])
    num_boxes = interpreter.get_tensor(output_details[3]['index'])
    
    # Go through every box
    for i in range(int(num_boxes[0])):
        classId = int(detected_classes[0][i])
        # 0 is person
        if(classId == 0):
            # Get confidence of each box and draw if 50% or higher confidence
            top, left, bottom, right = detected_boxes[0][i]
            score = detected_scores[0][i]
            if(score > 0.5):
                # Pull coordinates of bounding box
                ymin = int(top * res[1])
                xmin = int(left * res[0])
                ymax = int(bottom * res[1])
                xmax = int(right * res[0])

                # Draw rectangle onto numpy frame 
                cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0,255,0), 2)
    
    # Return drawn frame and number of detections
    return frame

# Program Entry Point
if(__name__ == '__main__'):
    # Image read
    img = cv2.imread("input.png")

    # BGR > RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Object detection model load
    interpreter = Interpreter(
        model_path="./mobilenet_v2.tflite",
        num_threads=4
    )
    interpreter.allocate_tensors()

    # Model detail pull
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    height = input_details[0]['shape'][1]
    width = input_details[0]['shape'][2]

    # Object detection function
    img = detect_objects(img)

    # Write out detected image
    cv2.imwrite("output.png", img)
    

