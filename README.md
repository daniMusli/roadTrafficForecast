# Road Traffic Forecast
Road traffic flow detection on video data collected from two sources 
- Videos captured from tablets mounted on ODOT trucks.
- Videos obtained from the Caltrans Measurement System (CMS) in the state of California [2GB Samples](http://www.poss.pku.edu.cn/OpenDataResource/TITS2016WangOnRoadVehicle.zip).
## Introduction 
The purpose of this project is to develop a system that can extract traffic information from live video streams, for example Road Condition Monotiring Systems all over the US. This project consists of two parts mainly. The first part is extract traffic data from
videos. The second part is to train forecasting models using LSTM and GRU Neural Networks.  
## project Walkthrough 
- install the project dependencies inside `requirements.txt` to your working environment.
- place the videos you want to work on in the `Video_Data_Samples`
- run `VehicleCounterYOLO.ipynb` if you do not care about real time data extraction the code is based on YOLO V3 published by Redmon and Farhadi(2018) [paper](https://arxiv.org/abs/1804.02767) . The counting API takes around 0.9 second on `NVIDIA GeForce GTX 1050` to process one video frame. very slow to be aplied on real time sources but much more accurate. (tested with around 96% accuracy). SSD object detector was also tested but it signifacantly struggled with smaller objects (tested with around 92% accuracy). for the SSD the time it required to run to forward a frame was around 0.1 second which a significant improvment compared with YOLO but still very slow for real time object detection specially for low processing power components that are typically used for Road Monitoring systems, for example [Beagle Board](https://beagleboard.org/black), [Raspberry Pi](https://www.raspberrypi.org/). Before running the code download the yolo-coco model weights from this [Link](https://drive.google.com/open?id=1FbtFXOgiGqWpDf1WOCPcw0W1VG8JTC3q) and put it inside `yolo-coco` directory.
- run `VehicleCounterOpenCV.ipynb` for real time data extraction. accuracy around 85% , frame processing time is less than 0.03 seconds. 
<p float="left">
  <img src="/images/cv1.png" width="140" height="120" />
  <img src="/images/cv2.png" width="140" height="120" />
  <img src="/images/cv3.png" width="140" height="120" />
  <img src="/images/cv.png" width="140" height="120" />
</p>

- after collection the data train the RNN models by running `traficForecast.ipynb`. you can skip the training process and load models from `models` directory.  

## Results
| Metrics | MAE | MSE | RMSE | MAPE |  R2  | Explained variance score |
| ------- |:---:| :--:| :--: | :--: | :--: | :----------------------: |
| LSTM | 7.097 | 93.554 | 9.672 | 17.059% | 0.942 | 0.942 |
| GRU | 7.267 | 95.928 | 9.794| 19.952% | 0.940 | 0.941 |

- To test the models with your own input run the webapp by going to the `webapp` directory and typing `flask run` from command line. 
The demo webpage will be running on: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

Website Demo Images: 
<p float="left">
  <img src="/images/web1.png" width="220" height="200" />
  <img src="/images/web2.png" width="220" height="200" /> 
  <img src="/images/web3.png" width="220" height="200" />
  <img src="/images/web4.png" width="220" height="200" />
</p>

Website Demo video: [YouTube Link](https://www.youtube.com/watch?v=5iINgD4f1yw&feature=youtu.be)
