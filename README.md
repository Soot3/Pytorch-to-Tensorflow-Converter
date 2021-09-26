# Pytorch-to-Tensorflow-Converter
Provides easy conversion of trained PyTorch models to their Tensorflow equivalents using ONNX as the mechanism.

## How to Run 
The tool can be used as a docker image or used as is with python.

**Sample Docker Image**
sootersaalu/pyt_tf_convert

### Docker Steps 
Run this command to pull the docker image to your machine
```
docker pull sootersaalu/pyt_tf_convert
```
Then use this template to convert your model
```
docker run -v sootersaalu/pyt_tf_convert --model <model_path> --output_onnx_path <path for the intial onnx convert> --model_output_path <path for the final model> --model_input_shapes <Input shapes used for your PyTorch model, dimensions separated by a ','>
```
**Example**

```
docker run -v sootersaalu/pyt_tf_convert --model ./potato.pth --output_onnx_path ./middle.onnx --model_output_path ./final --model_input_shapes 1,3,128,128
```

### Python Steps

First clone this repo

```
git clone https://github.com/Soot3/Pytorch-to-Tensorflow-Converter.git
```

Then run the .py file directly with your parameters
```
python ./Pytorch-to-Tensorflow-Converter/src/pytorch2tensorflow.py --model <model_path> --output_onnx_path <path for the intial onnx convert> --model_output_path <path for the final model> --model_input_shapes <Input shapes used for your PyTorch model, dimensions separated by a ','>
```


**Example**

```
python ./Pytorch-to-Tensorflow-Converter/src/pytorch2tensorflow.py --model ./potato.pth --output_onnx_path ./middle.onnx --model_output_path ./final --model_input_shapes 1,3,128,128
```
