<div align="center" markdown> 
<img src="https://i.imgur.com/UdBujFN.png" width="250"/> <br> 

# Import StrawDI dataset

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#license">License</a> •
  <a href="#acknowledgement">Acknowledgement</a> •
  <a href="#statistics">Statistics</a> •
  <a href="#examples">Examples</a> •
</p>

[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack) 
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/import-StrawDI-dataset)
[![views](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/import-StrawDI-dataset&counter=views&label=views)](https://supervise.ly)
[![downloads](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/import-StrawDI-dataset&counter=downloads&label=downloads)](https://supervise.ly)
</div>

## Overview 

App downloads data from official [StrawDI](https://strawdi.github.io/). After extraction data is converted to [Supervisely](https://app.supervise.ly) format.  

`Import StrawDI dataset` contains 3100 images of strawberries, taken from 20 plantations, within an approximate area of 150 hectares, in the province of Huelva, Spain. The plantations were not changed in any way for the experiment and the images were taken from real production conditions during a full picking campaign.

The capture device used was a Samsung Galaxy S7 Edge smartphone attached to an extendable arm. In order to build a data set close to the target application, the images were taken under different conditions of brightness, at a distance of approximately 20 cm from the ridge, at about 35 +-10 cm height and an approximate angle of 25 +-10º. The images have a 4032x3024 resolution and are stored in a `JPEG` format.

To reduce the computational demands on the models, the images have been rescaled to 1008 x 756 and stored in `PNG` format. Project is divided into train (2800 images), validation (100 images) and test (200 images) subsets.

<img src="https://i.imgur.com/J5MQcfW.png" style="max-height: 200px; width: auto;"/>

## [License](https://strawdi.github.io/)

This dataset is made freely available to academic and non-academic entities for non-commercial purposes such as academic research, teaching, scientific publications, or personal experimentation. Permission is granted to use the data given that you agree:

1. That the dataset comes “AS IS”, without express or implied warranty. Although every effort has been made to ensure accuracy, we (Isaac Perez-Borrero, Diego Marin, Manuel E. Gegundez-Arias and Estefanía Cortés-Ancos) do not accept any responsibility for errors or omissions.
2. That you include a reference to the StrawDI_Db1 Dataset in any work that makes use of the dataset. For research papers, cite our preferred publication as listed on [Using the database](https://strawdi.github.io/#using-the-database) Section.
3. That you do not distribute this dataset or modified versions. It is permissible to distribute derivative works in as far as they are abstract representations of this dataset (such as models trained on it or additional annotations that do not directly include any of our data) and do not allow to recover the dataset or something similar in character.
4. That you may not use the dataset or any derivative work for commercial purposes as, for example, licensing or selling the data, or using the data with a purpose to procure a commercial gain.
5. That all rights not expressly granted to you are reserved by us (Isaac Perez-Borrero, Diego Marin, Manuel E. Gegundez-Arias and Estefanía Cortés-Ancos).

## Acknowledgement

Please include the following acknowledgment…

```
Kindly provided by the StrawDI Team (see https://strawdi.github.io/).
```

…as well as a reference to the following paper:

```
@article{PEREZBORRERO2020105736,
title = "A fast and accurate deep learning method for strawberry instance segmentation",
journal = "Computers and Electronics in Agriculture",
volume = "178",
pages = "105736",
year = "2020",
issn = "0168-1699",
doi = "https://doi.org/10.1016/j.compag.2020.105736",
url = "http://www.sciencedirect.com/science/article/pii/S0168169920300624",
author = "Isaac Pérez-Borrero and Diego Marín-Santos and Manuel E. Gegúndez-Arias and Estefanía Cortés-Ancos"
}
```

To inform authors of a publication using StrawDI_Db1, or to give any other feedback, please contact [Isaac Pérez](mailto:isaac.perez@dci.uhu.es) or [Diego Marin](mailto:diego.marin@diesia.uhu.es).

## Statistics

Project contains 3 datasets with 3100 images in it, with a total of 17938 annotated objects. 

![](https://i.imgur.com/qcZmgkF.png)

## Examples

| <img src="https://i.imgur.com/kaQRk35.png" style="max-height: 600px; width: auto;"/> | <img src="https://i.imgur.com/fsp144B.png" style="max-height: 600px; width: auto;"/> | <img src="https://i.imgur.com/i9bUvm1.png" style="max-height: 600px; width: auto;"/> | <img src="https://i.imgur.com/dHWCUiV.png" style="max-height: 600px; width: auto;"/> |
| :----------------------------------------------------------: | :----------------------------------------------------------: | ------------------------------------------------------------ | ------------------------------------------------------------ |
| <img src="https://i.imgur.com/os0pm2K.png" style="max-height: 600px; width: auto;"/> | <img src="https://i.imgur.com/xxOko2U.png" style="max-height: 600px; width: auto;"/> | <img src="https://i.imgur.com/wwQCw8D.png" style="max-height: 600px; width: auto;"/> | <img src="https://i.imgur.com/OdXzkHW.png" style="max-height: 600px; width: auto;"/> |

