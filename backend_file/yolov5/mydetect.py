import argparse
import time
from pathlib import Path
import random

import cv2
import torch
import torch.backends.cudnn as cudnn

from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages, MyLoadImages
from utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path, save_one_box
from utils.plots import colors, plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized


class simulation_opt:  # 参数对象。
    def __init__(self, weights, img_size=640, conf_thres=0.25, iou_thres=0.45, device='', view_img=False,
                 classes=None, agnostic_nms=False, augment=False, update=False, exist_ok=False):
        self.weights = weights
        self.source = None
        self.img_size = img_size
        self.conf_thres = conf_thres
        self.iou_thres = iou_thres
        self.device = device
        self.view_img = view_img
        self.classes = classes
        self.agnostic_nms = agnostic_nms
        self.augment = augment
        self.update = update
        self.exist_ok = exist_ok


# 增加一个新类，这个新类是在原来detect函数上进行删减。可以先复制原来的detect函数代码，再着手修改
class detectapi:
    def __init__(self, weights, img_size=640):
        # 构造函数中先做好必要的准备，如初始化参数，加载模型
        ''' 删掉
        source, weights, view_img, save_txt, imgsz = opt.source, opt.weights, opt.view_img, opt.save_txt, opt.img_size
        webcam = source.isnumeric() or source.endswith('.txt') or source.lower().startswith(
        ('rtsp://', 'rtmp://', 'http://'))
        '''  # 改为
        self.opt = simulation_opt(weights=weights, img_size=img_size)
        weights, imgsz = self.opt.weights, self.opt.img_size

        ''' 删掉
        # Directories
        #save_dir = Path(increment_path(Path(opt.project) / opt.name, exist_ok=opt.exist_ok))  # increment run
        #(save_dir / 'labels' if save_txt else save_dir).mkdir(parents=True, exist_ok=True)  # make dir
        '''
        # Initialize
        set_logging()
        self.device = select_device(self.opt.device)
        self.half = self.device.type != 'cpu'  # half precision only supported on CUDA

        # Load model
        self.model = attempt_load(weights, map_location=self.device)  # load FP32 model
        self.stride = int(self.model.stride.max())  # model stride
        self.imgsz = check_img_size(imgsz, s=self.stride)  # check img_size
        if self.half:
            self.model.half()  # to FP16

        # Second-stage classifier
        self.classify = False
        if self.classify:
            self.modelc = load_classifier(name='resnet101', n=2)  # initialize
            self.modelc.load_state_dict(torch.load('weights/resnet101.pt', map_location=self.device)['model']).to(
                self.device).eval()
        '''
        self.names,和self.colors是由后面的代码拉到这里来的。names是类别名称字典，colors是画框时用到的颜色。
        '''
        # read names and colors
        self.names = self.model.module.names if hasattr(self.model, 'module') else self.model.names
        self.colors = [[random.randint(0, 255) for _ in range(3)] for _ in self.names]

    def detect(self, source):  # 使用时，调用这个函数
        if type(source) != list:
            raise TypeError('source must be a list which contain  pictures read by cv2')

        '''删掉
        if webcam:
        view_img = check_imshow()
        cudnn.benchmark = True  # set True to speed up constant image size inference
        dataset = LoadStreams(source, img_size=imgsz, stride=stride)
        else:
        save_img = True
        dataset = LoadImages(source, img_size=imgsz, stride=stride)


        '''  # 改为
        # Set Dataloader
        dataset = MyLoadImages(source, img_size=self.imgsz, stride=self.stride)
        # 原来是通过路径加载数据集的，现在source里面就是加载好的图片，所以数据集对象的实现要
        # 重写。修改代码后附。在utils.dataset.py上修改。

        '''移动到构造方法末尾。names是类别名称字典，colors是画框时用到的颜色。
        names = model.module.names if hasattr(model, 'module') else model.names
        colors = [[random.randint(0, 255) for _ in range(3)] for _ in names]
        '''
        # Run inference
        if self.device.type != 'cpu':
            self.model(torch.zeros(1, 3, self.imgsz, self.imgsz).to(self.device).type_as(
                next(self.model.parameters())))  # run once
        result = []
        ''' 删掉
        for path, img, im0s, vid_cap in dataset: 因为不用保存，所以path可以不要，因为不处理视频，所以vid_cap不要。
        '''  # 改为
        for img, im0s in dataset:
            img = torch.from_numpy(img).to(self.device)
            img = img.half() if self.half else img.float()  # uint8 to fp16/32
            img /= 255.0  # 0 - 255 to 0.0 - 1.0
            if img.ndimension() == 3:
                img = img.unsqueeze(0)

            # Inference
            # t1 = time_synchronized() #计算预测用时的，可以不要
            pred = self.model(img, augment=self.opt.augment)[0]

            # Apply NMS
            pred = non_max_suppression(pred, self.opt.conf_thres, self.opt.iou_thres, classes=self.opt.classes,
                                       agnostic=self.opt.agnostic_nms)
            # t2 = time_synchronized() #计算预测用时的，可以不要

            # Apply Classifier
            if self.classify:
                pred = apply_classifier(pred, self.modelc, img, im0s)

            '''删掉
             for i, det in enumerate(pred):  # detections per image
            if webcam:  # batch_size >= 1
                p, s, im0, frame = path[i], '%g: ' % i, im0s[i].copy(), dataset.count
            else:
                p, s, im0, frame = path, '', im0s, getattr(dataset, 'frame', 0)

            p = Path(p)  # to Path
            save_path = str(save_dir / p.name)  # img.jpg
            txt_path = str(save_dir / 'labels' / p.stem) + ('' if dataset.mode == 'image' else f'_{frame}')  # img.txt
            s += '%gx%g ' % img.shape[2:]  # print string
            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
            if len(det):
                # Rescale boxes from img_size to im0 size
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                # Print results
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()  # detections per class
                    s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

                # Write results
                for *xyxy, conf, cls in reversed(det):
                    if save_txt:  # Write to file
                        xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
                        line = (cls, *xywh, conf) if opt.save_conf else (cls, *xywh)  # label format
                        with open(txt_path + '.txt', 'a') as f:
                            f.write(('%g ' * len(line)).rstrip() % line + '\n')

                    if save_img or view_img:  # Add bbox to image
                        label = f'{names[int(cls)]} {conf:.2f}'
                        plot_one_box(xyxy, im0, label=label, color=colors[int(cls)], line_thickness=3)
            '''  # 改为
            # Process detections
            det = pred[0]  # 原来的情况是要保持图片，因此多了很多关于保持路径上的处理。另外，pred
            # 其实是个列表。元素个数为batch_size。由于对于我这个api，每次只处理一个图片，
            # 所以pred中只有一个元素，直接取出来就行，不用for循环。
            im0 = im0s.copy()  # 这是原图片，与被传进来的图片是同地址的，需要copy一个副本，否则，原来的图片会受到影响
            # s += '%gx%g ' % img.shape[2:]  # print string
            # gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
            result_txt = []
            # 对于一张图片，可能有多个可被检测的目标。所以结果标签也可能有多个。
            # 每被检测出一个物体，result_txt的长度就加一。result_txt中的每个元素是个列表，记录着
            # 被检测物的类别引索，在图片上的位置，以及置信度
            if len(det):
                # Rescale boxes from img_size to im0 size
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                # Print results
                '''
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()  # detections per class
                    s += f"{n} {self.names[int(c)]}{'s' * (n > 1)}, "  # add to string
                '''
                # Write results

                for *xyxy, conf, cls in reversed(det):
                    line = (int(cls.item()), [int(_.item()) for _ in xyxy], conf.item())  # label format
                    result_txt.append(line)
                    label = f'{self.names[int(cls)]} {conf:.2f}'
                    plot_one_box(xyxy, im0, label=label, color=self.colors[int(cls)], line_thickness=3)
            result.append((im0, result_txt))  # 对于每张图片，返回画完框的图片，以及该图片的标签列表。
        return result, self.names
