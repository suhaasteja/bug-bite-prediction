from flask import Flask, render_template, request, jsonify
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import torch

app = Flask(__name__)

model = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()

def transform_image(image_bytes):
    my_transforms = transforms.Compose([
        transforms.Resize((800, 800)),
        transforms.ToTensor()
    ])
    image = Image.open(image_bytes)
    return my_transforms(image)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img = transform_image(file)
        img = img.unsqueeze(0)  # model expects a batch
        with torch.no_grad():
            prediction = model(img)
        prediction = [{k: v.numpy().tolist() for k, v in t.items()} for t in prediction]
        return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
