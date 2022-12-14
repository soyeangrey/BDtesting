# -*- coding: utf-8 -*-
"""Copy of sampleBD.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XOocwY_i1G66jbvVr2O1kGxgU-tmiZ3H
"""

import numpy as np

import numpy as np

from ipywidgets import interact
import numpy as np

from bokeh.io import push_notebook, show, output_notebook
from bokeh.plotting import figure
output_notebook()
x = np.linspace(0, 2*np.pi, 2000)
y = np.sin(x)
p = figure(title="simple line example", height=300, width=600, y_range=(-5,5),
           background_fill_color='#efefef')
r = p.line(x, y, color="#8888cc", line_width=1.5, alpha=0.8)
def update(f, w=1, A=1, phi=0):
    if   f == "sin": func = np.sin
    elif f == "cos": func = np.cos
    r.data_source.data['y'] = A * func(w * x + phi)
    push_notebook()
show(p, notebook_handle=True)
interact(update, f=["sin", "cos"], w=(0,50), A=(1,10), phi=(0, 20, 0.1))









show(p, notebook_handle=True)

interact(update, f=["sin", "cos"], w=(0,50), A=(1,10), phi=(0, 20, 0.1))

a = np.arange(6)

import pandas as pd

df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],
                    'value': [1, 2, 3, 5]})

#try stats functions to fit distribution
from scipy import stats
from scipy.stats import norm
print('bounds of distribution lower: %s, upper: %s' % norm.support())

rv = norm()

dist_discrete = [d for d in dir(stats) if
...                  isinstance(getattr(stats, d), stats.rv_discrete)]

def rosen(x):
...     """The Rosenbrock function"""
...     return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

from sklearn import linear_model

reg = linear_model.LinearRegression()

reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])

reg.coef_

from sklearn import linear_model

reg = linear_model.Ridge(alpha=.5)

reg.fit([[0, 0], [0, 0], [1, 1]], [0, .1, 1])

import seaborn as sns

sns.set_theme()

tips = sns.load_dataset("tips")
 
# Create a visualization
sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)

fmri = sns.load_dataset("fmri")
sns.relplot(
    data=fmri, kind="line",
    x="timepoint", y="signal", col="region",
    hue="event", style="event",
)

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 5, 0.1)
y = np.sin(x)
plt.plot(x, y)

import spacy

nlp = spacy.load("en_core_web_sm")
 
# Process whole documents
text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. ???I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn???t "
        "worth talking to,??? said Thrun, in an interview with Recode earlier "
        "this week.")
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

from gensim import corpora, models, similarities, downloader

import pprint
document = "Human machine interface for lab abc computer applications"
text_corpus = [
    "Human machine interface for lab abc computer applications",
    "A survey of user opinion of computer system response time",
    "The EPS user interface management system",
    "System and human system engineering testing of EPS",
    "Relation of user perceived response time to error measurement",
    "The generation of random binary unordered trees",
    "The intersection graph of paths in trees",
    "Graph minors IV Widths of trees and well quasi ordering",
    "Graph minors A survey",
]
 
# Create a set of frequent words
stoplist = set('for a of the and to in'.split(' '))
# Lowercase each document, split it by white space and filter out stopwords
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in text_corpus]

# Count word frequencies
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

# Only keep words that appear more than once
processed_corpus = [[token for token in text if frequency[token] > 1] for text in texts]
pprint.pprint(processed_corpus)
 
from gensim import corpora

dictionary = corpora.Dictionary(processed_corpus)
print(dictionary)

import tensorflow as tf
print("TensorFlow version:", tf.__version__)

import tensorflow as tf
print("TensorFlow version:", tf.__version__)

mnist = tf.keras.datasets.mnist
 
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
 
 
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

# Commented out IPython magic to ensure Python compatibility.
 
# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()


from mnist import MNIST
data = MNIST(data_dir="data/MNIST/")

print("Size of:")
print("- Training-set:\t\t{}".format(data.num_train))
print("- Validation-set:\t{}".format(data.num_val))
print("- Test-set:\t\t{}".format(data.num_test))

import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

# Download training data from open datasets.
training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor(),
)

# Download test data from open datasets.
test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor(),
)

batch_size = 64

# Create data loaders.
train_dataloader = DataLoader(training_data, batch_size=batch_size)
test_dataloader = DataLoader(test_data, batch_size=batch_size)

for X, y in test_dataloader:
    print(f"Shape of X [N, C, H, W]: {X.shape}")
    print(f"Shape of y: {y.shape} {y.dtype}")
    break

# Get cpu or gpu device for training.
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using {device} device")

# Define model
class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10)
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

model = NeuralNetwork().to(device)
print(model)

import numpy as np
import torch
import matplotlib.pyplot as plt
from matplotlib import colors
plt.rcParams.update({'font.size': 16})

x = torch.rand(20, 5)
x

input_dim = 1
output_dim = 1
 
A = 2 * np.random.rand(output_dim, input_dim) - 1
b = 2 * np.random.rand(output_dim) - 1
 
true_model = lambda x: A @ x + b

n_train = 1000
noise_level = 0.04
 
# Generate a random set of n_train samples
X_train = np.random.rand(n_train, input_dim)
y_train = np.array([true_model(x) for x in X_train])
 
# Add some noise
y_train += noise_level * np.random.standard_normal(size=y_train.shape)
 
if input_dim == output_dim == 1:
   fig = plt.figure()
   fig.clf()
   ax = fig.gca()
   ax.plot(X_train, y_train, '.')
   ax.grid(True)
   ax.set_xlabel('X_train')
   ax.set_ylabel('y_train')

import torch.nn as nn
import torch
 
#%% Linear layer
class LinearModel(nn.Module):
   def __init__(self, input_dim, output_dim):
       super(LinearModel, self).__init__()
 
       self.input_dim = input_dim
       self.output_dim = output_dim
 
       self.linear = nn.Linear(self.input_dim, self.output_dim, bias=True)
 
   def forward(self, x):
       out = self.linear(x)
       return out
  
   def reset(self):
       self.linear.reset_parameters()
model = LinearModel(input_dim, output_dim)

# Commented out IPython magic to ensure Python compatibility.
!python -c "import monai" || pip install -q "monai-weekly[nibabel, tensorboard]"
!python -c "import matplotlib" || pip install -q matplotlib
!python -c "import catalyst" || pip install -q catalyst==20.07
# %matplotlib inline



# Copyright 2020 MONAI Consortium
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import glob
import logging
import os
import shutil
import sys
import tempfile

import catalyst.dl
import matplotlib.pyplot as plt
import nibabel as nib
import numpy as np
from monai.config import print_config
from monai.data import Dataset, create_test_image_3d, list_data_collate, decollate_batch, DataLoader
from monai.inferers import sliding_window_inference
from monai.losses import DiceLoss
from monai.metrics import DiceMetric
from monai.networks.nets import UNet
from monai.transforms import (
    Activations,
    EnsureChannelFirstd,
    AsDiscrete,
    Compose,
    LoadImaged,
    RandCropByPosNegLabeld,
    RandRotate90d,
    ScaleIntensityd,
)
from monai.utils import first

import torch

print_config()

!pip install napari
!pip install SimpleITK

import napari
from skimage.data import astronaut

# create the viewer and display the image
viewer = napari.view_image(astronaut(), rgb=True)

from skimage import data
import napari
 
 
viewer = napari.view_image(data.moon())

!pip install PyDICOM
!pip install scanpy

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import scanpy as sc
import matplotlib.pyplot as plt

sc.settings.verbosity = 3             # verbosity: errors (0), warnings (1), info (2), hints (3)
#sc.logging.print_versions()

sc.settings.set_figure_params(dpi=80)
# %matplotlib inline

import numpy as np
import pandas as pd
import anndata as ad
from scipy.sparse import csr_matrix
print(ad.__version__)

counts = csr_matrix(np.random.poisson(1, size=(100, 2000)), dtype=np.float32)
adata = ad.AnnData(counts)
adata
adata.X
 
 
adata.obs_names = [f"Cell_{i:d}" for i in range(adata.n_obs)]
adata.var_names = [f"Gene_{i:d}" for i in range(adata.n_vars)]
print(adata.obs_names[:10])

!pip freeze > requirements.txt