import argparse

def pytorch2onnx(args):
    # PyTorch exports to ONNX without the need for an external converter
    import torch
    from torch.autograd import Variable
    import torch.onnx
    import torchvision
    import onnx
    from onnx_tf.backend import prepare 


    # Create input with the correct dimensions of the input of your model
    if args.model_input_shapes == None:
        raise ValueError("Please provide --model_input_shapes to convert Pytorch models.")
    dummy_model_input = []
    if len(args.model_input_shapes) == 1:
        dummy_model_input = Variable(torch.randn(*args.model_input_shapes))
    else:
        for shape in args.model_input_shapes:
            dummy_model_input.append(Variable(torch.randn(*shape)))

    # load the PyTorch model
    model = torch.load(args.model, map_location="cpu")

    # export the PyTorch model as an ONNX protobuf
    torch.onnx.export(model, dummy_model_input, args.output_onnx_path)

    # load ONNX model
    onnx_model = onnx.load(args.output_onnx_path)
    # convert to tenorflow
    tf_rep = prepare(onnx_model)
    # export tensorflow model
    tf_rep.export_graph(args.model_output_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--model", required=False, help="The path of the model to be converted.")
    parser.add_argument("--output_onnx_path", required=False, help="The desired path to store the converted .onnx file")
    parser.add_argument("--model_output_path", required=False, help="The desired path to store the converted tensorflow file")
    parser.add_argument(
        "--model_input_shapes",
        required=False,
        type=shape_type,
        help=
        "Required for Pytorch models. List of tuples. The input shape(s) of the model. Each dimension separated by ','."
    )
        
    args = parser.parse_args()

    pytorch2onnx(args)