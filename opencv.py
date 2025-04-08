import warnings
import cv2
import requests
import os
from ultralytics import YOLO
import numpy as np

# 忽略 FutureWarning
warnings.filterwarnings("ignore", category=FutureWarning)

def getHotDogCount(image_url: str, output_dir: str = "debug_output"):
    try:
        # 创建调试输出目录
        os.makedirs(output_dir, exist_ok=True)

        # 下载图片
        response = requests.get(image_url)
        response.raise_for_status()
        # Convert response content to numpy array
        image_array = np.frombuffer(response.content, np.uint8)

        # 加载YOLOv8模型（使用 yolov8x 模型）
        model = YOLO('yolov8x.pt')

        # Load image using OpenCV
        img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

        # 使用YOLOv8进行检测
        results = model(img)

        # 存储检测到的所有类别名称
        detected_classes = set()
        # 过滤出热狗的检测结果
        detected_hotdogs = []
        for result in results:
            boxes = result.boxes
            for box in boxes:
                class_id = int(box.cls[0])
                class_name = result.names[class_id]
                confidence = float(box.conf[0])
                detected_classes.add(class_name)
                if class_name == 'hot dog':
                    x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    detected_hotdogs.append((x1, y1, x2, y2))
                    # 准备标签
                    label = f"{class_name}: {confidence:.2f}"
                    # 创建一个空白图像用于绘制文本
                    text_img = np.zeros((200, 200, 3), dtype=np.uint8)
                    cv2.putText(text_img, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                    # 计算旋转矩阵
                    height, width = text_img.shape[:2]
                    center = (width // 2, height // 2)
                    rotation_matrix = cv2.getRotationMatrix2D(center, -90, 1.0)
                    # 进行旋转
                    rotated_text_img = cv2.warpAffine(text_img, rotation_matrix, (height, width))
                    # 找到旋转后文本的非零区域
                    non_zero = cv2.findNonZero(cv2.cvtColor(rotated_text_img, cv2.COLOR_BGR2GRAY))
                    x, y, w, h = cv2.boundingRect(non_zero)
                    cropped_rotated_text = rotated_text_img[y:y + h, x:x + w]
                    # 将旋转后的文本粘贴到检测框内
                    img[y1:y1 + h, x1:x1 + w] = cropped_rotated_text

        # 输出检测到的所有类别名称
        print(f"检测到的类别有: {', '.join(sorted(detected_classes))}")

        # 保存检测结果图片
        cv2.imwrite(f"{output_dir}/detected_hotdogs.jpg", img)

        print(f"检测结果: {len(detected_hotdogs)} 个热狗")
        return len(detected_hotdogs)

    except Exception as e:
        print(f"Error: {e}")
        return 0
