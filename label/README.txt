如何整理数据并实现机器学习
1.对于未进行标注的长途驾驶，在获取events.txt和gsv.txt以后，使用label.py和replace.py来获取gsv-labeled.txt
2.可使用label_image.py来生成可视化图表来发现室内室外与卫星数量及snr之间的联系
3.可使用data_analyse.py来生成含有satellite_count, average_snr, satellite_change和inside_outside的训练txt（默认名字为output）
4.使用ML.py（random Forrest 或 logistic regression）来生成模型（默认名字为inside_outside_model.pkl）
5.可使用ML_test来测试模型，测试数据集需要与data_analyse.py生成的txt文件格式相同，可使用add_inside_outside来格式化
6.测试报告会告知模型对于该测试案例的精准度