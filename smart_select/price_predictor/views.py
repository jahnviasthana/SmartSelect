from django.shortcuts import render
from django.http import JsonResponse
import numpy as np
import pickle
import os

# ✅ Load the model
model_path = "C:/Users/Khushi/OneDrive/Desktop/final_major/final_year_major_project/smart_select/price_predictor/static/model_laptop.pkl"

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")

with open(model_path, "rb") as f:
    model = pickle.load(f)

# ✅ Prediction Page
def prediction(request):
    return render(request, 'prediction.html')

# ✅ Tablet Page
def tablet(request):
    return render(request, 'tablet.html')

# ✅ Laptop Prediction View
def laptop(request):
    if request.method == "POST":
        try:
            # ✅ Get form data
            company = request.POST.get("company", "").strip()
            typename = request.POST.get("typename", "").strip()
            ram = int(request.POST.get("ram", "0").strip())
            weight = float(request.POST.get("weight", "0").strip())
            touchscreen = int(request.POST.get("touchscreen", "0").strip())
            ips = int(request.POST.get("ips", "0").strip())
            resolution = request.POST.get("resolution", "").strip()
            inches = float(request.POST.get("inches", "0").strip())
            cpu_brand = request.POST.get("cpu_brand", "").strip()
            hdd = int(request.POST.get("hdd", "0").strip())
            ssd = int(request.POST.get("ssd", "0").strip())
            gpu_brand = request.POST.get("gpu_brand", "").strip()
            os = request.POST.get("os", "").strip()

            # ✅ Convert resolution (width * height)
            try:
                x_res, y_res = map(int, resolution.lower().replace(" ", "").split("x"))
            except ValueError:
                return JsonResponse({"error": "Invalid resolution format. Use '1920x1080' format."}, status=400)

            # ✅ Calculate PPI (Pixels Per Inch)
            ppi = ((x_res ** 2 + y_res ** 2) ** 0.5) / inches

            # ✅ Prepare input for model prediction
            input_features = np.array([[company, typename, ram, weight, touchscreen, ips, ppi, cpu_brand, hdd, ssd, gpu_brand, os]])

            # ✅ Make prediction and apply np.exp()
            predicted_price = np.exp(model.predict(input_features)[0])  

            return JsonResponse({"predicted_price": round(predicted_price, 2)})

        except ValueError:
            return JsonResponse({"error": "Invalid input values. Please check all fields."}, status=400)

    return render(request, "laptop.html")
