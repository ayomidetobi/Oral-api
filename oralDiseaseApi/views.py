from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# views.py
from django.http import JsonResponse
import torch
from torchvision import transforms,models
from PIL import Image
import torch.nn as nn
# Define your model class and any other necessary functions here
class_labels = {
    0: "calculus",
    1: "caries",
    2: "gingivitis",
    3: "hypodontia",
    4: "toothDiscoloration",
    5: "ulcers"
}
@csrf_exempt
def predict(request):
    if request.method == 'POST': 
        # Load the image from the request
        image_file = request.FILES.get('image')
         # Check if the request contains an image
        if 'image' not in request.FILES:
            return JsonResponse({'error': 'Image file not found in the request'}, status=400)

        # Load the image from the request
        image_file = request.FILES['image']

        # Check if the uploaded file is a JPEG
        if not image_file.name.endswith('.jpg') and not image_file.name.endswith('.jpeg')and not image_file.name.endswith('.JPEG')and not image_file.name.endswith('.JPG'):
            return JsonResponse({'error': 'Only JPEG files are supported'}, status=400)

        # Open the image using PIL
        try:
            image = Image.open(image_file)
        except Exception as e:
            return JsonResponse({'error': 'Failed to open image: ' + str(e)}, status=400)
        
        
        # Preprocess the image
        transform = transforms.Compose([
            transforms.Resize((299, 299)),  # Inception models expect 299x299 inputs
            # transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
        image = transform(image).unsqueeze(0)
        num_classes = 6  # Change this to the number of output classes in your checkpoint
       
        # Load the model and make predictions
        model = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V1)
        num_ftrs = model.fc.in_features
        model.fc = nn.Linear(num_ftrs, num_classes)

        model.load_state_dict(torch.load('./crossVIT_transformer_oral_disease_classifier.pth',map_location=torch.device('cpu')))
        model.eval()
        with torch.no_grad():
            output = model(image)
            predicted_class = torch.argmax(output).item()
            predicted_label = class_labels[predicted_class]
        # Return the predicted class as JSON response
        return JsonResponse({'predicted_class': predicted_label})
    else:
        return JsonResponse({'error': 'POST request required'})

# urls.py

