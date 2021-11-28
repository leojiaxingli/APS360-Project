from urllib import request
from utils.singleton import Singleton
from module.solver.model.neural_network import DigitNet
import cv2
import numpy as np
from config import model_state
import torch


class SolverService(Singleton):
    def data_url_to_cv2_img(self, data_url):
        resp = request.urlopen(data_url)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        return image

    def segment(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 27))
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        ctrs, hier = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
        segments = []
        for i, ctr in enumerate(sorted_ctrs):
            x, y, w, h = cv2.boundingRect(ctr)
            roi = img[y:y + h, x:x + w]

            roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            roi_ret, roi_thresh = cv2.threshold(roi_gray, 127, 255, cv2.THRESH_BINARY_INV)
            segments.append(roi_thresh)
            # cv2.rectangle(img, (x, y), (x + w, y + h), (90, 0, 255), 2)
        return segments

    def padding(self, img, padding,  width, height):
        result = np.full((padding, padding), fill_value=0, dtype=np.uint8)
        x_center = (padding - width) // 2
        y_center = (padding - height) // 2
        result[y_center:y_center + height, x_center:x_center + width] = img
        return result

    def pre_process(self, img):
        old_image_height, old_image_width = img.shape
        padding = max(old_image_width, old_image_height)
        img = self.padding(img, padding, old_image_width, old_image_height)
        img = cv2.resize(img, (28, 28), interpolation=cv2.INTER_AREA)
        img = self.padding(img, 31, 28, 28)
        resized = cv2.resize(img, (28, 28), interpolation=cv2.INTER_AREA)

        # cv2.imshow('', resized)
        # cv2.waitKey(0)

        img_torch = torch.from_numpy(np.array([resized]).astype(np.float32))
        img_torch = img_torch.unsqueeze(0)
        return img_torch

    def recognize(self, img):
        img_torch = self.pre_process(img)
        net = DigitNet()
        net.load_state_dict(model_state)
        out = net(img_torch)
        pred = out.max(1, keepdim=True)[1]
        return pred.item()
