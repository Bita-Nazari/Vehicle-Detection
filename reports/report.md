# 1. Data Inspection and Quality Analysis

## 1.1 Dataset Overview

This project focuses on **vehicle image classification**, with the objective of classifying vehicle images into eight predefined classes.

The dataset contains:

* **3,330 training images**
* **400 test images**
* **8 vehicle classes**

The following data quality checks were performed before model training:

* Corrupted image detection
* Duplicate image detection within the training set
* Duplicate image detection within the test set
* Train-test duplicate detection
* Class distribution analysis
* Image format and color mode analysis
* Image size analysis
* Random sample visualization from each class

---

## 1.2 Corrupted Image Detection

The dataset was first checked for corrupted or unreadable image files.

| Dataset | Number of Corrupted Images |
| ------- | -------------------------: |
| Train   |                          0 |
| Test    |                          0 |

No corrupted images were found in either the training or test datasets. Therefore, no images needed to be removed due to file corruption.

---

## 1.3 Duplicate Image Detection

Duplicate images were checked both within each dataset and between the training and test sets.

### Duplicates Within the Training Set

One duplicate pair was identified within the training dataset:

```text
train/vanet/214785158.jpg
train/savari/214785158.jpg
```

The same image appears in two different classes (`vanet` and `savari`), indicating a potential **label conflict** rather than a simple duplicate.

### Duplicates Within the Test Set

No duplicate images were found within the test dataset.

| Dataset | Number of Duplicate Images |
| ------- | -------------------------: |
| Train   |                          1 |
| Test    |                          0 |

---

## 1.4 Train-Test Duplicate Detection

A total of **8 images** were found to be duplicated between the training and test datasets.

These images included:

* 6 duplicate images from the `ambulance` class
* 2 duplicate images from the `minibus` class

test/ambulance/200396165.jpg', train/ambulance/200396165.jpg',
test/ambulance/214830125.jpg', train/ambulance/214830125.jpg',
test/ambulance/215713763.jpg', train/ambulance/215713763.jpg', 
test/ambulance/216095686.jpg', train/ambulance/216095686.jpg',
test/ambulance/217040489.jpg', train/ambulance/217040489.jpg',
test/ambulance/218089422.jpg', train/ambulance/218089422.jpg',
test/minibus/218138154.jpg'  , train/minibus/218138154.jpg',
test/minibus/218307381.jpg'  , train/minibus/218307381.jpg'

This issue is particularly important because having identical images in both the training and test sets can lead to **data leakage**. In such cases, the model may encounter the exact same images during training and evaluation, resulting in an overly optimistic estimate of its generalization performance.

Therefore, the **train-test duplicate images should be removed from the appropriate dataset before model training and final evaluation**.

---

## 1.5 Class Distribution

The distribution of images across the eight training classes was analyzed to identify potential class imbalance.

| Class     | Number of Images | Percentage |
| --------- | ---------------: | ---------: |
| Ambulance |              358 |     10.75% |
| Autobus   |              470 |     14.11% |
| Kamyun    |              496 |     14.89% |
| Kamyunet  |              455 |     13.66% |
| Minibus   |              413 |     12.40% |
| Savari    |              500 |     15.01% |
| Taxi      |              488 |     14.65% |
| Vanet     |              151 |      4.53% |

The `vanet` class has the lowest number of samples, with **151 images (4.53%)**, while the `savari` class has the highest number of samples, with **500 images (15.01%)**.

This indicates that the dataset is **not perfectly balanced**, with the `vanet` class being significantly underrepresented compared with the other classes. This imbalance should be considered during model training and evaluation, as it may affect the model's performance on the minority class.

---

## 1.6 Image Format, Color Mode, and Size Analysis

The training images were analyzed in terms of file format, color mode, and image dimensions.

The analysis showed that all **3,331 analyzed images** have the same format and color mode:

* **Format:** JPEG
* **Color Mode:** RGB

However, the image dimensions are not consistent across the dataset. Several different image sizes were observed.

The most frequent image dimensions were:

| Image Size | Number of Images |
| ---------- | ---------------: |
| 198 × 264  |              122 |
| 189 × 252  |              107 |
| 186 × 252  |               99 |
| 177 × 240  |               68 |
| 198 × 252  |               67 |
| 207 × 276  |               56 |
| 180 × 240  |               54 |
| 171 × 228  |               44 |
| 210 × 276  |               41 |
| 189 × 240  |               41 |

Other image dimensions were also present with lower frequencies.

Although the image format and color mode are consistent, the dataset contains images with different spatial dimensions. This indicates that the images were collected from different sources and were not originally standardized to a single resolution.

Therefore, a fixed input size will be required during the preprocessing stage before feeding the images into the CNN models.

---

## 1.7 Random Sample Visualization

To visually inspect the dataset and verify the correctness of the class labels, **eight randomly selected images from each class** were displayed.

This visualization was used to:

* Verify that the images correspond to their assigned labels.
* Identify visually unusual or low-quality samples.
* Examine the visual variation within each class.
* Gain an initial understanding of the differences between vehicle classes.
* Identify potential similarities between visually related classes.

The random samples provide an initial qualitative assessment of the dataset before proceeding to preprocessing and model training.

---

## 1.8 Summary of Data Quality Analysis

The initial data inspection revealed the following:

* No corrupted images were detected.
* One duplicate pair was found within the training dataset.
* No duplicates were found within the test dataset.
* Eight train-test duplicate images were identified, which may cause **data leakage**.
* The `vanet` class is significantly underrepresented compared with the other classes.
* All analyzed images are in **JPEG format** and use **RGB color mode**.
* Image dimensions vary considerably across the dataset.
* Random visual inspection was performed using eight samples from each class.

Based on these findings, the main data preparation steps before model training are to **remove train-test duplicates, resolve the identified duplicate/label conflict, standardize image dimensions, and consider the class imbalance during model development and evaluation**.
