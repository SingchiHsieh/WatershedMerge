import time
import tool

from watershed import Watershed
from skimage import future,io,segmentation,color
from skimage.measure import regionprops

if __name__ == "__main__":
    import cv2

    w = Watershed()

    starttime = time.time()

    color_img = cv2.imread("/Users/arthur/BSR/BSDS500/data/images/test/3063.jpg")

    img = color_img
    # show_img(img)
    # labels = segmentation.slic(img, compactness=30, n_segments=400)  # Using SLIC to segment pic 先用SLIC分割图像
    gray_img = cv2.cvtColor(color_img, cv2.COLOR_RGB2GRAY)

    # 转换到lab色彩空间，最后计算色差deltaE2000
    lab_img = cv2.cvtColor(color_img, cv2.COLOR_RGB2LAB)

    # 灰度图像应用于传统分水岭算法
    labels = w.apply(gray_img)

    for i in range(labels.shape[0]):
        for j in range(labels.shape[1]):
            if (labels[i][j] == 0):
                color_img[i][j] = [0,255,0]

    cv2.imshow('mark', color_img)

    # cv2.imwrite('results/watershed/watershed9.jpg',labels)
    labels = labels + 1  # So that no labelled region is 0 and ignored by regionprops
    # cv2.imwrite('./results/watershed/watershedPlus9.jpg',labels)
    # regions = regionprops(labels)  # regionprops helps us compute various features of these regions. 计算每块的多种特征，用于后面按照特征合并用

    # label_lab = color.label2rgb(labels, lab_img,kind='avg')  # The label2rgb function assigns a specific color to all pixels belonging to one region (having the same label).给属于同一类型的像素一样的颜色
    #
    # label_lab = segmentation.mark_boundaries(lab_img, labels, (0, 0, 0))  # 把分割线画出来
    # io.imsave('./results/LabelLAB/label_img9.jpg', label_lab)

    # g = future.graph.rag_mean_color(lab_img, labels)  # 计算每个小图块的权重，两个图块越相似权重越接近，这里用图块的像素均值作为每个图块的权重值
    #
    # labels2 = future.graph.merge_hierarchical(labels, g, thresh=50,
    #                                    rag_copy=False,
    #                                    in_place_merge=True,
    #                                    merge_func=tool.merge_mean_color,
    #                                    weight_func=tool._weight_mean_color)  # 合并权重相近的图块
    # # io.imsave('./results/merlabel/9.jpg', labels2)
    # label_rgb2 = color.label2rgb(labels2, img, kind='avg')
    # io.imsave('./results/merge25/11.jpg', label_rgb2)
    # label_rgb2 = segmentation.mark_boundaries(label_rgb2, labels2, (255, 255, 255))
    # # io.imsave('./results/merge2/09.jpg', label_rgb2)
    #
    # endtime = time.time()
    # print('总共的时间为:', round(endtime - starttime, 2), 'secs')
    cv2.waitKey();


