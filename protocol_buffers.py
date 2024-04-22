# Commented out IPython magic to ensure Python compatibility.
# Python ≥3.5 is required
import sys
assert sys.version_info >= (3, 5)

# Scikit-Learn ≥0.20 is required
import sklearn
assert sklearn.__version__ >= "0.20"

try:
    # %tensorflow_version only exists in Colab.
#     %tensorflow_version 2.x
    !pip install -q -U tfx==0.21.2
    print("You can safely ignore the package incompatibility errors.")
except Exception:
    pass

# TensorFlow ≥2.0 is required
import tensorflow as tf
from tensorflow import keras
assert tf.__version__ >= "2.0"

# Common imports
import numpy as np
import os

# to make this notebook's output stable across runs
np.random.seed(42)

# To plot pretty figures
# %matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

# Where to save the figures
PROJECT_ROOT_DIR = "."
CHAPTER_ID = "data"
IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR, "images", CHAPTER_ID)
os.makedirs(IMAGES_PATH, exist_ok=True)

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)

"""First let's write a simple protobuf definition:"""

# Commented out IPython magic to ensure Python compatibility.
# 
# %%writefile person.proto
# syntax = "proto3";
# message Person {
#   string name = 1;
#   int32 id = 2;
#   repeated string email = 3;
# }

"""Overwriting person.proto

And let's compile it (the --descriptor_set_out and --include_imports options are only required for the tf.io.decode_proto() example below):
"""

!protoc person.proto --python_out=. --descriptor_set_out=person.desc --include_imports

!ls person*

from person_pb2 import Person

person = Person(name="Al", id=123, email=["a@b.com"])  # create a Person
print(person)  # display the Person

person.name  # read a field

person.name = "Alice"  # modify a field

person.email[0]  # repeated fields can be accessed like arrays

person.email.append("c@d.com")  # add an email address

print(person)

person.email[1]

s = person.SerializeToString()  # serialize to a byte string
s

person2 = Person()  # create a new Person
person2.ParseFromString(s)  # parse the byte string (27 bytes)

person == person2  # now they are equal

print(person2)
